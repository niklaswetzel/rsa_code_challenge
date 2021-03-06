
def split_to_messages(plaintext, alphabet_len, char_bit_len=7):

    """
    Divides plaintext into substrings of constant length, such that each substring can be represented by an alphabet of
    length alphabet_len. Last block is padded with ' '.

    :param plaintext: str
        The text that has to be split. Has no ' ' characters at the end.
    :param alphabet_len: int
        Alphabet number of symbols in the alphabet
    :param char_bit_len: int
        Bit length of a single character.
        Defaults to 7.
    :return: list
        List of stings with constant character length.
    """
    ...


def join_to_plaintext(message_list):
    """
    :param message_list:
        List of substrings
    :return: str
        A single string consisting of all joined substrings. ' ' at the end are deleted.
    """

    ...
