#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import eea
import random

def RSA_keygen(n=512):
    """
    Perform steps 1. to 5. in the RSA Key Generation process.
    """
    # step 1
    import generate_primes
    p = generate_primes.generate_primes(n=n, k=1)[0]
    q = generate_primes.generate_primes(n=n, k=1)[0]
    # step 2
    n = p * q
    # step 3
    phi_n = (p - 1) * (q - 1)
    # step 4 and step 5
    while True:
        e = random.randrange(1, phi_n-1)
        if math.gcd(e, phi_n) == 1:
            # step 5
            gcd, s, t = eea.EEA(phi_n, e)
            if gcd == (s*phi_n + t*e):
                d = t % phi_n
                break
    return (e, n, d)

if __name__ == '__main__':
    print(RSA_keygen())
