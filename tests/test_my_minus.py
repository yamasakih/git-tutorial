from tutorial import my_minus

def test_my_minus():
    actual = my_minus(1, 10)
    expected = -9
    assert actual == expected