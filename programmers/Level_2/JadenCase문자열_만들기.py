# def My_solution(s):
#     to_list_word = s.split(" ")
#     clean_list = [i for i in to_list_word if i != ''] # 이게 빠져야함
#     # answer = []
#     for i in range(len(clean_list)):
#         if clean_list[i].isalpha():
#             clean_list[i] = clean_list[i].upper()[0] + clean_list[i].lower()[1:]
#
#         else:
#             clean_list[i] = clean_list[i][0] + clean_list[i].lower()[1:]
#
#     return ' '.join(clean_list)

#
def My_solution_2(s):
    to_list_word = s.split(" ")
    answer = []
    for i in to_list_word:
        if i!= '':
            i = i.upper()[0] + i.lower()[1:]
            answer.append(i)
        else:
            answer.append(i)

    return ' '.join(answer)


print(My_solution_2("a 3peoPle    a  a a a a a a a a "))

""" 코드리뷰 """
# 1) 처음에 문제를 잘 읽지 공백이 여러개인것을 간과하였다.
# 2) '3peopple'.isalpha() 에서 3people은 isalnum() 즉 str 이였다.