

def solution(n, lost, reserve):

    start = n - len(lost)

    for i in lost:
        if i + 1 in reserve:
            start += 1
            reserve.remove(i+1)
            #lost.remove(i) # 여기를 추가를 안해줬었다

        elif i - 1 in reserve:
            start += 1
            reserve.remove(i-1)
            #lost.remove(i)

    return start

print(solution(5, [2,4], [1,3,5]))
print(solution(5, [2,4], [3]))
print(solution(3, [3], [1]))

# 다른 사람 풀이

def solution(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)

    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n-len(set_lost)