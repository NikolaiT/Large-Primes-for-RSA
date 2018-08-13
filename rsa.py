#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import rsa_keygen
from generate_primes import square_and_multiply

def RSA_encrypt(x, publicKey):
    e, n = publicKey
    assert x < n

    y = square_and_multiply(x, e, n)
    return y

def RSA_decrypt(y, privateKey):
    d, n = privateKey
    assert y < n

    x = square_and_multiply(y, d, n)
    return x

def test():
    bitlength = 512

    e, n, d = rsa_keygen.RSA_keygen(n=bitlength)

    print('Public Key (e, n) = {}'.format((e,n)))
    print('Private Key (d) = {}'.format(d))

    # generate a random message
    x = random.getrandbits(bitlength)
    print('Plaintext x={}'.format(x))

    # test RSA cryptosystem
    y = RSA_encrypt(x, (e, n))
    print('Ciphertext y={}'.format(y))

    # test that decrypting the ciphertext yields the plaintext
    assert RSA_decrypt( y, (d, n)) == x

if __name__ == '__main__':
    test()
