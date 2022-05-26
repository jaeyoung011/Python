

def solution(numbers):
    sum = 0

    elements = [1,2,3,4,5,6,7,8,9]
    for i in elements:
        if i not in numbers:
            sum += i

    return sum



print(solution([1,2,3,4,6,7,8,0]))