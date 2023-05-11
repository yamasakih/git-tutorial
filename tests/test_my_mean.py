import pytest

from tutorial import my_mean


def test_my_mean():
    actual = my_mean([1, 2, 3, 4, 5])
    expected = 3
    assert actual == expected


def test_my_mean_with_empty_list():
    with pytest.raises(ValueError) as e:
        my_mean([])
