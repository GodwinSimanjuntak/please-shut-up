from textutil import title_case, truncate
from stats import average, median


def test_title_case():
    assert title_case("hello  world") == "Hello  World"


def test_truncate():
    assert truncate("abcdefgh", 6) == "abc..."
    assert truncate("abc", 6) == "abc"


def test_average_empty():
    assert average([]) == 0


def test_median_even():
    assert median([4, 1, 3, 2]) == 2.5
    assert median([3, 1, 2]) == 2
