# -*- coding: utf-8 -*-


def _binaryNum(n):
    return format(n, 'b')

def My_solution(s):
    s = list(map(int, s))
    transform = 0
    count_0 = 0
    while len(s) != 1:

        new_s = []
        for i in s:
            if i == 0:
                count_0+=1
            else:
                new_s.append(i)

        s = _binaryNum(len(new_s))
        s = list(map(int, s))
        transform += 1

    return [transform, count_0]


print(My_solution("110010101001"))