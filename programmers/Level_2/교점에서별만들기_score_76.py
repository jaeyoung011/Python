# -*- coding: utf-8 -*-

from itertools import combinations

def _base_line(line1, line2):

    A, B, E = line1[0], line1[1], line1[2]
    C, D , F = line2[0] , line2[1], line2[2]

    if (A*D) - (B*C) == 0:
        return '', ''
    else:
        x = (B*F - E*D) / (A*D - B*C)
        y = (E*C - A*F) / (A*D - B*C)

        if x.is_integer() and y.is_integer(): # 정수일때 x, y
            return int(x), int(y)
        else:
            return '', ''


# def My_solution(line):
#     # 1) 만나는 좌표중 정수인것만 찾기
#     combi = list(combinations(line, 2))
#     answer_list = []
#     for i in combi:
#         x, y  = _base_line(i[0], i[1])
#         if x == '' or y == '':
#             pass
#         else:
#             answer_list.append([x,y])
#
#     # 2) 스케치 밑그림 그리고 그에맞게 별그림 그려주기
#     # 2-1) 그래프 그리기 쉽게 같은 부호로 바꾸어주기
#     x_negative_list = []
#     y_negative_list = []
#     for i in answer_list:
#         if i[0] < 0:
#             x_negative_list.append(i[0])
#         if i[1] < 0:
#             y_negative_list.append(i[1])
#
#     if len(x_negative_list) != 0:
#         min_x = abs(min(x_negative_list))
#     else:
#         min_x = 0
#
#     if len(y_negative_list) != 0:
#         min_y = abs(min(y_negative_list))
#     else:
#         min_y = 0
#
#     for i in answer_list:
#         i[0] += min_x
#         i[1] += min_y
#
#     # 2-2) 리스트에 맞게 별 그려주기
#     x_coor_max = max([x[0] for x in answer_list]) + 1
#     y_coor_max = max([y[1] for y in answer_list]) + 1
#
#     # y 축에 맞추어서 정렬해주기
#     answer_list = sorted(answer_list, key=lambda answer_list : answer_list[1] , reverse=False)
#
#     final_result = []
#     for i in range(y_coor_max):
#
#         result_temp = []
#         for j in range(x_coor_max):
#             if [j, i] in answer_list:
#                 result_temp.append('*')
#             else:
#                 result_temp.append('.')
#         final_result.append(result_temp)
#
#
#     final_result.reverse()
#
#     # 밑에 교점이없을떄 제거
#     for i in range(len(final_result)):
#         if '*' not in final_result[-1]:
#             final_result.pop()
#
#
#     final_result = [''.join(final_result[i]) for i in range(len(final_result)) ]
#
#
#
#     return final_result


def My_solution(line):
    # 1) 만나는 좌표중 정수인것만 찾기
    combi = list(combinations(line, 2))
    answer_list = []
    for i in combi:
        x, y  = _base_line(i[0], i[1])
        if x == '' or y == '':
            pass
        else:
            answer_list.append([x,y])

    # 2) 스케치 밑그림 그리고 그에맞게 별그림 그려주기
    # 2-1) 그래프 그리기 쉽게 같은 부호로 바꾸어주기
    x_negative_list = []
    y_negative_list = []
    for i in answer_list:
        if i[0] < 0:
            x_negative_list.append(i[0])
        if i[1] < 0:
            y_negative_list.append(i[1])

    if len(x_negative_list) != 0:
        min_x = abs(min(x_negative_list))
    else:
        min_x = 0

    if len(y_negative_list) != 0:
        min_y = abs(min(y_negative_list))
    else:
        min_y = 0

    for i in answer_list:
        i[0] += min_x
        i[1] += min_y

    # 2-2) 리스트에 맞게 별 그려주기
    x_coor_max = max([x[0] for x in answer_list]) + 1
    y_coor_max = max([y[1] for y in answer_list]) + 1

    # y 축에 맞추어서 정렬해주기
    answer_list = sorted(answer_list, key=lambda answer_list : answer_list[1] , reverse=False)

    final_result = []
    for i in range(y_coor_max):

        result_temp = []
        for j in range(x_coor_max):
            if [j, i] in answer_list:
                result_temp.append('*')
            else:
                result_temp.append('.')
        final_result.append(result_temp)


    final_result.reverse()

    # 밑에 교점이없을떄 제거
    for i in range(len(final_result)):
        if '*' not in final_result[-1]:
            final_result.pop()


    final_result = [''.join(final_result[i]) for i in range(len(final_result)) ]



    return final_result


print(My_solution(	[[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
# print(My_solution( [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]  ))