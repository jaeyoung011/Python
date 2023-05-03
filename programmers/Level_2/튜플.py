# -*- coding: utf-8 -*-


def main(s):
    s = s.replace('{','[').replace('}', ']')
    s = eval(s)
    s.sort(key=len, reverse=False)

    new_lst = []
    for i in s:
        for j in i:
            if len(i) == 1:
                new_lst.append(i[0])
            elif j not in new_lst:
                new_lst.append(j)

    print(new_lst)
    return new_lst


if __name__ == '__main__':

    # main("{{2},{2,1},{2,1,3},{2,1,3,4}}")
    main("{{4,2,3},{3},{2,3,4,1},{2,3}}")
