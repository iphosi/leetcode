n = int(input())
children = list(map(lambda c: int(c), input().split()))
m = int(input())
chocolates = list(map(lambda c: int(c), input().split()))

children.sort()
chocolates.sort()

i = j = 0

while i < m and j < n:
    if chocolates[i] >= children[j]:
        j += 1
    i += 1

print(j)