
n=int(input("Enter a number: "))
sum=0
for i in range(2):
    digit=n%10 # digit=4
    sum=sum+digit
    n =n//10
print("sum of digits is :", sum)