
# Description
Finally, you implement a cyrptosystem in form of the `RSA` class.
The class constructor has the arguments `prime_0, prime_1` and `public_key`,
which are two prime numbers and a valid public key.
It initialises the attributes `alphabet_len, public_key, private_key`,
which are respectively the *alphabet length*, the *public key* and the *private key*
of the [RSA algorithm](https://en.wikipedia.org/wiki/RSA_(cryptosystem\)).

The class has the methods `encrypt` and `decrypt`, which implement the RSA
[en-](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Encryption) and
[decryption](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Encryption).



# Example
```
In:
rsa = RSA(4,14)
multiple

Out:
28

In:
divisor = gcd(456,232)
divisor

Out:
8

In:
solution = extended_euclidean(456,232)
solution

Out:
(8, -1, 2)
```

# Explanation
`gcd(456,232) = 8` and `8 = -456 + 2*232`.
