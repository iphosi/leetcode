from collections import defaultdict


n = int(input())
gt_pw = input()
pw_list = [input() for _ in range(n)]
pw_set = set(pw_list)

len_dict = defaultdict(int)

for pw in pw_set:
    len_dict[len(pw)] += 1

min_num_attempts = 0

for l in range(len(gt_pw)):
    if l in len_dict:
        min_num_attempts += len_dict[l]

max_num_attempts = min_num_attempts + len_dict[len(gt_pw)]
min_num_attempts += 1

print(" ".join([str(min_num_attempts), str(max_num_attempts)]))