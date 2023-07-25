def to_binary_string(n):
    return "{0:b}".format(n)


def binary_power(x, k, n):
    y = 1
    k_bin_string_reversed = to_binary_string(k)[::-1]

    i = len(k_bin_string_reversed) - 1
    while i >= 0:
        if k_bin_string_reversed[i] == "1":
            y = (y * x) % n
        y = (y * y) % n
        i = i - 1

    return y


if __name__ == "__main__":
    b = int(input("b = "))
    k = int(input("k = "))
    n = int(input("n = "))
    print(binary_power(b, k, n))
