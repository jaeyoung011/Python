def solution(n):

    list_divisor = []
    for i in range(1,n+1):
        if n % i == 0:
            list_divisor.append(i)
    answer = sum(list_divisor)

    return answer


print(solution(12))