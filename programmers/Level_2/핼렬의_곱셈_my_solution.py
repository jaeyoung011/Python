# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd


def my_solution(arr1, arr2):

    arr2 = np.transpose(arr2)

    result = []
    for i, v in enumerate(arr1):
        temp = []
        for j , v2 in enumerate(arr2):
            temp.append(int(sum(v*v2)))
        result.append(temp)

    return result












if __name__ == '__main__':
    result = my_solution([[1,4], [3,2], [4,1]] , [[3,3], [3,3]])

    print(result)