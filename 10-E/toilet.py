import sys

s = input().strip()

a1 = 2 * s.count('D')
if s[:2] == 'DD':
    a1 -= 3
elif s[:2] == 'DU':
    a1 -= 1
print(a1)

a2 = 2 * s.count('U')
if s[:2] == 'UU':
    a2 -= 3
elif s[:2] == 'UD':
    a2 -= 1
print(a2)

print(sum(1 for i in range(len(s)-1) if s[i] != s[i+1]))

