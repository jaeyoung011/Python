
# 0, 1, 1, 2, 3, 5, 8, 13

def _fib(n): # 재귀함수 사용해서 런타임 에러
    if n == 0:
        return 0
    if n == 1 or n==2:
        return 1
    else:
        return _fib(n-2) + _fib(n-1)


def My_solution(n):
    new_n = _fib(n)
    return new_n % 1234567

print(_fib(7))

print(My_solution(7))

def My_solution_2(n):

    list_fibo = []
    for i in range(n):
        if i < 3:
            if i == 0:
                list_fibo.append(0)
            else:
                list_fibo.append(1)
        else:
            i = list_fibo[i-2] + list_fibo[i-1]
            list_fibo.append(i)
    sum = list_fibo[-2] + list_fibo[-1]
    return sum % 1234567

print(My_solution_2(5))

