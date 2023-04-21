"""
# 풀이과정
1) 단어 정렬을 이용해서 같은 단어로 만들어준다

2) 같은단어들은 제거해준다

3) 그거의 길이를 구해준다

"""




def main():

    N = int(input())
    words = [str(input()) for word in range(N)]

    new_list = [''.join(sorted(word)) for word in words]
    group = set(new_list)

    print(len(group))


if __name__=='__main__':
    main()

