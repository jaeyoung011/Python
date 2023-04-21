import pandas as pd

# n = int(input())
# member_lst = []
#
# for i in range(n):
#     member_lst.append(input())
#
# member_list = list(map(lambda x : x.split(' ') , member_lst))
# member_df = pd.DataFrame(member_list)
# result = member_df.sort_values(by=[0], axis=0)
# print(result)


# test2

n = int(input())
member_lst = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    member_lst.append((age, name))

member_lst.sort(key = lambda x: x[0])

for i in member_lst:
    print(i[0], i[1])