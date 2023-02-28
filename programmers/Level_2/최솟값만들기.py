# -*- coding: utf-8 -*-

def My_solution(A,B):

    A_min = sorted(A, reverse=False)
    B_max = sorted(B, reverse=True)

    sum = 0
    for i in range(len(A)):
        sum += (A_min[i] * B_max[i])
    return sum


print(My_solution([1,4,2] , [5,4 ,4]))

# 다른 간단한 다른사람 풀이

def getMinSum(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])
