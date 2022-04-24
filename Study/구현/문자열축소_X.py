

def solution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1
        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 다시 상태 초기화
                count = 1
        # 남아있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    return answer
print(solution('abcabcabcabcdededededede'))


# 생각만하다가 전혀 풀지못하였다.
# 1) for 문에서 step 만큼의 문자열 추출을 해주어야 한다.
# 2) 두번째에서 동일한게 있으면 count += 1 을해주어서 올려준다.
# 3) prev 를 업데이트 해주는게 신선했다.
# 4) compressed에 대해서 변형시켜주는방식
# 5) answer 에서 이태까지 나온걸 min(answer, len(compressed))로 값을 결정하는게 신선했다.

# 결론 : 기초가 많이 부족하고 for 문에 대해서 더 정확하게 아는게 중요하다고 생각한다.
