


nums = [2,7,11,15]
target = 9



# def TwoSum(list, target):
#     for i in range(len(list)):
#         for j in range(i + 1, len(list)):
#
#             if list[i] + list[j] == target:
#                 return [i, j]
#

# 조회 구조 개선
def twoSum_map(nums, target):
    nums_map = {}
    # 하나의 for 문장으로 통함
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i



# 투 포인터 이용

def Twopoint_twosum(nums, target):
    left, right = 0, len(nums)-1
    while not left == right:
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        if nums[left] + nums[right] < target:
            left +=1
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]


Twopoint_twosum(nums, target)