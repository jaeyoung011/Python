

# 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어 수
# 실패율이 높은 스테이지부터 내림순으로 스테이지의 번호가 담겨있는 배열을 return
#
# def MY_solution_v1(N, stages):
#
#     challenger = len(list(stages))
#     answer = []
#     fail_rate = []
#     for i in range(1, N+1):
#         fail_rate_state = len([j for j in stages if j == i]) / challenger
#         fail_rate.append(fail_rate_state)
#         challenger -= len([j for j in stages if j == i])
#
#     while len(answer) != N:
#         select = list(filter(lambda x: fail_rate[x] == max(fail_rate), range(len(fail_rate))))
#         [answer.append(anw) for anw in select]
#
#         remove_set = max(fail_rate)
#
#         while remove_set in fail_rate:
#             fail_rate.remove(remove_set)
#
#     return answer


def MY_solution(N, stages):

    challenger = len(list(stages))
    answer = []
    fail_rate = []
    for i in range(1, N+1):
        fail_rate_state = len([j for j in stages if j == i]) / challenger
        fail_rate.append(fail_rate_state)

        challenger -= len([j for j in stages if j == i])
        if challenger != 0:
            pass
        else:
            challenger=1


    for ans in sorted(set(fail_rate) , reverse=True):
        select = list(filter(lambda x: fail_rate[x] == ans, range(len(fail_rate))))
        [answer.append(anw) for anw in select]

    return [k+1 for k in answer]




# print(MY_solution(5, [2,1,2,6,2,4,3,3]))
print(MY_solution(5, [3,3,3,3])) # 분모가 0인경우를 생각해 주어야했다.