# -*- coding: utf-8 -*-

from itertools import combinations

def My_solution(n): # sum > 15 : break -> 안해주면 시간 초과로 실패했다.

    count = 0
    for i in range(1, n+1):
        sum = 0
        for j in range(i,n+1):
            sum += j
            if sum == n:
                count += 1
                break
            elif sum > n+1:
                break

    return count

print(My_solution(15))