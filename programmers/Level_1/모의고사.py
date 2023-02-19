def My_solution(answers):

    len_answer = len(answers)

    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]

    s1_multi = len_answer // len(s1)
    s2_multi = len_answer // len(s2)
    s3_multi = len_answer // len(s3)

    s1 += s1*s1_multi
    s2 += s2*s2_multi
    s3 += s3*s3_multi

    a1 = []
    a2 = []
    a3 = []

    for ans in range(len(answers)):
        if answers[ans] == s1[ans]:
            a1.append('correct')
        if answers[ans] == s2[ans]:
            a2.append('correct')
        if answers[ans] == s3[ans]:
            a3.append('correct')

    ans_sort = [len(a1), len(a2), len(a3)]
    winner_num = max(ans_sort)

    result = [winner+1 for winner in range(len(ans_sort)) if ans_sort[winner] == winner_num]
    return result

print(My_solution([1,3,2,4,2]))


# # 다른 사람 풀이_1 : 함수를 잘사용함
# def answer_type(pattern, length):
#     return pattern * (length // len(pattern)) + pattern[:length%len(pattern)]
#
# def check_answer(p, a):
#     return [(x==y) for x,y in zip(p,a)].count(True)
#
# def solution(answers):
#     p1 = [1,2,3,4,5]
#     p2 = [2,1,2,3,2,4,2,5]
#     p3 = [3,3,1,1,2,2,4,4,5,5]
#     ps = [p1,p2,p3]
#     anws =  [answer_type(p, len(answers)) for p in ps]
#     chks = [check_answer(a, answers) for a in anws]
#     return [i+1 for i in range(len(ps)) if chks[i] == max(chks)]
#

# def solution(answers):
#     pattern1 = [1,2,3,4,5]
#     pattern2 = [2,1,2,3,2,4,2,5]
#     pattern3 = [3,3,1,1,2,2,4,4,5,5]
#     score = [0, 0, 0]
#     result = []
#
#     for idx, answer in enumerate(answers):
#         if answer == pattern1[idx%len(pattern1)]:
#             score[0] += 1
#         if answer == pattern2[idx%len(pattern2)]:
#             score[1] += 1
#         if answer == pattern3[idx%len(pattern3)]:
#             score[2] += 1
#
#     for idx, s in enumerate(score):
#         if s == max(score):
#             result.append(idx+1)
#
#     return result
