
# 나의 풀이( 점수75)... 이해가 안가서 다른 사람 풀이 밑에 참조
def solution(n, lost, reserve):

    start = n - len(lost)

    for i in lost:
        if i + 1 in reserve:
            start += 1
            reserve.remove(i+1)
            #lost.remove(i) # 여기를 추가를 안해줬었다

        elif i - 1 in reserve:
            start += 1
            reserve.remove(i-1)
            #lost.remove(i)

    return start

print(solution(5, [2,4], [1,3,5]))
print(solution(5, [2,4], [3]))
print(solution(3, [3], [1]))

# 다른 사람 풀이
# 여별 체육복을 가지고 있는 사람도 도난을 당할수있다..! 이거를 까먹지 말았어야한다...
# https://rain-bow.tistory.com/30 (참조)
# 테스트 케이스 에서 계속 실패를 해서 설명을 듣고 문제를 정확하게 파악하는것이 중요하다는걸 알았다..

def solution(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)

    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n-len(set_lost)
