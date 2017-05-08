import sys

def digit_sum(x):
    return sum(int(z) for z in str(x))

def digit_sum_interval(x, y):
    if y - x <= 10:
        return sum(digit_sum(z) for z in range(x, y+1))

    xp = (x // 10) + 1
    ym = y // 10

    return (
            digit_sum_interval(x, xp * 10 - 1) +
            45 * (ym - xp) +     # 45 == digit_sum_interval(0, 9)
            digit_sum_interval(xp, ym-1) * 10 +
            digit_sum_interval(ym * 10, y)
            )


for ctr, line in enumerate(sys.stdin):
    if ctr == 0:
        number_test_cases = int(line)
        continue
    if ctr > number_test_cases:
        # trailing lines?
        break

    a, b = [int(x) for x in line.split()]
    print(digit_sum_interval(a, b))
    # print(sum(digit_sum(x) for x in range(a, b+1)))


