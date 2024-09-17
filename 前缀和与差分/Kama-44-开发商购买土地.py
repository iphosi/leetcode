# nums[i1:i2 + 1][j1:j2 + 1] 中所有元素的和等于
# prefix[i2][j2] - prefix[i1 - 1][j2] - prefix[i2][j1 - 1] + prefix[i1 - 1][j1 - 1]


num_rows, num_cols = list(map(lambda n: int(n), input().split()))

matrix = [
    list(map(lambda n: int(n), input().split()))
    for _ in range(num_rows)
]

for i in range(num_rows):
    for j in range(1, num_cols):
        matrix[i][j] += matrix[i][j - 1]

for j in range(num_cols):
    for i in range(1, num_rows):
        matrix[i][j] += matrix[i - 1][j]

result = matrix[-1][-1]

for i in range(num_rows):
    result = min(result, abs(matrix[-1][-1] - 2 * matrix[i][-1]))

for j in range(num_cols):
    result = min(result, abs(matrix[-1][-1] - 2 * matrix[-1][j]))

print(result)
