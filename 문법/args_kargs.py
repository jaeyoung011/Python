# coding:utf-8
#



def param_test(a, b, *args, **kargs):
    print(a)
    print(b)
    print(args)
    print(kargs)



if __name__ == '__main__':
    param_test(1, 2, 3, 4 ,c=3, d=4)

# args 는 튜플 형태로 나타나난다
# kargs 는 딕셔너리 형태로 나타난다

# class 에서 상속을할때 다른것을 어떻게 처리하는지에 따라 args, kargs를 써주면 되는것이다.
