import random


def square_root(b, p):
    k = (p - 3) // 4
    z = p - 1 - k

    return int(effective_powering(b, z, p))


def is_quadratic_rest(b, p):
    c = (p - 1) // 2

    if effective_powering(b, c, p) == 1:
        return True

    return False


def effective_powering(b, k, n):
    k_bin = bin(k)[2:]  # 0x...
    m = len(k_bin)
    r = 1
    x = b % n

    for i in range(m - 1, -1, -1):
        if k_bin[i] == '1':
            r = r * x % n

        x = (x * x) % n

    return r


def random_point(A, B, p):
    while True:
        x = random.randint(0, p - 1)
        z = effective_powering(x, 3, p) + (A * x) + B

        if is_quadratic_rest(z, p):
            break

    y = square_root(z, p)
    return x, y


p = 19
A = 1
B = 0

print("(x, y) = " + str(random_point(A, B, p)))
