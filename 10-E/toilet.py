import sys

s = input().strip()

countD = s.count('D')
countU = len(s) - countD

a1 = 2 * countD
if s[:2] == 'DD':
    a1 -= 3
elif s[:2] == 'DU':
    a1 -= 1
print(a1)

a2 = 2 * countU
if s[:2] == 'UU':
    a2 -= 3
elif s[:2] == 'UD':
    a2 -= 1
print(a2)

print(len([1 for i in range(len(s)-1) if s[i] != s[i+1]]))

