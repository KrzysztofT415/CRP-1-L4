# N = pq
# d = e^(-1) mod φ(N) (gdzie e = 65537)
# dp = d mod (p-1)
# dq = d mod (q-1)
# qi = q^(-1) mod p

import timeit
import random
from math import gcd
from sympy.ntheory.factor_ import totient
import matplotlib.pyplot as plt

def RSA(x, n, e):
    return pow(x, e, n)

def RSA_CRT(x, p, q, dp, dq, qi):
    yp = pow(x, dp, p)
    yq = pow(x, dq, q)
    h = (qi * (yp - yq)) % p
    if (h < 0):
        h += p
    return yq + h * q

def main():
    results_crt = []
    results_no = []
    sizes = [128, 256, 512, 3072, 4096]
    for size in sizes:
        print(f'{size} start')
        primes = []
        file = open(f'p_{size}.txt', 'r')
        for line in file.readlines():
            primes.append(int(line))

        p_arr = random.choices(primes, k=1000)
        q_arr = random.choices(primes, k=1000)
        print(f'{size} read')

        avg = 0
        avg2 = 0
        skips = 0
        for i in range(1000):
            p = p_arr[i]
            q = q_arr[i]
            if (q == p):
                print('equality skip')
                skips += 1
                continue
            N = p * q
            d = pow(65537, -1, totient(N))
            dp = d % (p - 1)
            dq = d % (q - 1)
            qi = pow(q, -1, p)
            inp = random.randint(2, N - 1)

            start = timeit.default_timer()
            RSA_CRT(inp, p, q, dp, dq, qi)
            stop = timeit.default_timer()
            avg += stop - start

            start = timeit.default_timer()
            RSA(inp, p, d)
            stop = timeit.default_timer()
            avg2 += stop - start

        results_crt.append(avg / (1000 - skips))
        results_no.append(avg2 / (1000 - skips))
        print(f'{size} ended')

    plt.plot(sizes, results_no, 'b', sizes, results_crt, 'r')
    plt.ylabel('average time: no crt - blue, with crt - red')
    plt.xlabel('bit length of primes')
    plt.savefig('fig')

if __name__ == '__main__':
    main()