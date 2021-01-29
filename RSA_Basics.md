#Rivest-Shamir-Adleman (RSA) Cryptosystem
##Key Generation
*  Choose two distinct prime number $p$ and $q$.
* Compute $n$.

> $n$ = $p$$q$

> * $n$ is the `modulus` for both the **public** and **private** keys.
> * $n$ is released as part of the **public** key

* Compute $\lambda$($n$) where $\lambda$ is **Carmichael's Totient Function**.

> $n = pq$

> $\lambda$($n$) = $lcm$($\lambda$($p$),$\lambda$($q$))

> Since $p$ and $q$ are *prime*

>> $\lambda$($p$) = $\phi$($p$) = p - 1

>> $\lambda$($p$) = $\phi$($q$) = q - 1

> Hence,

>> $\lambda$($n$) = $lcm$($p$ - 1, $q$ - 1)
*  Choose and integer $e$ such that 1 < $e$ << $\lambda$($n$).

> - $e$ and $\lambda$($n$) are *coprime*

> - $e$ having a short bit-length and small *Hamming Weight* results in more efficient encryption

> - Most common, $e$ = $2^{16}$ + 1 = 65,537

> - Smallest and fastest value for $e$ is 3

> - $e$ is released as part of the **public** key

* Determin $d$ as $d$ $\equiv$ $e^{-1}(mod$ $\lambda(n))$

> Solve for $d$:

>> $de \equiv 1(mod$ $\lambda(n))$

> - $d$ can be computed efficiently by using the **Extended Euclidean Algorithm** since $e$ and $\lambda(n)$ are *coprime*.

> - This is a form of **Bezout's Identity**, where $d$ is one of the coefficients.

> - $d$ is kept secret as the **private key exponent**.

##Encryption
To encrypt a `plaintext` variable given $p, q,$ and $e$:

```
# Set given variables
pt = [plaintext vairable]
p  = [prime number]
q  = [prime number]
e  = [value 1 < e << lambda(n)]

# Caluclate modulus n
n  = p * q

# Encrypt plaintext variable
ct = pow(pt, e, n)

print(ct)
```

##Decryption
To decrypt a `ciphertext` given $p, q,$ and $e$:

```
from Crypto.Utils.number import inverse

# Set given variables
ct  = [ciphertext vairable]
p   = [prime number]
q   = [prime number]
e   = [value 1 < e << lambda(n)]

# Calculate totient phi
phi = (p - 1) * (q - 1)

# Calculate d
d   = inverse(e, phi)

# Decrypt ciphertext
pt  = pow(ct, d, n)

print(pt)
```