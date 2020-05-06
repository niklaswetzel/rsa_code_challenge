
# Description
You want to ask your friend whats going on, but you remember that he only responds to encrypted messages.
The text that you want to secretly transmit is written in the string variable `plaintext`.
You agreed to divide the `plaintext` into a `message_list` containing message strings of equal character length,
which will be encrypted separately.
To make sure that the last message has the same length as the others, it is padded with `' '` at the end.

You agreed to use the alphabet `0, ..., alphabet_len -1`for encryption,
therefore you have to make sure that each message can be represented by such a number.  

The number of bits available to represent a single character is given by `char_bit_len`.
The length of each message is the maximal number of characters such that the concatenation of their bit representations 
is guaranteed to be an integer (base-2 representation) of the alphabet.

The function `split_to_messages` converts a plaintext to a list of messages,
the function `join_to_plaintext` converts a list of messages back to the plaintext,
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

