class A :
    def __init__(self,x):
        n=int(input("enter value in n :"))
        for i in range(1,n+1):
            if (n%i==0):
                print(i)
obj=A(2)