

def find_k(array, commands):
    # anw1 = []
    # anw2 = []
    # anw3 = []
    result = []
    for i in range(len(commands)):
        anw = []
        anw.append( array[commands[i][0] -1 :commands[i][1]] )

        anw = sorted(anw[0])

        result.append(anw[commands[i][2] - 1])

    return result


print(find_k([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))


# 다른 사람 풀이


def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


