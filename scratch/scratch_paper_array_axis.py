# -*- coding:utf-8 -*-
import os
from util import path_util
from util import csv_util
from util import path_util
from util import pickle_util

from data_preprocessing.batch import make_train_set_batch
from batch_process import batch_train
from batch_process import batch_evaluate





# clsf_path = path_util.ClsfPath('CPC_C01')
# standard_csv_path = clsf_path.standard_csv_path()  # 01.csv
# patent_cnt = csv_util.read_csv_to_list(standard_csv_path, [0,1,2,3])
#
# # patent_cnt = csv_util.read_csv_to_list(standard_csv_path, [0,1,2,3])
#
# print(patent_cnt)

# clsf_path = path_util.ClsfPath('CPC_C01')
# valid_dataset = clsf_path.valid_dataset_pkl_path()
# _, _, skey_list = pickle_util.load_object(valid_dataset)
# valid_cnt = len(skey_list)
# print(valid_cnt)


# pjt_path  = [1,2,3,4]
# pjt_path = pjt_path[:-1]
#
# print(pjt_path)


#
# name = ''
# for i in ['hello', 'world', 'I', 'am' , 'groottt']:
#     name += '{} '.format(i)
#
# print(type(name))
# print(name)



# # preprocessing_train_06
#
# string = "word1 word2 word3    word4    "
# print(string.split()) # split()은 공백이 1개이건 2개이건 n개이건 상관없이 무조건 1개로 보고 처리 + "\t", "\n" 도 처리해줌
# print(string.split(" ")) # 은 공백 1개, 1개를 각각의 공백으로 따로따로 처리합니다.


from util import pickle_util

# # f'' {} {} 나타내기
# year = 2016
# event = 'Referendum'
# print(f'Results of the {year} {event}')


# import pandas as pd
# test_columns = pd.DataFrame({ "bid_id": [1, 2, 3], "bidder_id": ["Gadi", "Conda", "Lion"],
#                               "city": ["Seoul", "LA", "Sydney"], "item": ["TV", "jewelry", "book"]}).set_index("bid_id")
#
#
#
# print(test_columns.iloc[:, 1:-1])

# import numpy as np
# #np.sum & argmax
# import numpy as np
# x = np.array([
#     [ 1,  2,  13,  4],
#     [ 5,  16,  7,  8],
#     [ 19, 10, 11, 12],
# ])
#
#
# print(np.sum(x, axis=0))
# print(np.argmax(x, axis=1))



# axis = 0 ,  axis = 1

# axis=0은 각 열(row)의 모든 행(column)에 대해 동작한다. 진행방향 세로. 결과값이 행으로 나타남.
#
# axis=1은 각 행(column)의 모든 열(row)에 대해 동작한다. 진행방향 가로. 결과값이 열로 나타남

# summation_result = np.sum(total_result, axis=0)  # 각 열의 모든행에대해 더해라(axis=0 행을 뜻)
# y_summation = np.argmax(summation_result, axis=1)  # 각 행의 모든 열에대한 인덱스를 가져와라 (axis = 1 열을 뜻)
# summation_acc = np.sum(t == y_summation) / len(t)
# print("summation_acc : ", summation_acc)
#
# # weighting
# weighting_result = np.sum(total_weighting_result, axis=0)  # 각 열의 모든 행에 대해서 더해라 (total_weighting_result.shpae(x,y)
# # total_weighting_result.shape(x,y) => axis=0 => x,y 행렬에서 x 라고 생각하면 된다.
# # 진행방향은 반대라고 생각하는게 마음이 편하다.
# y_weighting = np.argmax(weighting_result, axis=1)  # 각 행의 모든 열에 대해서 최대 인덱스 값을 가져와라
# # total_weighting_result.shape(x,y) => axis=0 => x,y 행렬에서 y



