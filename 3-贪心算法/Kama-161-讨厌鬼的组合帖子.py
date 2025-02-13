n = int(input())
a = list(map(lambda n: int(n), input().split()))
b = list(map(lambda n: int(n), input().split()))

g1 = g2 = 0

for i in range(n):
    if a[i] - b[i] > 0:
        g1 += a[i] - b[i]
    else:
        g2 += b[i] - a[i]

print(max(g1, g2))