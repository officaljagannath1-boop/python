def buzz():
    n=int(input("Enter a number: "))
    if n%7==0 or n%10==7:
         print(n,"is a buzz number")
    else:        print(n,"is not a buzz number")
    
buzz()