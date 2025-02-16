from typing import List
from collections import defaultdict


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    result_dict = defaultdict(list)

    for string in strs:
        result_dict["".join(sorted(string))].append(string)

    return list(result_dict.values())
