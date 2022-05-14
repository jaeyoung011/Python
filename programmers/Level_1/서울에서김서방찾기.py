

def solution(seoul):

    for index, value in enumerate(seoul):
        if value == 'Kim':
            return '김서방은 {}에 있다'.format(index)


print(solution(["Jane", "Kim"]))


# 다른사람 풀이

def findkim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

# index 라는 함수를 찾는것이 중요