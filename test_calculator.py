from calculator2 import square
import pytest


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


def tesst_str():
    with pytest.raises(TypeError):
        square("cat")
