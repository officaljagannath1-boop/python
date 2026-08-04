'''nested if : multiple if statements inside another if statement
 (multple conditions cheak at a time)'''
#cheak no positive or negative usin
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
