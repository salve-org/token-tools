=========
Functions
=========

.. _normal_text_range Overview:

``normal_text_range(full_text: str, text_range: tuple[int, int] = (1, -1)) -> tuple[list[str], tuple[int, int]]``
*****************************************************************************************************************

Takes the full text and a text range (inclusively numbered) and returns the split text and a tuple with the proper text range.

.. _only_tokens_in_text_range Overview:

``only_tokens_in_text_range(tokens: list[Token], text_range: tuple[int, int]) -> list[Token]``
**********************************************************************************************

Given a list of ``Token``'s and proper text range (see above), it returns a new list of all Token's in the range (inclusively).

.. _merge_tokens Overview:

``merge_tokens(tokens: list[Token]) -> list[Token]``
****************************************************

Given a list of ``Token``'s, it will merge any Token's next to each other of the same type.

.. _overwrite_tokens Overview:

``overwrite_tokens(old_tokens: list[Token], new_tokens: list[Token]) -> list[Token]``
*************************************************************************************

Given a list of old ``Token``'s and new ``Token``'s, the old ``Token``'s inside new ``Token``'s will be removed and any partial overlaps rectified.

.. _overwrite_and_merge_tokens Overview:

``overwrite_and_merge_tokens(old_tokens: list[Token], new_tokens: list[Token]) -> list[Token]``
***********************************************************************************************

Given a list of old ``Token``'s and new ``Token``'s, it will merge both lists, overwrite old overlapping ``Token``'s and then merge the final result.
