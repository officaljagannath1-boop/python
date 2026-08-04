class A :
    a=int(input("enter value in a :"))
    b=int(input("enter value in b :"))
    c=int(input("enter value in c :"))
    d=int(input("enter value in d :"))
    e=int(input("enter value in e :"))
    def __init__(self):
        av=A.a+A.b+A.c+A.d+A.e/5
        print(av)
obj=A()