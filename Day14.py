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
number=int(input("Enter the number:"))
def fib(num):
    if num<=1:
        return num
    else:
        return fib(num-1)+fib(num-2)
print(fib(number))    

