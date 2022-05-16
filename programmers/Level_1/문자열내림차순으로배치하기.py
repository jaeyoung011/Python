import string

def solution(s):
    slist = list(map(str,s))

    lower = []
    upper = []
    for i in slist:
        if i in string.ascii_lowercase:
            lower.append(i)
        else:
            upper.append(i)
    lower = sorted(lower, reverse=True)
    upper = sorted(upper, reverse=True)

    answer = lower + upper
    return ''.join(answer)

print(solution('Zbcdefg'))