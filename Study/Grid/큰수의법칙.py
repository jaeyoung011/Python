

# n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
# data = list(map(int, input().split()))

# 내 답안
def big_number_rule(data):
    n, m, k = 5, 8, 3
    sum = 0
    first = sorted(data, reverse=True)[0]
    second = sorted(data, reverse=True)[1]

    # 계산시작
    for i in range(1,m+1):
        if i % (k+1) != 0:
            sum += first
        else:
            sum += second
    return sum


print(big_number_rule([2,4,5,4,6]))

# 모법 답안 1

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
    for i in range(k): # 가장 큰 수를 K번 더하기
        if m == 0: # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 # 더할때마다 1씩 뺴기
    if m ==0: # m이 0이라면 반복문 탈출
        break
    result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1 # 더할 때마다 1씩 빼기

print(result)


# 모범 답안2

data.sort()
first = data[n - 1]
second = data[n - 2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result) # 최종 안 출력