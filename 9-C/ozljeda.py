K = int(input())
a = input().split()
d = [0]
for x in a:
    d.append(d[-1] ^ int(x))  # d[i] == a_1 ^ ... ^ a_i

Q = int(input())

for i in range(Q):
    l, r = [int(x) for x in input().split()]
    print(d[r % (K+1)] ^ d[(l-1) % (K+1)])

