

def My_solution(nums):

    can_get = len(nums)//2
    set_nums = set(nums)
    len_set_nums = len(set_nums)

    if len_set_nums > can_get:
        return can_get
    else:
        return len_set_nums


print(My_solution(nums=[3,3,3,2,2,2]))