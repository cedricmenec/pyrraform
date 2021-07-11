from typing import List, Any, Tuple, Optional

DOUBLE_DASH = '--'
SINGLE_DASH = '-'


class ShellCommand:
    def __init__(self, name: str, args: List[str] = None, options: dict = None, flags: List[str] = None,
                 config: dict = None):
        self.name: str = name
        self.args: List[str] = args or []
        self.options: dict = options or {}
        self.flags: List[str] = flags or []

        config = config or {}
        self.config = {
            'option_prefix': config.get("option_prefix", DOUBLE_DASH)
        }

    def add_argument(self, value: str):
        self.args.append(value)

    def add_option(self, name: str, value: Any):
        """Add an option to the Command.
        If the option already exists, its value is updated.

        Args:
            name (str): Option Name
            value (str): Option Value

        Raises:
            ValueError: The option name is not valid.

        """
        if name.startswith(DOUBLE_DASH):
            raw_name = name[:2]
        elif name.startswith(SINGLE_DASH):
            raw_name = name[:1]
        else:
            raw_name = name

        if not raw_name[0].isalpha():
            raise ValueError(f"Command option must start with an alpha character (name: {raw_name}")
        else:
            self.options[name] = value

    def _prepend_prefix(self, name: str):
        """Return the name with the right prefix (single or double dash)

        Args:
            name (str): Raw name of the option or flag (with no dash prefix)

        Returns
            str: The name with the single or double dash prefix.

        """
        return self.config['option_prefix'] + name

    def get_option(self, name) -> Tuple[str, str]:
        """Return the option name (with appropriate prefix) and its value converted to str.

        Args:
            name: Raw name of the option (with no dash prefix)

        Returns:
            Tuple[str, str]: (key, value) of the option

        Raises:
            KeyError: If the request option name is not found.
            `
        Examples:
            > print(get_option('myoption'))
            >> ("--myoption", "value")

        """
        return self._prepend_prefix(name), str(self.options[name])

    def get_flag(self, name) -> str:
        return self._prepend_prefix(name)

    def has_flag(self, name) -> bool:
        return name in self.flags


class ShellCommandOutput:
    def __init__(self, return_code: int, error: Optional[str] = None, output: Optional[str] = None):
        self._return_code: int = return_code
        self._error: Optional[str] = error or ""
        self._output: Optional[str] = output or ""

    @property
    def output(self):
        return self._output

    @property
    def error(self):
        return self._error

    @property
    def return_code(self):
        return self._return_code
