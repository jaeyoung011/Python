from itertools import combinations

# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를  출력하라
nums = [-1, 0, 1, 2, -1, -4]

# 나의 풀이
def three_sum(nums): # time_out....
    sum = 0
    list = []
    for i in range(3, 4):
        for i in combinations(nums, i):
            for j in i:
                sum += j
            if sum == 0:
                list.append(i)
            else:
                sum = 0
    # sorted 로 중복 확인
    new_list = [sorted(i) for i in list]
    # 같은 tuple 값 제거
    result = [t for t in (set(tuple(i) for i in new_list))]

    return result


def threeSum_brute(nums):
    results = []
    nums.sort()

    # 브루트 포스 n^3 반복
    for i in range(len(nums) - 2): # 한칸 한칸 i가 2번 중복이 되면 안되니까
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 1):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k-1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append([nums[i], nums[j], nums[k]])




def two_point_threesum(nums):
    results = []
    nums.sort()
    # nums = [-1, 0, 1, 2, -1, -4]
    for i in range(len(nums) - 2): # why -2 : i 가 연속으로 나타나는것을 방지하기 위해서
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # 간격을 좁혀가며 합 sum 계산
        left, right = i + 1 , len(nums) -1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # sum = 0 인경우이므로 정답 및 스킵 처리
                results.append([nums[i], nums[left] , nums[right]])

                while left < right and nums[left] == nums[left + 1]: # 중복 방지같은건가..? => 여기 부분 약간이해안감
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return results


print(two_point_threesum(nums))