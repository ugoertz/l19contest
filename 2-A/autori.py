import sys
from string import ascii_uppercase

print(''.join(x for x in sys.stdin.read() if x in ascii_uppercase))

