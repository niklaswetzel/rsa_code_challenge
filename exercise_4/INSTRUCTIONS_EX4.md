
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
rsa = RSA(61, 53, 17)
print(rsa.alphabet_length, rsa.public_key, rsa.private_key)

Out:
(3233, 17, 413)

In:
rsa = RSA(61, 53, 17)
cipher = rsa.encrypt(65)
cipher

Out:
2790

In:
rsa = RSA(61, 53, 17)
plain = rsa.decrypt(2790)
plain

Out:
65
```

# Explanation
`2790 = 65**17 % 3233` and `65 = 2790**413 % 3233`.
