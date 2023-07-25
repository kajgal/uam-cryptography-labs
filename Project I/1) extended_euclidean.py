

def extended_euclidean(b, n):

    modulo = n
    A = n
    B = b
    U = 0
    V = 1

    while B != 0:
        q = A // B

        A, B, U, V = B, A - q * B, V, U - q * V

    d = A
    u = U
    v = (d - b * u) // n

    if u < 0:
        u = u + modulo

    return u


if __name__ == "__main__":
    b = float(input("b = "))
    n = float(input("n = "))
    print(extended_euclidean(b, n))