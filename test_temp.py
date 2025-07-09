from temp import add


def test_add():
    a, b = 1, 2
    result = add(a, b)
    assert result == 3
