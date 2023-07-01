# GENERATING RANDOM PRIMES
import random
from math import gcd

def square_and_multiply(x, k, p=None):
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
    if p == 2:
        return True
    if not (p & 1):
        return False

    p1 = p - 1
    u = 0
    r = p1

    while r % 2 == 0:
        r >>= 1
        u += 1

    assert p-1 == 2**u * r

    def witness(a):
        z = square_and_multiply(a, r, p)
        if z == 1:
            return False

        for i in range(u):
            z = square_and_multiply(a, 2**i * r, p)
            if z == p1:
                return False
        return True

    for _ in range(s):
        a = random.randrange(2, p-2)
        if witness(a):
            return False

    return True

def generate_primes(n, k):
    x = random.getrandbits(n)
    primes = []
    while k>0:
        if miller_rabin_primality_test(x, s=7) and gcd(x, 65537) == 1:
            primes.append(x)
            k = k - 1
        x = x + 1
    return primes

def main():
    for size in [128, 256, 512, 1024, 1536, 2048]:
        print(f'{size} start')
        file = open(f'p_{size}.txt', 'w')
        primes = generate_primes(size, 2000)
        for p in primes:
            print(p, file=file)
        file.close()
        print(f'{size} ended')

if __name__ == '__main__':
    main()