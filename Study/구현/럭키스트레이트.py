

def get_lucky(N):
    mid = len(str(N)) // 2
    left = []
    right = []
    for left_side in range(mid):
        left.append(str(N)[left_side])
    for right_side in range(mid, len(str(N))):
        right.append(str(N)[right_side])

    left_map = map(int, left)
    left_list = list(left_map)
    right_map = map(int, right)
    right_list = list(right_map)

    if sum(left_list) == sum(right_list):
        return 'LUCKY'
    else:
        return 'READY'

print(get_lucky(123402))



풀이

n = input()
length = len(n) # 점수값의 총 자릿수
summary = 0
# 왼쪽 부분의 자릿수 합 더하기
for i in range(length // 2):
    summary += int(n[i])
# 오른쪽 부분의 자릿수 합 빼기
for i in range(length //2, length):
    summary -= int(n[i])
    
# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary == 0:
    print("LUCKY")
else:
    print('READY')
# summary 를 이용해서 바로 구하는 방법이 인상적이다.


