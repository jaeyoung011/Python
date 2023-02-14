
# 각 단어의 짝수번째 알파벳은 대문자, 홀수번쨰 알파벳은 소문자!!

# def My_solution(s):
#
#     s = list(s)
#
#     new_list = []
#     for i in range(len(s)):
#         if i % 2 == 0:
#             new_list.append(s[i].upper())
#         else:
#             new_list.append(s[i].lower())
#
#     return  ''.join(new_list)


# def My_solution(s):
#
#     # temp = s.split(" ") # 공백1 개를 각각의 공백으로 따로따로 처리
#
#     temp = s.split(sep=' ')
#     new_list = []
#
#     for i in temp:
#
#         if i.isalpha():
#             each_word = list(i)
#         else:
#             new_list.append(i)
#         for j in range(len(each_word)):
#             if j % 2 == 0:
#                 new_list.append(each_word[j].upper())
#             else:
#                 new_list.append(each_word[j].lower())
#         new_list.append(' ')
#
#     new_list = new_list[:-1]
#
#
#     return ''.join(new_list)

def solution(s): # 다른사람 풀이
    answer = []
    word=s.split(" ")
    for i in word:
        part=[]
        for j in range(0,len(i)):
            if j%2==0:
                part.append(i[j].upper())
            else:
                part.append(i[j].lower())
        part="".join(part)
        answer.append(part)
    answer=" ".join(answer)
    print(answer)
    return answer


print(solution("try hello world"))