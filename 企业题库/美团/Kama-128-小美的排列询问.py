n = int(input())

a = list(map(lambda s: int(s), input().split()))

x, y = list(map(lambda s: int(s), input().split()))

i_x = i_y = -1

for i in range(n):
    if a[i] == x:
        i_x = i
    if a[i] == y:
        i_y = i

if abs(i_x - i_y) == 1:
    print("Yes")
else:
    print("No")