from .token import Token


# If we are going to have a only_tokens_in_text_range function then we have to have a normal_text_range function
def normal_text_range(
    full_text: str, text_range: tuple[int, int] = (1, -1)
) -> tuple[list[str], tuple[int, int]]:
    """Takes the full text and a text range (inclusively numbered) and returns the split text and a tuple with the proper text range."""
    # Text range is the first and last line inclusively with -1 for the end line indicating that it goes until the last line
    split_text: list[str] = full_text.splitlines()

    if text_range[1] == -1:
        # This indicates that the text range should span the length of the entire code
        split_len: int = len(split_text)
        split_len = (
            1 if split_len == 0 else split_len
        )  # If its a one line code snippet, we need to +1
        text_range = (text_range[0], split_len)

    # We want only the lines in the text range because this list is iterated
    split_text = (
        split_text[text_range[0] - 1 : text_range[1]] if split_text else [""]
    )

    return (split_text, text_range)


def only_tokens_in_text_range(
    tokens: list[Token], text_range: tuple[int, int]
) -> list[Token]:
    """Given a list of Token's and proper text range (see normal_text_range), it returns a new list of all Token's in the range (inclusively)."""
    # We create a new list because lists are pass by reference
    output_tokens: list[Token] = []

    for token in tokens:
        token_lineno: int = token[0][0]
        minimum_line: int = text_range[0]
        maximum_line: int = text_range[1]

        if token_lineno < minimum_line or token_lineno > maximum_line:
            continue

        output_tokens.append(token)

    output_tokens = merge_tokens(output_tokens)
    return output_tokens


def merge_tokens(tokens: list[Token]) -> list[Token]:
    """Given a list of Token's, it will merge any Token's next to each other of the same type."""
    output_tokens: list[Token] = []
    depth: int = 0
    for token in tokens:
        # Deal with basic edge case
        if depth == 0:
            output_tokens.append(token)
            depth += 1
            continue

        previous_token = output_tokens[-1]

        # Get our boolean checks
        same_token_type: bool = previous_token[2] == token[2]
        same_line: bool = previous_token[0][0] == token[0][0]
        neighboring_tokens: bool = (
            previous_token[0][1] + previous_token[1] == token[0][1]
        )

        # Determine if tokens should be merged
        if not (same_token_type and same_line and neighboring_tokens):
            output_tokens.append(token)
            depth += 1
            continue

        # Replace previous token with new token (we don't increase depth because we are substituting, not adding)
        new_token: Token = (
            (token[0][0], previous_token[0][1]),
            previous_token[1] + token[1],
            token[2],
        )
        output_tokens[-1] = new_token

    return output_tokens


def overwrite_tokens(
    old_tokens: list[Token], new_tokens: list[Token]
) -> list[Token]:
    """Given a list of old Token's and new Token's, the old Token's inside new Token's will be removed and any partial overlaps rectified"""
    # If there are no new tokens, return the old tokens as they are
    if not new_tokens:
        return old_tokens

    # List to hold the final set of tokens
    output_tokens: list[Token] = []
    # List to track tokens that should not be added again
    dont_add_tokens: list[Token] = []

    # Iterate over each new token
    for new_token in new_tokens:
        # Extract the new token's properties
        new_start: tuple[int, int] = new_token[0]
        new_line: int = new_start[0]
        new_start_col: int = new_start[1]
        new_length: int = new_token[1]
        new_end_col: int = new_start_col + new_length

        # Iterate over each old token
        for old_token in old_tokens:
            # Extract the old token's properties
            old_start: tuple[int, int] = old_token[0]
            old_line: int = old_start[0]
            old_start_col: int = old_start[1]
            old_length: int = old_token[1]
            old_end_col: int = old_start_col + old_length
            old_type: str = old_token[2]

            # If the old and new tokens are the same, skip processing
            if old_token == new_token:
                continue

            # If tokens are on different lines, add the old token to output if it's not already added
            if old_line != new_line:
                if old_token not in dont_add_tokens:
                    output_tokens.append(old_token)
                continue

            # Check for no overlap (old token is entirely before or after the new token)
            if old_end_col <= new_start_col or old_start_col >= new_end_col:
                if old_token not in dont_add_tokens:
                    output_tokens.append(old_token)
                continue

            # Since there's overlap, mark the old token to avoid re-adding it
            dont_add_tokens.append(old_token)

            # Remove any instances of the old token
            while old_token in output_tokens:
                output_tokens.remove(old_token)

            # Handle partial overlap where the old token starts before the new token
            if old_start_col < new_start_col:
                left_token: Token = (
                    (old_line, old_start_col),
                    new_start_col - old_start_col,
                    old_type,
                )
                output_tokens.append(left_token)

            # Handle partial overlap where the old token ends after the new token
            if old_end_col > new_end_col:
                right_token: Token = (
                    (old_line, new_end_col),
                    old_end_col - new_end_col,
                    old_type,
                )
                output_tokens.append(right_token)

        # Add the new token to the output list
        output_tokens.append(new_token)

    # Sort the output tokens to ensure they are in the correct order
    output_tokens = sorted(set(output_tokens))
    return output_tokens


def overwrite_and_merge_tokens(
    old_tokens: list[Token], new_tokens: list[Token]
) -> list[Token]:
    """Given a list of old Token's and new Token's, it will merge both lists, overwrite old overlapping Token's and then merge the final result"""
    merged_old_tokens: list[Token] = sorted(set(merge_tokens(old_tokens)))
    merged_new_tokens: list[Token] = sorted(set(merge_tokens(new_tokens)))
    output_tokens: list[Token] = overwrite_tokens(
        merged_old_tokens, merged_new_tokens
    )

    output_tokens = merge_tokens(output_tokens)
    return output_tokens
