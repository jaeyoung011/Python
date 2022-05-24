import itertools

def solution(d, budget): # 82.6

    d = sorted(d)

    sum = 0
    for i,v in enumerate(d):
        sum += v
        if sum > budget:
            return i
        elif sum == budget:
            return i+1

# print(solution([1,3,2,5,4], 9))
# print(solution([2,2,3,3], 10))
print(solution([2], 2))

# # 다른사람의 풀이
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

