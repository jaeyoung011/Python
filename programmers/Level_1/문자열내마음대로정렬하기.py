


# 실패...

def solution(strings, n):
    n_list = []
    for index, value in enumerate(strings):
        n_list.append(value[n])

    # values = sorted(n_list)
    values = sorted(range(len(n_list)), key=lambda k: n_list[k])

    answer = []
    for i in values:
        answer.append(strings[i])



    return answer




def solution(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n])


print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))



# 리스트를 정렬 key사용(sort, sorted)

a = [(1, 2), (5, 1), (0, 1), (5, 2), (3, 0)]

# ▷ key 인자를 정하지 않은 기본적인 sort에선, 튜플 순서대로 우선순위 기본 할당
# 앞의 인자로 정렬됨
b = sorted(a)
b = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]

# ▷ key 인자를 정하지 않은 기본적인 sort에선, 튜플 순서대로 우선순위 기본 할당
c = sorted(a, key = lambda x : x[0])  # 첫번째로 기준으로 정렬

c = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]

d = sorted(a, key = lambda x : x[1])  # 두번째 기준으로 정렬

d = [(3, 0), (5, 1), (0, 1), (1, 2), (5, 2)]

