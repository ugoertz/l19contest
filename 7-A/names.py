
def num_changes(s):
    '''Compute how many letters need to be changed to make s into
    a palindrome. (No adding of letters at this point.)'''

    n = len(s) - 1
    return len([i for i in range(n//2 + 1) if s[i] != s[n-i]])


name = list(input())
print(min(num_changes(name[i:]) + i for i in range(len(name)//2 + 1)))


