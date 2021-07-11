from core.models.shellcommand import ShellCommand


def test_shellcommand_has_flag_true():
    cmd = ShellCommand('command', flags=['flag'])
    assert cmd.has_flag('flag') is True


def test_shellcommand_has_not_flag():
    cmd = ShellCommand('command', flags=['flag'])
    assert cmd.has_flag('bad-flag') is False
