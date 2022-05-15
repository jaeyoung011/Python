


def solution(arr):

    result = [arr[0]]
    for value in range(1,len(arr)):
        pre = arr[value-1]
        if pre != arr[value]:
            result.append(arr[value])

    return result


# print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))