class A :
    y=int(input("enter value in y :"))
    def __init__(self):
        if(A.y%4==0 and A.y%100!=0 or A.y%400==0):
            print(A.y,"= year is  leap year")
        else:
            print(A.y,"not leap year")
obj=A()