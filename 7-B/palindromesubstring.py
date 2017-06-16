import sys

def palindromes(s):
    result = set([])

    for i in range(len(s) - 1):
        # even length palindromes with "left middle" at index i
        for j in range(min(i+1, len(s)-i-1)):
            if s[i-j] != s[i+j+1]:
                break
            result.add(s[i-j:i+j+2])

        # odd length palindromes with middle at index i
        j = 1
        for j in range(1, min(i+1, len(s)-i)):
            if s[i-j] != s[i+j]:
                break
            result.add(s[i-j:i+j+1])

    return result

result = []
for s in sys.stdin.readlines():
    result.append('\n'.join(sorted(palindromes(s))))

print('\n\n'.join(result))

