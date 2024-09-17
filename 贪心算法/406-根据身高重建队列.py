from typing import List


# people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
# people = [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]


def reconstructQueue(people: List[List[int]]) -> List[List[int]]:
    people.sort(key=lambda p: (- p[0], p[1]))
    result = []

    for i in range(len(people)):
        if people[i][1] >= len(result):
            result.append(people[i])  # result 中的元素的身高值一定大于等于当前元素的身高值
        else:
            result.insert(people[i][1], people[i])  # 靠前的先插入

    return result


reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])