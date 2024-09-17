n, m = list(map(lambda i: int(i), input().split()))

candy_list = list(map(lambda i: int(i), input().split()))
candy_list.sort(key=lambda c: - c)

bear_list = []

for i in range(n):
    bear_list.append(
        [i] + list(map(lambda i: int(i), input().split()))
    )

bear_list.sort(key=lambda b: - b[1])

for i in range(n):
    j = 0

    while j < m and bear_list[i][1] > 0:
        if candy_list[j] != 0 and candy_list[j] <= bear_list[i][2]:
            bear_list[i][2] -= candy_list[j]
            candy_list[j] = 0
        j += 1

bear_list.sort(key=lambda b: b[0])

for bear in bear_list:
    print(bear[2])