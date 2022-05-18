
from itertools import combinations

def solution(numbers):
    combi_list = list(combinations(numbers,2))

    comb_sum = []
    for i in combi_list:
        comb_sum.append(sum(i))

    comb_sum = list(set(comb_sum))

    return sorted(comb_sum) # tuple -> list 가능


print(solution([2,1,3,4,1]))