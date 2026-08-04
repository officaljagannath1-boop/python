# cheak n is +,-,0 using class and object nested if
class c:
    n=int(input("enter value in n  :"))
    if(n>0):
        print(n,"is positive number")
    elif(n<0):
        print(n,"is negative number")
    else:
        print(n,"is zero")
obj=c()