

def My_solution(a, b, n):

    sum = 0
    remainder = 0
    while n >= a:

        rest = n // a
        remainder_num = n % a
        remainder += remainder_num
        sum += (rest) * b
        n = n // a


        if remainder != 0:
            n += 1
            remainder = 0
    return sum


print(My_solution(2, 1, 20)) # Test_case 맨밑에 2개뺴고 실패