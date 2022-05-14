

def solution(s):

    # setting
    s = s.lower()
    str_list = list(map(str,s))

    # count start
    y_count = []
    p_count = []
    for i in str_list:
        if i == 'y':
            y_count.append(i)
        elif i == 'p':
            p_count.append(i)

    # get result
    if len(y_count) == 0 and len(p_count) == 0:
        return True
    elif len(y_count) == len(p_count):
        return True
    else:
        return False



print(solution("pPoooyY"))



### 다른 사람들의 풀이

def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')


