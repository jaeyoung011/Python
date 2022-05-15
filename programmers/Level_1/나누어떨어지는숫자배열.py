

def solution(arr, divisor):
    answer = []
    nothing = []
    for i in arr:
        if i % divisor != 0:
            nothing.append(i)
        elif i % divisor == 0:
            answer.append(i)
    if len(nothing) == len(arr):
        return [-1]
    return sorted(answer)

print(solution([2,36,1,3], 2))