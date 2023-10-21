# #Recursion 

# def multiply( a, b):
#     if a==1:
#         return b
#     else:
#         return (b+multiply(a-1,b))
    
# print(multiply(2,3))

#factirial of number

# number=int(input("Enter The Number:"))
# def fac(num):
#     if num==1:
#         return 1
#     else:
#         return num*fac(num-1)
    
# print(fac(number))    
# number=int(input("Enter the number:"))
# def fib(num):
#     if num<=1:
#         return num
#     else:
#         return fib(num-1)+fib(num-2)
# print(fib(number))    

#checking number for palindrom

def pal(a):
    if len(a)<=1:
        print("its a plindrom")
    else:
        if a[0]==a[-1]:
            pal(a[1:-1])
        else:
            print("its not a plaindrom")
#num=input("Enter the string : ")
pal("Usama")
pal("maam")            


