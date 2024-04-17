from hello2 import hello


def test_default():
    hello("John") == "hello, John"


def test_arguments():
    assert hello("John") == "hello, John"
