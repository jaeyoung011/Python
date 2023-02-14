

def getMyDivisor(n):
    divisorsList = []

    for i in range(1, n + 1):
        if (n % i == 0):
            divisorsList.append(i)

    return divisorsList


def My_solution(left, right):

    sum = 0
    for i in range(left, right+1):
        if len(getMyDivisor(i)) % 2 == 0:
            sum += i
        else:
            sum -= i

    return sum


print(My_solution(13, 17))