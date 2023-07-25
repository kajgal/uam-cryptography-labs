import random


def delta(A, B, p):
    return (4 * effective_powering(A, 3, p) + 27 * effective_powering(B, 2, p)) % p


def random_eliptic_curve(p):
    while True:
        A = random.randint(0, p - 1)
        B = random.randint(0, p - 1)

        if delta(A, B, p) != 0:
            return A, B


def effective_powering(b, k, n):
    k_bin = bin(k)[2:]  # 0x...
    m = len(k_bin)
    r = 1
    x = b % n

    for i in range(m - 1, -1, -1):
        if k_bin[i] == '1':
            r = r * x % n

        x **= 2
        x %= n

    return r


p = 254629497041810760783555711051172270131433549208242031329517556169297662470417088272924387

A, B = random_eliptic_curve(p)

print("A = " + str(A))
print("B = " + str(B))
print("Y^2 = X^3 + " + str(A) + "X" + " + " + str(B))