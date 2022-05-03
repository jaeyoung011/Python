def solution(n):
    n = str(n)
    n_list = list(n)
    n_int = []
    for i in n_list:
        n_int.append(int(i))
    # 위에 for 문을
    # list(map(str,n)) 으로도 가능 하다
    # map 을 잘쓰는게 좋다.

    n_sort = sorted(n_int, reverse=True)
    n_sort = list(map(str, n_sort))
    result = ''.join(n_sort)
    result = int(result)

    return result






print(solution(118372))
# 873211 이런느낌


# 다른 풀이들

def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))

