from string import ascii_lowercase

data = input()

result = []
indent = 0
current_word = []
for x in data:
    if x in ascii_lowercase:
        current_word.append(x)
    elif x == '{':
        result.append(' ' * indent + '{')
        indent += 2
    elif x == '}':
        if current_word:
            result.append(' ' * indent + ''.join(current_word))
            current_word = []
        indent -= 2
        result.append(' ' * indent + '}')
    elif x == ',':
        if current_word:
            result.append(' ' * indent + ''.join(current_word))
            current_word = []
        result[-1] += ','  # also if ',' follows a '}'

print('\n'.join(result))
