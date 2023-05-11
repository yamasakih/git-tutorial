from tutorial import my_sum


def test_my_sum():
    actual = my_sum(2, 3)
    expected = 5
    assert actual == expected

def test_my_sum_2():
    actual = my_sum(-1000, 50000)
    expected = 49000
    assert actual == expected
