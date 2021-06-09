"""
Author: Jose Stovall | oitsjustjose
"""

from typing import Union

from pip._vendor.colorama import Fore


def _with_color(msg: str, color: str) -> None:
    """
    Prints anything with some color
    """
    print(f"{color}{msg}{Fore.RESET}")


class Logger:
    """
    A simple logging class
    Arguments:
        name (str|None): the name of the logger, if any
    """

    def __init__(self, name: Union[str, None] = None):
        self._name = name

    def info(self, msg: str) -> None:
        """
        Prints out a message to log
        """
        if self._name:
            _with_color(f"[{self._name}]: {msg}", Fore.WHITE)
        else:
            _with_color(msg, Fore.WHITE)

    def success(self, msg: str) -> None:
        """
        Prints out a successfully finished event/msg
        """
        if self._name:
            _with_color(f"[{self._name}]: {msg}", Fore.GREEN)
        else:
            _with_color(msg, Fore.GREEN)

    def warn(self, msg: str) -> None:
        """
        Prints out a message as a warning
        """
        if self._name:
            _with_color(f"[{self._name}]: {msg}", Fore.YELLOW)
        else:
            _with_color(msg, Fore.YELLOW)

    def err(self, msg: str) -> None:
        """
        Prints out a message as an error
        """
        if self._name:
            _with_color(f"[{self._name}]: {msg}", Fore.RED)
        else:
            _with_color(msg, Fore.RED)

    def notice(self, msg: str) -> None:
        """
        Prints out a notice in a color that will be seen
        """
        if self._name:
            _with_color(f"[{self._name}]: {msg}", Fore.BLUE)
        else:
            _with_color(msg, Fore.BLUE)
