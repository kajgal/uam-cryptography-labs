import random


# generate random number with n-bits
def n_bit_random(n):
    return (random.randrange(2 ** (n - 1) + 1, 2 ** n - 1))


def is_first_fermat(n, k):
    i = 0
    while i < k:
        a = random.randint(1, n - 1)
        if effective_powering(a, (n-1), n) == 1:
            i = i + 1
        else:
            return False
    return True


def get_generator(n_bits):

    # find prime number q
    q_candidate = -1
    while True:
        q_candidate = n_bit_random(n_bits)

        if is_first_fermat(q_candidate, 24):
            print(q_candidate)
            break

    # calculate p = 2q + 1
    q = q_candidate
    p = 2 * q + 1

    while True:
        g_candidate = random.randint(2, p - 1)
        g_squared = effective_powering(g_candidate, 2, p)
        g_to_power_q = effective_powering(g_candidate, q, p)

        if g_squared % p != 1 and g_to_power_q % p != 1:
            print(g_candidate)
            break

    g = g_candidate

    return q, g



# used in decryption for finding inversion of A
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


# calculating y = g^x mod p
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


# generates a pair of keys where y = g^x mod p
def keys_generator():
    p, g = get_generator(1024)
    x = random.randint(1, p)  # 72
    y = effective_powering(g, x, p)

    return ([p, g, y], [p, g, x])  # public key, private key


# a = g^k mod p | b = m * y^k mod p
def encrypt(public_key, message):
    p = public_key[0]
    g = public_key[1]
    y = public_key[2]

    # random value k
    k = random.randint(1, p)

    # a = g^k mod p
    a = effective_powering(g, k, p)

    # b = M * y^k mod p
    b = (message * effective_powering(y, k, p)) % p

    # encryption result
    return [a, b]


# m(plaintext) = (b/(a^x)) mod p
def decrypt(cipher, private_key):
    a = cipher[0]
    b = cipher[1]

    p = private_key[0]
    x = private_key[2]

    inv_a = extended_euclidean_algorithm(a, p)
    y = effective_powering(inv_a, x, p)
    return int(y * b % p)


if __name__ == '__main__':
    message = 123
    public_key, private_key = keys_generator()
    encrypted_message = encrypt(public_key, message)
    decrypted_cipher = decrypt(encrypted_message, private_key)
    print("Public key: " + str(public_key))
    print("Private key: " + str(private_key))
    print("Encrypted: " + 'a = ' + str(encrypted_message[0]) + " " + 'b = ' + str(encrypted_message[1]))
    print("Decrypted: " + str(decrypted_cipher))
    success = (message == decrypted_cipher)
    print("Success: " + str(success))