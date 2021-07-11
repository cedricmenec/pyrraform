from pyrraform.core.models.shellcommand import ShellCommand, SINGLE_DASH
from pyrraform.core.runner import ShellCommandRunner


def test_generate_subprocess_command():
    test_options = {
        'option-with-dash': 'value-with-dash'
    }
    test_command = ShellCommand('command',
                                args=['arg-with-dash', 'argument with space'],
                                options=test_options,
                                flags=['flag'])
    runner = ShellCommandRunner(test_command)
    expected_result = ['command', 'arg-with-dash', 'argument with space',
                       '--option-with-dash', 'value-with-dash',
                       '--flag']
    result = runner._generate_subprocess_command()
    assert result == expected_result


def test_generate_command_with_double_dash_options():
    test_options = {
        'option1': 1,
        'option2': "value"
    }
    test_command = ShellCommand('command', options=test_options)
    runner = ShellCommandRunner(test_command)
    expected_result = ['command', '--option1', '1', '--option2', 'value']
    result = runner._generate_subprocess_command()
    assert result == expected_result


def test_generate_command_with_single_dash_options():
    test_options = {
        'option1': 1,
        'option2': "value"
    }
    test_config = {
        'option_prefix': SINGLE_DASH
    }
    test_command = ShellCommand('command', options=test_options, config=test_config)
    runner = ShellCommandRunner(test_command)
    expected_result = ['command', '-option1', '1', '-option2', 'value']
    result = runner._generate_subprocess_command()
    assert result == expected_result

# def test_last_command_output(mocker: MockerFixture):
#     """Scenario: A ShellCommandRunner store the last_command_output
#     Given a ShellCommandRunner and an arbitrary ShellCommand,
#     When the runner properly run the command,
#     Then the last_command_output is set with the CommandOutput returned by the execution
#     """
#
#     mocker.patch('pyrraform.core.runner.subprocess.Popen')
#     mocker.patch('pyrraform.core.runner.subprocess.Popen.communicate',
#                  return_value=("", "output"))
#
#     cmd = ShellCommand("command")
#     runner = ShellCommandRunner(cmd)
#     cmd_output = runner.run()
