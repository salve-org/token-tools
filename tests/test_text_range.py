from token_tools import normal_text_range, only_tokens_in_text_range


def test_normal_text_range():
    code_snippet = """def foo:
        if bar(baz):
            qux()"""

    assert normal_text_range(code_snippet) == (
        ["def foo:", "        if bar(baz):", "            qux()"],
        (1, 3),
    )
    assert normal_text_range(code_snippet, (1, 2)) == (
        ["def foo:", "        if bar(baz):"],
        (1, 2),
    )
    assert normal_text_range(code_snippet, (2, 3)) == (
        ["        if bar(baz):", "            qux()"],
        (2, 3),
    )
    assert normal_text_range("") == (
        [""],
        (1, 1),
    )
    assert normal_text_range("def foo: bar()") == (
        ["def foo: bar()"],
        (1, 1),
    )


def test_only_tokens_in_text_range():
    assert only_tokens_in_text_range(
        [
            ((1, 0), 3, "Name"),
            ((2, 5), 4, "Text"),
            ((3, 2), 6, "Comment"),
            ((4, 0), 1, "Punctuation"),
            ((5, 0), 1, "String"),
        ],
        (2, 4),
    ) == [
        ((2, 5), 4, "Text"),
        ((3, 2), 6, "Comment"),
        ((4, 0), 1, "Punctuation"),
    ]

    assert only_tokens_in_text_range(
        [
            ((1, 0), 3, "Name"),
            ((2, 5), 4, "Text"),
            ((3, 2), 6, "Comment"),
            ((4, 0), 1, "Punctuation"),
            ((5, 0), 1, "String"),
        ],
        (2, 6),
    ) == [
        ((2, 5), 4, "Text"),
        ((3, 2), 6, "Comment"),
        ((4, 0), 1, "Punctuation"),
        ((5, 0), 1, "String"),
    ]
    assert only_tokens_in_text_range([], (2, 6)) == []
