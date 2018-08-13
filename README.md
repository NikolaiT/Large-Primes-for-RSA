# Finding large Prime Number for RSA Key Generation

Source code for the blog post on [large prime numbers for RSA](http://incolumitas.com/2018/08/12/finding-large-prime-numbers-and-rsa/#finding-large-prime-numbers-and-rsa)

The approach in this code is to generate large primes by randomly selecting large integers and then testing them for primality with the Miller-Rabin Primality Test. Due to the prime number theorem, primes must occur with probability roughly `P(n is prime) = 2/ln(n)`. Generated primes are used for RSA encryption/decryption as a sample application.
