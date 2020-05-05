
# Description
You want to use an integers alphabet.
Therefore you need to convert strings to integers.
Each character of a message is mapped to its corresponding ascii value, 
then padded with `0` values at the beginning to have each character correspond to `char_bit_len` bits.
These values are then concatenated and interpreted as base-2 integer.

The function `to_int` has the arguments `message` (str) and `char_bit_len` (int) and returns the corresponding integer.
The function `to_message` has the arguments `n` (int) and `char_bit_len` (int) and returns the corresponding string.

# Example
```
In:
int_rep = to_int('az',8)
int_rep

Out:
24954

In:
message = to_message(24954,8)
message

Out:
'az'
```
# Explanation
The bit representation of `'a'` is `1100001` and `'z'` is `1111010`.
The bit representation have length 7, therefore they are padded with a single `0` at the beginning.
The bit representation of `'az'` is therefore `0110000101111010`, which corresponds to the integer `24954`.
