import platform

import oslex2


def test_quote_and_split_roundtrip():
    # Test that quote and split are inverses for simple cases
    args = ["foo", "bar baz", "qux$quux", "'quoted'"]
    joined = oslex2.join(args)
    split = oslex2.split(joined)
    assert split == args


def test_quote_shell_injection():
    # Test that quote properly escapes the string for the shell
    dangerous = "foo; rm -rf /"
    quoted = oslex2.quote(dangerous)
    # The quoted string should not be identical to the original
    assert quoted != dangerous
    # It should be wrapped in quotes (single or double)
    assert quoted.startswith('"') or quoted.startswith("'")


def test_split_basic():
    s = 'a "b c" d'
    result = oslex2.split(s)
    assert result == ["a", "b c", "d"]


def test_platform_underlying():
    if platform.system() == "Windows":
        assert oslex2.underlying.__name__ == "mslex"
    else:
        assert oslex2.underlying.__name__ == "shlex"
