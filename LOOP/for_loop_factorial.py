#print factorial of a number using for loop
n=int(input("enter a number: "))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print("factorial of",n,"is",factorial)
        