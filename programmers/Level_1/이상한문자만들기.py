

def solution(s):
    list_str = list(map(str, s))

    answer = []
    for i in range(len(list_str)):
        if i % 2 == 0:
            answer.append(list_str[i].upper())
        else:
            answer.append(list_str[i].lower())

    return ''.join(answer)




print(solution("try hello world"))
print(solution('hello hello'))