from itertools import combinations


# def My_solution(number):
#     combi = list(combinations(number, 3))
#
#     count = 0
#     for i in range(len(combi)):
#         if sum(combi[i]) == 0:
#             count += 1
#
#     return count


def My_solution_2(number):
    combi = list(combinations(number, 3))
    answer = [len(combi[i]) for i in range(len(combi)) if sum(combi[i]) == 0]
    return len(answer)




print(My_solution_2([-2, 3, 0, 2, -5]))