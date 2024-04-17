from calculator2 import square


def main():
    test_square()


def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("not true value")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("not true value")
    try:
        assert square(3) == 9
    except AssertionError:
        print("not true value")


if __name__ == "__main__":
    main()
