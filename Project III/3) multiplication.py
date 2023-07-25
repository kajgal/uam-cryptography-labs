def hex_to_bin(num_hex):
    return bin(int(num_hex, 16))[2:].zfill(8)


def bin_to_hex(num_bin):
    return hex(int(num_bin, 2))[2:].zfill(2)


def sum(a, b):
    return ''.join([str((int(a[bit]) ^ int(b[bit]))) for bit in range(8)])


def left_shift(num_bin):
    return num_bin[1:8] + "0"


def xtime(num_bin):

    if num_bin[0] == '0':
        return left_shift(num_bin)

    return sum(left_shift(num_bin), "00011011")


def right_shift(num_bin):
    return "0" + num_bin[0:7]


def multiply(a, b):

    if b == '00000000':
        return '00000000'

    if b == '00000001':
        return a

    if b[7] == '0':
        return multiply(xtime(a), right_shift(b))

    return sum(multiply(xtime(a), right_shift(b)), a)


if __name__ == '__main__':
    a_hex = "e1"
    a_bin = hex_to_bin(a_hex)

    b_hex = "03"
    b_bin = hex_to_bin(b_hex)

    result_bin = multiply(a_bin, b_bin)
    result_hex = bin_to_hex(result_bin)

    print(result_hex)
