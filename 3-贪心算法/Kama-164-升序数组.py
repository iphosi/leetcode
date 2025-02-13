n = int(input())
a = list(map(lambda s: int(s), input().split()))

count = 0

for i in range(1, n):
    if a[i] < a[i - 1]:
        count += max(0, a[i - 1] - a[i] + 1 - count)

print(count)