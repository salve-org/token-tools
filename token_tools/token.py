# The token consists of three parts: the start position, the length, and the type
# The start position is the line number (starting at 1)
# The length includes the start column
# The type is any one of the tokens in GENERIC_TOKENS
Token = tuple[tuple[int, int], int, str]

GENERIC_TOKENS: list[str] = [
    "Identifier",  # Variable
    "Error",
    "Keyword",
    "Type",
    "String",
    "Number",
    "Literal",
    "Operator",
    "Punctuation",
    "Comment",
]
