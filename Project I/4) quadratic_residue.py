from binary_power import binary_power


def is_quadratic_residue(b, p):
    x = (p - 1) // 2
    y = binary_power(b, x, p)

    if y == 1:
        return True
    else:
        return False


if __name__ == "__main__":
    b = int(input("b = "))
    p = int(input("p = "))
    print(is_quadratic_residue(b, p))