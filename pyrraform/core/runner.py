from typing import List

from pyrraform.core.models.shellcommand import ShellCommand, ShellCommandOutput
import subprocess


class ShellCommandRunner:
    def __init__(self, command: ShellCommand):
        """Create a command runner for a ShellCommand

        Args:
            command (ShellCommand): The command to run.

        """
        self._command: ShellCommand = command

    @property
    def command(self):
        return self._command

    def _generate_subprocess_command(self) -> List[str]:
        """Transform a ShellCommand object into a command format accepted by subprocess module.
        The function output is a list of string with:
         - The command name
         - the arguments
         - the options (name & value)
         - the tags (i.e options, with no value

        Returns:
            List[str]: The command in a list of string format

        Examples:
            > _generate_subprocess_command(cmd)
            >> ['command', 'arg1', 'arg2', '--option1', 'value', '--flag']

        """
        # First add the command name
        cmd = [self._command.name]

        # Add command arguments
        for arg in self._command.args:
            cmd.append(arg)

        # Add command options (name and value)
        for option in self._command.options:
            option_name, option_value = self._command.get_option(option)
            cmd.append(option_name)
            cmd.append(option_value)

        # Add command flags
        for flag in self._command.flags:
            cmd.append(self._command.get_flag(flag))

        return cmd

    def run(self) -> ShellCommandOutput:
        """Actually run the command using subprocess module.

        Returns:
            ShellCommandOutput

        """
        subprocess_cmd = self._generate_subprocess_command()
        process = subprocess.Popen(subprocess_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        command_output = ShellCommandOutput(return_code=process.returncode,
                                            error=str(stderr, 'utf-8'),
                                            output=str(stdout, 'utf-8'))
        return command_output
