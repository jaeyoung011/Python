import random

def main():
    N = int(input())

    if 1 <= N <= 100000:
        # ran_list = [random.randint(0,10) for value in range(N)]
        ran_list = list(map(int, input().split()))

        # process_1
        set_list = list(set(ran_list))
        result = sorted(set_list)

        [print(i, end=' ') for i in result]

    else:
        pass



if __name__ == '__main__':
    main()