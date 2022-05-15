
def solution(a, b):
    sum = 0
    if b > a:
        for i in range(a,b+1):
            sum += i
    elif b < a:
        for i in range(b, a+1):
            sum += i
    else:
        sum = a

    return sum

print(solution(5,3))


# 다른 풀이들

def adder(a, b): # 수열공식을 이용
    return (abs(a-b)+1)*(a+b)//2


def adder(a, b): # 이런 방식도...?
    if a > b: a, b = b, a

    return sum(range(a,b+1))

