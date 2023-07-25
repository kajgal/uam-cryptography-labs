from itertools import product

def hex_to_bin(num_hex):
    return bin(int(num_hex, 16))[2:].zfill(8)


def bin_to_hex(num_bin):
    if num_bin is None:
        return 'Undefined'

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


def vec_multiply(V, W):
    res = hex_to_bin('00')
    for i in range(len(V)):
        multiply_res = multiply(V[i], W[i])
        res = sum(res, multiply_res)

    res_hex = bin_to_hex(res)

    return res_hex


def solve(W, res_hex):
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    all_hex_numbers = [''.join(i) for i in product(hex_digits, repeat=2)]

    for i in all_hex_numbers:
        for j in all_hex_numbers:
            for k in all_hex_numbers:
                V = [hex_to_bin(i), hex_to_bin(j), hex_to_bin(k)]
                temp_res = vec_multiply(V, W)
                if temp_res == res_hex:
                    print([i, j, k])
                    #return [i, j, k]

    return ['00', '00', '00']


if __name__ == '__main__':

    # W
    b1 = "aa"
    b2 = "17"
    b3 = "ce"

    W = [hex_to_bin(b1), hex_to_bin(b2), hex_to_bin(b3)]
    res_hex = 'cc'

    V = solve(W, res_hex)

    print("V = " + str(V))





