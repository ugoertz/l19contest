import sys
from math import pi, log, ceil
log10 = log(10)
logsqrt2pi = 0.5 * log(2*pi)

def logstirling(n):
    return logsqrt2pi + (n + 0.5) * log(n) - n

def numberdigits(n):
    if n <= 1:
        return 1
    return ceil(logstirling(n)/log10)

for l in sys.stdin.readlines():
    if l.strip():
        print(numberdigits(int(l)))
