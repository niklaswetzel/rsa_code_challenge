
# Description
The text that you want to secretly transmit to your friend is written in the string variable `plaintext`.
You agreed to divide the `plaintext` into string messages of equal character length, which will be encrypted separately.
To make sure that the last message has the same length as the others, it is padded with `' '` at the end.

You agreed to use the alphabet of the integers `0, ..., alphabet_len -1` 
The number of bits available to represent a single character is given by `char_bit_len`.

The length of each message is the maximal number of characters such that the concatenation of their bit representations 
is guaranteed to be an integer (2-based representation) of the alphabet.

The function `split_to_messages` converts a plaintext to a list of messages, the function `join_to_plaintext` converts a list of messages back to the plaintext,
erasing all `' '` at the end of the reconstructed plaintext.


# Example
```
In:
message_list = split_to_messages('abcxy', 2 ** 12, char_bit_len=6)
message_list

Out:
['ab', 'cx', 'y ']

In:
plaintext = join_to_plaintext(['ab', 'cx', 'y '])
plaintext

Out:
'abcxy'
```

