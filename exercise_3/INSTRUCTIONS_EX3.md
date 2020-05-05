
# Description
Before you implement the RSA cryptosystem, you want implement some helper functions. 

The function `extended_euclidean` implements the 
[extended euclidean algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm).
It has the arguments `a` and `b` and solves the equation `gcd(a,b) = s*a + t*b`,
where gcd is the [greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor).

The function `create_private_key` has the arguments `prime_0, prime_1` and  `public_key`.
It returns the `private_key`, which solves the equation
```
m = ((m**public_key)**private_key) % N
```
for `N = prime_0*prime_1` and all `0 <= m < N`. 

The algorithm is described [here](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Key_generation).
# Example
```
In:
solution = extended_euclidean(456,232)
solution

Out:
(8, -1, 2)

In:
private_key = create_private_key(5, 11, 3)
private_key

Out:
7
```
# Explanation
`(8, -1, 2)` is a valid solution since `gcd(456,232) = 8` and `8 = -456 + 2*232`.

`7` is a private key since `m = m**21 % 55` for all `0 <= m < 55`. 