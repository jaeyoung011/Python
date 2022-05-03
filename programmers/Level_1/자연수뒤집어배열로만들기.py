def solution(n):
    n = list(str(n))
    result = list(reversed(n))
    result = list(map(int, result))

    return result


print(solution(12345))