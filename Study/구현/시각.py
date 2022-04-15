

# n시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력한다.
# n = 5

def count_in_3(hour):
    count = 0
    for h in range(hour+1):
        for m in range(60):
            for s in range(60):
                if '3' in str(h) + str(m) + str(s):
                    count += 1
    return count


print(count_in_3(5))