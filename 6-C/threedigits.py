import sys


def nu(n, p):
    '''
    p-adic valuation of n!, i.e., the exponent of the largest power of p which
    divides n. By Legendre's formula, this is equal to (n - s_p(n))/(p-1), where
    s_p(n) is the sum of digits in the p-adic expression of n.
    '''

    i = 0
    nn = n
    while nn > 0:
        nn, r = divmod(nn, p)
        i += r

    return (n - i) // (p - 1)


# precompute large values to save some time
# precomputed[i] == three_digits_omit25((i+1) * 1000000)
precomputed = [1, 33, 157, 791, 389, 441, 831, 247, 233, 447, 189, ]


def three_digits_omit25(n):

    q, r = divmod(n, 1000000)
    lo = q * 1000000 + 1
    result = precomputed[q]
    limit = n - (n % 1000)

    for i in range(lo, n+1):
        if (i % 2) and (i % 5) and i < limit:
            # those factors cancel with their inverse mod 1000
            continue

        while i % 2 == 0:
            i = i // 2
        while i % 5 == 0:
            i = i // 5
        result = (result * (i % 1000)) % 1000

    return result


def three_digits(n):

    result = three_digits_omit25(n)

    # take care of the 2-power which does not "go into" trailing zeros
    d1, d2 = divmod(nu(n, 2) - nu(n, 5), 10)
    for i in range(d1):
        result = (result * 24) % 1000
    for i in range(d2):
        result = (result * 2) % 1000

    return result


for l in sys.stdin.readlines():
    n = int(l)
    # handle small cases separately because no padding with zeros
    if n <= 6:
        print(three_digits(n))
    else:
        td = three_digits(n)
        print('%03d' % td)

