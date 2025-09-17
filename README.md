# oslex2

[![CI](https://github.com/jessielw/oslex2/actions/workflows/ci.yml/badge.svg)](https://github.com/jessielw/oslex2/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/oslex2.svg)](https://badge.fury.io/py/oslex2)

**oslex2** is an OS-independent wrapper for Python's [`shlex`](https://docs.python.org/3/library/shlex.html) (POSIX) and [`mslex`](https://pypi.org/project/mslex/) (Windows) modules.

> Like `os.path` abstracts over `posixpath` and `ntpath`, `oslex2` abstracts over `shlex` and `mslex` for shell-quoting and splitting.

## Features

- Unified API for shell quoting, splitting, and joining on all platforms
- Automatically uses `shlex` on POSIX and `mslex` on Windows
- Drop-in replacement for `shlex` in cross-platform code

## Installation

```sh
pip install oslex2
```

## Usage

```python
import oslex2

# Safely quote a string for the shell
cmd = oslex2.quote('foo; rm -rf /')

# Split a shell command into arguments
args = oslex2.split('python -m pip install "oslex2>=1.0.0"')

# Join arguments into a shell command
command = oslex2.join(["python", "-m", "pip", "install", "oslex2>=1.0.0"])
```

## API

- `oslex2.quote(s: str, **kwargs) -> str`: Shell-escape a string for safe use as a single token.
- `oslex2.split(s: str, **kwargs) -> List[str]`: Split a shell command string into arguments.
- `oslex2.join(args: List[str]) -> str`: Join arguments into a shell-escaped command string.

**Note:** All functions accept `**kwargs` and pass them through to the underlying `shlex` or `mslex` implementation. This allows you to use platform-specific options (such as `posix`, `punctuation_chars`, etc.) as needed.

## Platform Detection

- On Windows, uses `mslex` for Windows shell syntax.
- On all other platforms, uses the standard library `shlex`.

## License

- MIT License (this library)
- [`mslex`](https://pypi.org/project/mslex/) is Apache 2.0

## Links

- [GitHub](https://github.com/jessielw/oslex2/)
- [PyPI](https://pypi.org/project/oslex2/)
- [mslex on PyPI](https://pypi.org/project/mslex/)
