#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import random
import math

"""
Generate prime numbers with the Miller-Rabin Primality Test.
For example useful for RSA prime number generation.

Generating a 2048 Bit Prime takes 11 seconds on my laptop:

    $ time python generate_primes.py
    18687035979164759960466760296206931684048670365627731168581812017856988830965115380270770738787389085718116283127416689537626499398221423941864131345832239438016468120676003896789194409913408615320990238865137075670115908902303929614757662667625835901714318363069492532318855874659498625458479795852690370922508203783115512849318748971370018698508809310655527728638519173556845950918379394995191185954569447143685450657088230510827375976211180471624026433253567874110992844598001397299587423215893037362024063057346321319865682948169846512354337641419160496824946523484362125933347273900485920490790844892064041256141 is prime with bitlength=2048

    real	0m11.099s
    user	0m11.068s
    sys	0m0.020s
"""

def fermat_primality_test(p, s=5):
    """
    a^(p-1) ≡ 1 mod p
    Input: prime candidate p and security paramter s
    Output: either p is a composite (always trues), or
            p is a prime (with probability)
    """
    if p == 2:
        return True
    if not p & 1: # if p is even, number cant be a prime
        return False

    for i in range(s):
        a = random.randrange(2, p-2)
        x = pow(a, p-1, p) # a**(p-1) % p
        if x != 1:
            return False
    return True

def square_and_multiply(x, k, p=None):
    """
    Square and Multiply Algorithm
    Parameters: positive integer x and integer exponent k,
                optional modulus p
    Returns: x**k or x**k mod p when p is given
    """
    b = bin(k).lstrip('0b')
    r = 1
    for i in b:
        r = r**2
        if i == '1':
            r = r * x
        if p:
            r %= p
    return r

def miller_rabin_primality_test(p, s=5):
    if p == 2: # 2 is the only prime that is even
        return True
    if not (p & 1): # n is a even number and can't be prime
        return False

    p1 = p - 1
    u = 0
    r = p1  # p-1 = 2**u * r

    while r % 2 == 0:
        r >>= 1
        u += 1

    # at this stage p-1 = 2**u * r  holds
    assert p-1 == 2**u * r

    def witness(a):
        """
        Returns: True, if there is a witness that p is not prime.
                False, when p might be prime
        """
        z = square_and_multiply(a, r, p)
        if z == 1:
            return False

        for i in range(u):
            z = square_and_multiply(a, 2**i * r, p)
            if z == p1:
                return False
        return True

    for j in range(s):
        a = random.randrange(2, p-2)
        if witness(a):
            return False

    return True

def generate_primes(n=512, k=1):
    """
    Generates prime numbers with bitlength n.
    Stops after the generation of k prime numbers.

    Caution: The numbers tested for primality start at
    a random place, but the tests are drawn with the integers
    following from the random start.
    """
    assert k > 0
    assert n > 0 and n < 4096

    # follows from the prime number theorem
    necessary_steps = math.floor( math.log(2**n) / 2 )
    # get n random bits as our first number to test for primality
    x = random.getrandbits(n)

    primes = []

    while k>0:
        if miller_rabin_primality_test(x, s=7):
            primes.append(x)
            k = k-1
        x = x+1

    return primes

def main():
    n = 2048
    primes = generate_primes(n=n)
    for p in primes:
        print('{} is prime with bitlength={}'.format(p, n))

if __name__ == '__main__':
    main()
