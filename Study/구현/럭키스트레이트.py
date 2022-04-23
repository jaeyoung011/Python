

def get_lucky(N):
    mid = len(str(N)) // 2
    left = []
    right = []
    for left_side in range(mid):
        left.append(str(N)[left_side])
    for right_side in range(mid, len(str(N))):
        right.append(str(N)[right_side])

    left_map = map(int, left)
    left_list = list(left_map)
    right_map = map(int, right)
    right_list = list(right_map)

    if sum(left_list) == sum(right_list):
        return 'LUCKY'
    else:
        return 'READY'

print(get_lucky(123402))
