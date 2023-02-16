
# def My_solution(sizes):
#
#     candidates = [sizes[i][0]*sizes[i][1]  for i in range(len(sizes))]
#     answer_cand = []
#     for i in range(len(sizes)):
#         for j in range(len(sizes)):
#             temp = sizes[i][0] * sizes[j][1]
#
#             if temp >= max(candidates):
#                 answer_cand.append(temp)
#     answer_cand = set(answer_cand)
#     answer_cand = [*answer_cand]
#     answer_cand = sorted(answer_cand)
#
#     if answer_cand[0] in candidates:
#         return answer_cand[0]
#     else:
#         return answer_cand[1]

# hint : 사실상 문제를 보면 가로x세로 길이를 명시해서 더 헷갈리게 만들었다.
# 사실 어떤 모서리는 가로가 될 수도 있고 세로도 될 수가 있다.
# 그치만 한 모서리를 가로라고 지정하면 다른 모서리는 세로가 되어야 옳다.
#
# 두 개의 모서리를 비교하여 큰 값을 전부 가로 작은 값을 전부 세로로 두면
# 각 모서리의 길이의 최댓값이 답이 되지않을까?

def My_solution(sizes):
    w = []
    h = []
    for i in range(len(sizes)):
        w.append(max(sizes[i]))
        h.append(min(sizes[i]))

    return max(w) * max(h)


# 문제 이해가 먼저다.




print(My_solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
# print(My_solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
# print(My_solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))