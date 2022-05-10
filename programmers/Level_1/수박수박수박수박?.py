def solution(n):
    warehouse = '수박'*n

    return warehouse[:n]


# 이건 다른사람의 풀이 괜찮은것같다.

def water_melon(n):
    return "수박"*(n//2) + "수"*(n%2)
