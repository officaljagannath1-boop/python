####### print prime no i to n using for loop ###  
print ("enter value in i and n to print prime num i to n")
i=int(input("enter value in i :"))
n=int(input("enter value in n :"))
for num in range(i,n+1):
    if num>1:
        for j in range(2,num):
            if num%j==0:
                break
        else:
            print(num)