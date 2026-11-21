from tags import unique_tags


def test_unique_tags():
    assert unique_tags(["b", "a", "b", "c"]) == ["b", "a", "c"]
