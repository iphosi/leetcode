from typing import List
from collections import defaultdict


def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    address_to_name = {}
    parent_dict = {}

    def find(u):
        if parent_dict[u] == u:
            return u
        else:
            parent_dict[u] = find(parent_dict[u])
            return parent_dict[u]

    def join(u, v):
        u = find(u)
        v = find(v)

        if u != v:
            parent_dict[u] = v

    for info in accounts:
        left = 1
        right = 2
        address_to_name[info[left]] = info[0]
        if info[left] not in parent_dict:
            parent_dict[info[left]] = info[left]

        while right < len(info):
            address_to_name[info[right]] = info[0]
            if info[right] not in parent_dict:
                parent_dict[info[right]] = info[right]
            join(info[left], info[right])
            right += 1

    result_dict = defaultdict(list)

    for address in address_to_name.keys():
        result_dict[find(address)].append(address)

    result = [
        [address_to_name[root]] + sorted(result_dict[root])
        for root in result_dict.keys()
    ]

    return result
