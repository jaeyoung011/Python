#
#
# def to_notation(n, q):
#     rev_base = ''
#
#     while n > 0:
#         n, mod = divmod(n, q)
#         rev_base += str(mod)
#
#     return rev_base[::-1]

# 진법 뭔지몰라서...어렵.. 다시 풀어봐야할듯..
def solution(n):
    result = ''
    while n:
        result += str(n%3)
        n=n//3
    return int(result,3)

print(solution(45))