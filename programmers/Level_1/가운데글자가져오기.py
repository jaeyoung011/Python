
def solution(s):
    list_s = list(map(str,s))
    if len(list_s) % 2 != 0: # odd
        return list_s[len(list_s)//2]

    else: # even
        mid = list_s[len(list_s)//2-1:len(list_s)//2+1]
        return ''.join(mid)








print(solution('abcde'))
print(solution('qwer'))