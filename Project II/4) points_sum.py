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


def extended_euclidean_algorithm(a, b):
    mod = b
    x = 1
    z = 0
    u = 0
    v = 1
    while 0 < b:
        q = (a//b)

        a, b, x, z, u, v = b, (a%b), u, v, (x-u*q), (z-v*q)


    if x < 0:
        x = x + mod
    return x


# P + Q = R
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


p = 2 ** 297 - 285
A = 12444294553580413309261690068074902197491116730730148566639545894744246709929621325173395
B = 84392518890582039404267377489450873639534503950959442291224326041747596054960509300406339
x1 = 62879858904779613999710318830676706809314870827467974421140720563100203290425093563934657
y1 = 149817366140562266110553419586998052533831523439414441562530978574083437163330386770868728
x2 = 175206595850734074515052840468994826498800594359854142955665029870917612984058638317963939
y2 = 59934386267125367704024703269545993709732203383419447223761888563165595460613196860483119

P = [x1, y1]
Q = [x2, y2]

print("(x, y) = " + str(points_sum(p, A, P, Q)))
