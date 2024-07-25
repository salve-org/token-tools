from beartype.claw import beartype_this_package

beartype_this_package()

from .token import GENERIC_TOKENS, Token  # noqa: F401, E402
from .token_funcs import (  # noqa: F401, E402
    merge_tokens,
    normal_text_range,
    only_tokens_in_text_range,
    overwrite_and_merge_tokens,
    overwrite_tokens,
)
