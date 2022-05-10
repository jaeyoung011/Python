def solution(s, n):
    to_list = list(map(str, s))
    char_sum = []
    for i in to_list:
        if i == ' ':
            char_sum.append(' ')
            # pass를 해버리면 공백을 구분못함
        elif chr(ord(i)+n) >= 'z':
            next_char_1 = chr(ord(i)-25+(n-1))
            char_sum.append(next_char_1)

        else:
            next_char_2 = chr(ord(i) + n)
            char_sum.append(next_char_2)
    answer = "".join(char_sum)

    return answer



print(solution("a B z", 1))

#뭔가 문제가있다...