    #no need to close the file when we use with as f

with open ("jp.txt","a+") as f:
    st=input("write data in jp.txt file :")
    f.write("\t"+st)
    f.seek(0)# move the file pointer to the beginning
    print(f.read())