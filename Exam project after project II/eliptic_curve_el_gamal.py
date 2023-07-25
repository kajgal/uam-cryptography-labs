import random
import sys

sys.setrecursionlimit(10000)


# generate random number with n-bits
def n_bit_random(n):
    return random.randrange(2 ** (n - 1) + 1, 2 ** n - 1)


def effective_powering(b, k, p):
    k_bin = bin(k)[2:]  # 0x...
    m = len(k_bin)
    r = 1
    x = b % p

    for i in range(m - 1, -1, -1):
        if k_bin[i] == '1':
            r = r * x % p

        x **= 2
        x %= p
    return r


def is_first_fermat(n, k):
    i = 0

    while i < k:
        a = random.randint(1, n - 1)
        if effective_powering(a, (n - 1), n) == 1:
            i = i + 1
        else:
            return False

    return True


def generate_p(n):
    p = -1

    while True:
        x = n_bit_random(n)
        p_candidate = 4 * x + 3
        if is_first_fermat(p_candidate, 24):
            return p_candidate


def delta(A, B, p):
    return (4 * effective_powering(A, 3, p) + 27 * effective_powering(B, 2, p)) % p


def random_eliptic_curve(p):
    while True:
        A = random.randint(0, p - 1)
        B = random.randint(0, p - 1)

        if delta(A, B, p) != 0:
            return A, B


def square_root(b, p):
    k = (p - 3) // 4
    z = p - 1 - k

    return int(effective_powering(b, z, p))


def is_quadratic_rest(b, p):
    c = (p - 1) // 2

    if effective_powering(b, c, p) == 1:
        return True

    return False


def random_point(A, B, p):
    while True:
        x = random.randint(0, p - 1)
        z = effective_powering(x, 3, p) + (A * x) + B

        if is_quadratic_rest(z, p):
            break

    y = square_root(z, p)
    return x, y


def extended_euclidean_algorithm(a, b):
    mod = b
    x = 1
    z = 0
    u = 0
    v = 1
    while 0 < b:
        q = (a // b)

        a, b, x, z, u, v = b, (a % b), u, v, (x - u * q), (z - v * q)

    if x < 0:
        x = x + mod
    return x


def points_sum(p, A, P, Q):
    if P[0] == "infinity" or P[1] == "infinity":
        return Q

    if Q[0] == "infinity" or Q[1] == "infinity":
        return P

    if P[0] == Q[0] and P[1] == (-Q[1] + p):
        return ["infinity", "infinity"]

    if P[0] == Q[0] and P[1] == Q[1] == 0:
        return ["infinity", "infinity"]

    if P[0] == Q[0] and P[1] == Q[1]:
        lam = ((3 * effective_powering(P[0], 2, p) + A) * extended_euclidean_algorithm((2 * P[1] % p), p)) % p
        x3 = (effective_powering(lam, 2, p) - P[0] - Q[0]) % p
        y3 = (lam * (P[0] - x3) - P[1]) % p

        return [x3, y3]

    if P[0] != Q[0]:
        lam = ((Q[1] - P[1]) * extended_euclidean_algorithm(((Q[0] - P[0]) % p), p)) % p
        x3 = (effective_powering(lam, 2, p) - P[0] - Q[0]) % p
        y3 = (lam * (P[0] - x3) - P[1]) % p

        return x3, y3


def point_multiplication(p, A, P, n):
    if n == 0:
        return 0

    if n == 1:
        return P

    if n % 2 == 1:
        return points_sum(p, A, P, point_multiplication(p, A, P, n - 1))

    if n % 2 == 0:
        return point_multiplication(p, A, points_sum(p, A, P, P), n // 2)


def print_encryption_info():
    print("Encryption for p of " + str(p_bits) + " bits")
    print("p = " + str(p))

    print("A = " + str(A))
    print("B = " + str(B))

    print("Q = " + str(Q))

    print("xA = " + str(x_alice))
    print("xB = " + str(x_bob))

    print("QB = " + str(Q_bob))
    print("QA = " + str(Q_alice))

    print("SA = " + str(S_alice))
    print("SB = " + str(S_bob))

    print("Result = " + str(S_alice == S_bob))


if __name__ == '__main__':
    # set number of bits for p number
    p_bits = 1000

    # generate prime p number that fits p === 3 % 4 rule
    p = generate_p(p_bits)

    # generate elliptic curve for given p
    A, B = random_eliptic_curve(p)

    # generate random point on this curve
    Q = random_point(A, B, p)

    # generate random xA for alice and multiply point Q xA times
    x_alice = random.randint(0, p // 2)
    Q_alice = point_multiplication(p, A, Q, x_alice)

    # generate random xB for bob and multiply point Q xB times
    x_bob = random.randint(0, p // 2)
    Q_bob = point_multiplication(p, A, Q, x_bob)

    # calculate points by multiplication of exchanged points
    S_alice = point_multiplication(p, A, Q_bob, x_alice)
    S_bob = point_multiplication(p, A, Q_alice, x_bob)

    # points should be the same
    print_encryption_info()
