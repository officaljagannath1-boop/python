class A:
    n=int(input("enter value in n  :"))
    s=n*n
    if(n%10==s%10):
         print(n,"is automorphic number")
    else:
         print(n,"is nonatomorphic number")
obj= A()