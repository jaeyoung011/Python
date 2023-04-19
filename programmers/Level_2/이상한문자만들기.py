

def my_solution(s):

    list_char = list(s)

    count = 0
    for i in range(len(list_char)):
        if list_char[i] == ' ':
            count = 0
            continue

        elif count % 2 == 0:
            list_char[i] = list_char[i].upper()
            count+=1

        elif count % 2 != 0:
            list_char[i] = list_char[i].lower()
            count+= 1

    result = ''.join(list_char)
    return result


def book_solution(s):
    s = list(s)
    cnt = 0
    for i in range(len(s)):
        if s[i] == ' ':
            cnt = 0 # 공백을 만나면 카운트 ㅗ기화
            continue
        s[i] = s[i].upper() if cnt % 2 == 0 else s[i].lower()
        cnt += 1
    return ''.join(s)



if __name__ == '__main__':
    """각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로"""

    s = "try hello world"

    result  = my_solution(s)
    print(result)