def solution(arr):
    if len(arr) <= 1:
        return [-1]
    elif len(arr) > 2:
        result = [arr[0]]
        temp = arr[0]
        for i in range(1,len(arr)):
            if temp > arr[i]:
                result.append(arr[i])
                temp = arr[i]
            elif temp < arr[i]:
                result.append(arr[i])
                temp = temp
        result.remove(temp) # remove 는 특정 값을 / pop 은 특정 인덱스를 없애준다.

        return result


# print(solution([4,3,2,1]))



def rm_small(mylist): # -1 적용전문제
    return [i for i in mylist if i > min(mylist)]

#와... 이렇게 2줄로 끝낼수있다니...

def rm_small_1(mylist): # -1 적용전문제
    mylist.remove(min(mylist))
    return mylist




print(rm_small([4,3,2,1]))