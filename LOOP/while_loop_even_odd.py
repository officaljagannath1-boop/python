print("enter value in  i and n to print even and odd numbers i to n")
i=int(input("Enter i: "))
n=int(input("Enter n: "))
while i<=n:
    if i%2==0:
        print(i,"is even")
    else:
        print(i,"is odd")
    i+=1