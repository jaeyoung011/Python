def My_solution(t, p):

    slice_len = len(p)
    list_t = list(t)
    new_list = []
    for i in range(len(list_t)):
        if len(list_t[i:(i + slice_len)]) >= slice_len:
            new_list.append(list_t[i:(i + slice_len)])
        else:
            pass

    answer = 0
    for i in [int(''.join(i)) for i in new_list]:
        if int(p) >= i:
            answer += 1

    return answer


print(My_solution("3141592", "271"))





