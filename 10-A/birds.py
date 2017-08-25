l, d, n = [int(x) for x in input().split()]
l = l - 12 + 2*d

birds = [0, l, ]  # place birds at beginning and end to ensure correct handling there
birds.extend(int(input()) - 6 + d for i in range(n))
birds = sorted(birds)

print(sum((birds[i+1] - birds[i])//d - 1 for i in range(len(birds)-1)))





