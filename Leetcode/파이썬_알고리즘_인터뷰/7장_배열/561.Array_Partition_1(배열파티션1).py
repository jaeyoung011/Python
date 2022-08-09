

## [O, , ,]
# 다른 풀이 방법은 참조할만하다.


import numpy as np
from itertools import combinations

#Q) n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
# Ex) n은 2 가 되면, 최대합은 4이다.
# min(1,2) + min(3,4) = 4

nums = [1,4,3,2]

def arrayPariSum(nums):

    # 내 풀이
    # pair_list = []
    # for i in range(len(nums)- 1):
    #     for j in range(i+1, len(nums)):
    #         a, b = nums[i], nums[j]
    #         pair_list.append((a,b))

    # pair_list = list(combinations(nums,2)) # 똑같다.

    # 방법1
    # sum = 0
    # pair = []
    # nums.sort()
    #
    # for n in nums:
    #     # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
    #     pair.append(n)
    #     if len(pair) == 2:
    #         sum += min(pair)
    #         pair = [] # reset
    # return sum

    # 방법2
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        # 짝수 번째 값의 합 계산
        if i % 2 == 0:
            sum += n
    return sum

print(arrayPariSum(nums))


# Pythonic Way
def arrayPiarSum_pythonic(nums):
    return sum(sorted(nums[::2])) # [::2]는 2칸씩 건더뛰므로 짝수 번째를 계산하는 것과 동일하다.











