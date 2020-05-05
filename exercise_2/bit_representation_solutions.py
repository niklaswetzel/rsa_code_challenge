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

    return reduce(lambda bits, char: (bits << char_bit_len) | ord(char), message, 0)


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

    bit_str = bin(n)[2:]  # remove prefix 0b
    zero_pad = (-len(bit_str)) % char_bit_len
    bit_str = zero_pad * '0' + bit_str
    bits_list = [bit_str[i:i+char_bit_len] for i in range(0, len(bit_str), char_bit_len)]

    return reduce(lambda mess, bits: mess + chr(int(bits, 2)), bits_list, '')
