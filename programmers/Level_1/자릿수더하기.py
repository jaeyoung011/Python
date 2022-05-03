def solution(n):
    n = list(str(n))
    list_int = list(map(int, n))
    sum = 0
    for i in list_int:
        sum += i

    return sum