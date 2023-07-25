from binary_power import binary_power


def quadratic_sqrt(p, b):
    x = (p + 1) // 4
    return binary_power(b, x, p)


if __name__ == "__main__":
    p = int(input("p = "))
    b = int(input("b = "))
    print(quadratic_sqrt(p, b))