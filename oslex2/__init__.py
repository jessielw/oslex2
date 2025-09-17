import platform
from typing import List

# import OS-specific module
if platform.system() == "Windows":
    import mslex as underlying
else:
    import shlex as underlying


def quote(s: str, **kwargs) -> str:
    """
    Return a shell-escaped version of the string s. The returned value is a string that can safely be used as one token in a shell command line, for cases where you cannot use a list.
    This function is safe to use both for POSIX-compatible shells and for Windows's cmd.
    """
    return underlying.quote(s, **kwargs)


def split(s: str, **kwargs) -> List[str]:
    """
    Split the string s using shell-like syntax.
    This function is safe to use both for POSIX-compatible shells and for Windows's cmd.
    """
    return underlying.split(s, **kwargs)


def join(split_command: List[str]) -> str:
    """
    Concatenate the tokens of the list split_command and return a string. This function is the inverse of split().
    The returned value is shell-escaped to protect against injection vulnerabilities (see quote()).
    This function is safe to use both for POSIX-compatible shells and for Windows's cmd.
    """
    # shlex only has join() since Python 3.8
    # mslex doesn't have it at all
    # It's easier to just implement it without trying to import the functionality
    # Implementation is the same as shlex.join(), see https://github.com/python/cpython/blob/3.8/Lib/shlex.py
    return " ".join(quote(arg) for arg in split_command)
