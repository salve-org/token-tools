from token_tools import (
    merge_tokens,
    overwrite_and_merge_tokens,
    overwrite_tokens,
)


def test_merge_tokens():
    assert merge_tokens([]) == []
    assert merge_tokens([((1, 0), 2, "Test")]) == [((1, 0), 2, "Test")]
    assert merge_tokens([((1, 0), 2, "Test"), ((1, 2), 2, "Test")]) == [
        ((1, 0), 4, "Test")
    ]
    assert merge_tokens([((1, 0), 2, "Test"), ((1, 2), 2, "Test2")]) == [
        ((1, 0), 2, "Test"),
        ((1, 2), 2, "Test2"),
    ]
    assert merge_tokens(
        [((1, 0), 2, "Test"), ((1, 2), 2, "Test"), ((1, 4), 2, "Test")]
    ) == [((1, 0), 6, "Test")]
    assert merge_tokens(
        [((1, 0), 2, "Test"), ((1, 2), 2, "Test"), ((1, 4), 2, "Test2")]
    ) == [((1, 0), 4, "Test"), ((1, 4), 2, "Test2")]


def test_overwrite_tokens():
    assert overwrite_tokens([((1, 0), 2, "Test")], []) == [((1, 0), 2, "Test")]
    assert overwrite_tokens([], [((1, 0), 2, "Test")]) == [((1, 0), 2, "Test")]
    assert overwrite_tokens([((1, 0), 2, "Test")], [((1, 1), 2, "Test")]) == [
        ((1, 0), 1, "Test"),
        ((1, 1), 2, "Test"),
    ]


def test_overwrite_and_merge_tokens():
    assert overwrite_and_merge_tokens(
        [((1, 0), 2, "Test"), ((1, 2), 2, "Test"), ((1, 4), 2, "Test3")],
        [((1, 2), 2, "Test2")],
    ) == [((1, 0), 2, "Test"), ((1, 2), 2, "Test2"), ((1, 4), 2, "Test3")]
    assert overwrite_and_merge_tokens(
        [((1, 0), 2, "Test"), ((1, 2), 2, "Test"), ((1, 4), 2, "Test2")], []
    ) == [((1, 0), 4, "Test"), ((1, 4), 2, "Test2")]
    assert overwrite_and_merge_tokens(
        [((1, 0), 2, "Test"), ((1, 2), 2, "Test"), ((1, 4), 2, "Test2")],
        [((1, 6), 2, "Test2")],
    ) == [((1, 0), 4, "Test"), ((1, 4), 4, "Test2")]
    pass
