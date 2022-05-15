def solution(s):
    to_list = list(map(str, s))

    if len(to_list) !=4 and len(to_list) != 6:
        return False
    else:
        for i in to_list:
            if i not in ['0','1','2','3','4','5','6','7','8','9']:
                return False
        return True

print(solution("1234"))



# not in 을 써주는게 훨씬 깔끔해 보인다
def solution(s):
    to_list = list(map(str, s))

    if len(to_list) not in [4,6]:
        return False
    else:
        for i in to_list:
            if i not in ['0','1','2','3','4','5','6','7','8','9']:
                return False
        return True

print(solution("1234a"))