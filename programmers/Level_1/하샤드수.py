def solution(x):
    x = str(x)
    # sum = [] : 이렇게 하면 당연히 더할수없지않은가
    sum = 0
    for i in x:
        i = int(i)
        sum += i

    if int(x) % sum == 0:
        return True
    else:
        return False

print(solution(12))



## 좋은 풀이

def Harshad(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Harshad(18))