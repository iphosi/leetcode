from collections import defaultdict


def canConstruct(ransomNote: str, magazine: str) -> bool:
    count_dict = defaultdict(int)

    for char in magazine:
        count_dict[char] += 1

    for char in ransomNote:
        if char not in count_dict.keys():
            return False
        else:
            count_dict[char] -= 1
            if count_dict[char] < 0:
                return False

    return True
