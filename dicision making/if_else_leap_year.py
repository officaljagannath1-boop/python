#leap year century using if else

y=int(input("enter year:"))
if(y%400==0):
    print(y," is a leap year")
elif(y%100==0):
    print(y," is not leap year")
elif(y%4==0):
    print(y," is a leap year")
else:
    print(y," is not leap year")
