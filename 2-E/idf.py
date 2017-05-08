import sys
from string import ascii_lowercase

cache = {}

def num_df_start(l, available=26, initial='', initial_count=None):
    '''
    Return the number of possible expressions with distribution l on available
    letters starting with the string initial. It may still be unknown how often
    each of the letters of initial occurs in the final string.

    Available is a number specifying how many letters are still available; it
    corresponds to a final piece of ascii_lowercase (e.g., available=5 means
    that the letters 'vwxyz' can be used).

    Only letters in available may occur in initial.
    '''

    sum_initial_dist = len(initial)
    if sum_initial_dist > (l*(l+1))//2:
        return 0

    if initial_count is None:
        initial_count = {}
        for x in set(initial):
            initial_count[x] = initial.count(x)

    initial_dist = sorted(
            [initial_count[x] for x in set(initial)],
            reverse=True)

    if len(initial_dist) > l:
        return 0

    key = (
        tuple(initial_dist),
        initial_count[initial[-1]] if initial else None,
        l,
        available)
    if key in cache:
        return cache[key]

    if any(initial_dist[i] > l-i for i in range(min(len(initial_dist), l))):
        cache[key] = 0
        return 0

    if sum_initial_dist == (l*(l+1))//2:
        # given initial string is (the unique) solution
        cache[key] = 1
        return 1

    a = 0
    ndfs = {}
    for x in set(initial) - set(initial[-1]):
        icx = initial_count[x]
        try:
            a += ndfs[icx]
        except KeyError:
            initial_count[x] += 1
            ndfs[icx] = num_df_start(
                    l,
                    available,
                    initial=initial+x,
                    initial_count=initial_count)
            initial_count[x] -= 1
            a += ndfs[icx]

    new_letters = list(set(ascii_lowercase[26-available:]) - set(initial))
    if new_letters:
        x = new_letters[0]
        initial_count[x] = 1
        a += len(new_letters) * num_df_start(
                l,
                available,
                initial=initial+x,
                initial_count=initial_count)
        initial_count[x] -= 1

    cache[key] = a
    return a


def idf(k, n):
    number_of_expressions = [
            1,
            26,
            650,
            156000,
            385351200,
            12922802006400,
            7485426209701440000,
            ]  # these numbers are num_df_start(i), i = 0, ..., 6
               # hardcode them to save some time
    number_of_expressions_2 = [
            1,
            1,
            2,
            60,
            25776,
            196454880,
            32512818528000,
            137240175635933126400,
            ]  # these numbers are num_df_start(i, available=i)

    if n >= number_of_expressions[min(k, 6)]:
        # Take min above to avoid too long computation,
        # this is justified since we know that n <= 10**18.
        return -1

    initial = ''
    # check how long the "trivial" initial sequence is
    i = 1
    while n >= number_of_expressions_2[i]:
        i += 1

    j = max(0, (k - i) // 2)
    for ctr, x in enumerate([
            'ab', 'cd', 'ef', 'gh', 'ij', 'kl', 'mn',
            'op', 'qr', 'st', 'uv', 'wx', 'yz'][:j]):
        initial += x * (k - 2*ctr - 1) + x[0]

    k -= 2*j  # the expression still missing from result is
              # built from k-j different letters

    result = ''
    available = 26 - 2*j
    sum_l = k * (k+1) // 2

    while len(result) < sum_l:
        # add next letter
        for letter in ascii_lowercase[26-available:]:
            if result and letter == result[-1]:
                continue

            ndfs = num_df_start(k, available, initial=result+letter)

            if n < ndfs:
                result += letter
                break
            else:
                n -= ndfs
        else:
            print(n, ndfs, result, letter)
            raise Exception('Fail to find next letter')

    return initial + result


k, n = [int(x) for x in sys.stdin.read().split()]
print(idf(k, n-1))


