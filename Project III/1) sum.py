def hex_to_bin(num_hex):
    return bin(int(num_hex, 16))[2:].zfill(8)


def bin_to_hex(num_bin):
    return hex(int(num_bin, 2))[2:].zfill(2)


def sum(a, b):
    return ''.join([str((int(a[bit]) ^ int(b[bit]))) for bit in range(8)])


if __name__ == '__main__':
    a_hex = "e1"
    b_hex = "03"

    a_bin = hex_to_bin(a_hex)
    b_bin = hex_to_bin(b_hex)

    result_bin = sum(a_bin, b_bin)
    result_hex = bin_to_hex(result_bin)

    print(result_hex)
