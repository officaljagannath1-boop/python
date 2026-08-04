pn=int(input("enter your phone number : +91"))
if(pn>=1000000000 and pn<=9999999999):
    print("valid phone number")
    np=input("enter alphabet and unicode symbol to create strong password : ")
    cp=input("confirm password : ")
    while(np!=cp):
        print("password not matched try again")
        np=input("enter alphabet and unicode symbol to create strong password : ")
        cp=input("confirm password : ")
    if(np==cp):
        print("password created successfully remember your password ",np) 
        
        name=input("enter your name : ")
        email=input("enter your email : ")
        
    else:
        print("something went wrong try please again")
else:
    print("invalid phone number")