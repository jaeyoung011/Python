def solution(n):

    list_divisor = []
    for i in range(1,n+1):
        if n % i == 0:
            list_divisor.append(i)
    answer = sum(list_divisor)

    return answer


print(solution(12))



# 다른 사람 풀이
def sumDivisor(num):
    return sum([i for i in range(1,num+1) if num%i==0])


# 이렇게 if 문을 한줄로...깔끔하게 쓰도록 지향하자
