# -*- coding: utf-8 -*-


def solution(line):
    # prevent swallow copy
    pos, answer = [], []
    n = len(line)

    x_min = y_min = int(1e15)
    x_max = y_max = -int(1e15)

    #1 주어진 직선에서 교점을 구합니다.
    for i in range(n):
        a, b, e = line[i]
        for j in range(i+1, n):
            c, d, f = line[j]
            if a * b == b * c : continue
            x = (b*f - e*d) / (a*d - b*c)
            y = (e*c - a*f) / (a*d - b*c)


    # 2. 그중 정수 교점만 따로 변수로 저장합니다.
    if x == int(x) and y == int(y):
        x = int(x)
        y = int(y)
        pos.append([x, y])

        #교점을 모두 표현할 수 있는 최소한의 사각형을 알아냅니다.
        if x_min > x: x_min = x # 파이썬 문법 확인
        if y_min > y: y_min = y
        if x_max < x: x_max = x
        if y_max < y: y_max = y

    x_len = x_max - x_min + 1
    y_len = y_max - y_min + 1
    coord = [['.' * x_len for _ in range(y_len)]]

    for star_x, star_y in pos:
        nx = star_x + abs(x_min) if x_min < 0 else star_x - x_min
        ny = star_y + abs(y_min) if y_min < 0 else star_y - y_min
        coord[ny][nx] = '*'

    for result in coord: answer.append(''.join(result))

    return answer[::-1] # == [].reverse() or reversed([])


print(solution(	[[0, 1, -1], [1, 0, -1], [1, 0, 1]]))

