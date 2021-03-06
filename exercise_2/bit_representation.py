from functools import reduce


def to_int(message, char_bit_len=7):
    """
    Converts message to int by concatenating the bit representation of each character.
    :param message: str
    :param char_bit_len: int
        Bit length of a single character.
        Defaults to 7
    :return: int
    """
    ...


def to_message(n, char_bit_len=7):
    """
    Inverts to_int function. Each `char_bit_length` bits of `n` are converted to a string character.
    Returns the string of concatenated characters.
    :param n: int
    :param char_bit_len:
        Bits used for a single character
        Defaults to 7
    :return: str
        Concatenated characters
    """

    ...
