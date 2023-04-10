# -*- coding: utf-8 -*-

from itertools import combinations

def manhatten_distance(T1, T2):
    r1, c1 = T1
    r2, c2 = T2
    distance = abs(r1 - r2) + abs(c1 - c2)
    return distance


def coor_plus_1(coor):

    up = [x + y for x, y in zip(coor, [0,1])]
    down = [x + y for x, y in zip(coor, [0, -1])]
    right = [x + y for x, y in zip(coor, [1, 0])]
    left =  [x + y for x, y in zip(coor, [-1, 0])]

    # list3 = [x + y for x, y in zip(list1, list2)]

    return [up,down,right,left]

def patittion_protect(list_coor):

    coor1 = coor_plus_1(list_coor[0])
    coor2 = coor_plus_1(list_coor[1])


    insersectin_list = []
    for i in coor1:
        if i in coor2:
            insersectin_list.append(i)

    return insersectin_list



def to_list(words):

    list_result = [list(i) for i in words]
    return list_result

def maha_to_list(person_coor):
    # mahhanten

    distance_check_list = list(combinations(person_coor, 2))
    return distance_check_list


def main(table):


    # check
    # table = [list(i) for i in table_0]

    table_list = to_list(table)


    # person coordinate
    person_coor = []
    patitions = []
    for x in range(len(table_list)):
        for y in range(len(table_list)):
            if table_list[x][y] == 'P':
                person_coor.append([x,y])
            elif table_list[x][y] == 'X':
                patitions.append([x,y])
    # person check
    if len(person_coor) == 0:
        return 1


    # mahhanten
    distance_check = maha_to_list(person_coor)
    distance_check_list = []
    for i in distance_check:
        T1 = i[0]
        T2 = i[1]
        result = manhatten_distance(T1, T2)
        if result <= 2:
            distance_check_list.append([T1, T2])
        else:
            pass

    # patittion 으로 둘러쌓여있으면 pass
    list_inter = patittion_protect(distance_check_list[0])
    if len(list_inter) == 0:
        return 0
    else:
        pass

    count = 0
    for i in list_inter:
        if i in patitions:
            pass
            count+=1
        else:
            return 0

    if count == len(list_inter):
        return 1



def solution(places):

    result = []
    for i in places:
        answer = main(i)
        result.append(answer)

    return result

############## 위에까지 답으로 ##########
############ 시간 초과 에러


if __name__ == '__main__':

    check = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
     ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
     ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

    result = []
    for i in check:
        answer = main(i)
        result.append(answer)

    print(result)


