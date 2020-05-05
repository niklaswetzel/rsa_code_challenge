
# Description
Now you combine everything in the `cipher` class.
The class constructor has the arguments `char_bit_len, prime_0, prime_1` and `public_key`,
which are 
 * the number of bits used to represent a single character,
 * two prime numbers used for the RSA cryptosystem,
 * a valid public key integer.

The `cipher` class has two attributes:
 * `char_bit_len`, the number of bits used to represent a single character,
 * `rsa`, an instance of the RSA class (Exercise 4), initialized with `prime_0, prime_1` and `public_key`.
 
The `cipher` class has two methods:
1. The `encrypt` method has the string argument `plaintext`:
    1. The `plaintext` is divided into a list of messages via the `split_to_messages` function (Exercise 1).
    1. Each message is translated to an integer via the `to_int` function (Exercise 2).
    1. Each integer is encrypted via the `encrpyt` method of the `RSA` class (Exercise 4).
    1. The `cipher_list` containing all encrypted integers is returned

1. The `decrypt` method has the list argument `cipher_list`:
    1. The `cipher_list` contains encrypted integers. To decrypt
     the `ciper_list` apply the  `decrpyt` method of the `RSA` class (Exercise 4) to each integer of the list.
    1. Then convert each decrypted integer to a string message, using the `to_message` function (Exercise 2).
    1. Reconstruct the plaintext by applying `join_to_plaintext` function (Exercise 1) to the list of strings.
    1. Return the reconstructed plaintext

If done correctly, the `plaintext` is equal to decrypting the encrypted `plaintext`, 

# Example
```
In:
c = Cipher(
            char_bit_len=7,
            prime_0=61,
            prime_1=53,
            public_key=17,
        )
plaintext = "Hello World"
ciphertext = c.encrypt(plaintext)
ciphertext

Out:
[3000, 1313, 745, 745, 2185, 1992, 604, 2185, 2412, 745, 1773]

In:
c = Cipher(
            char_bit_len=7,
            prime_0=61,
            prime_1=53,
            public_key=17,
        )
ciphertext = [3000, 1313, 745, 745, 2185, 1992, 604, 2185, 2412, 745, 1773]
plaintext = c.decrypt(ciphertext)
plaintext

Out:
"Hello World"
```
