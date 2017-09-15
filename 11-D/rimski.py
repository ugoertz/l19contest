B = input().strip()

B1 = ''
for b in B:
    if b in ['X', 'L', 'C']:
        B1 += b
    else:
        break
if B1 == 'LX':
    B1 = 'XL'

B2 = B[len(B1):]
if B2 == 'VI':
    B2 = 'IV'
elif B2 == 'I' and B1.endswith('X'):
    B1 = B1[:-1]
    B2 = 'IX'
if B1 == 'LX':
    B1 = 'XL'

print(B1+B2)

