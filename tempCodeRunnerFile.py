def pal(a):
    if len(a)==1:
        print("its a plindrom")
    else:
        if a[0]==a[-1]:
            pal(a[1:-1])
        else:
            print("its not a plaindrom")
#num=input("Enter the string : ")
pal("Usama")
pal("maam")            
