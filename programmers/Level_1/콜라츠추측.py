# def solution(num):
#     count = 0
#     while num != 1:
#         if num % 2 == 0:
#             num = (num//2)
#             count += 1
#         elif num %2 != 0:
#             num = (num*3) +1
#             count += 1
#         # elif count >= 500: 스쳐지나간다 왜냐면 이거는 num에 관한것들이니까
#         #     return -1
#     return count
#
# print(solution(626331))

def solution(num):
    count = 0
    while num != 1:
        if num % 2 == 0:
            num = (num//2)
            count += 1
        elif num %2 != 0:
            num = (num*3) +1
            count += 1
    if count >= 500:
        return -1
    else:
        return count