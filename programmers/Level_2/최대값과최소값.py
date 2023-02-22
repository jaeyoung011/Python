def My_solution(s):
    s = s.split(' ')
    to_int = list(map(int, s))
    return f'{min(to_int)} {max(to_int)}'


print(My_solution("-1 -2 -3 -4"))