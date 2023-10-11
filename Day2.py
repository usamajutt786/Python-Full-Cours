import random
 #input vaidation in python
# number=input("Enter a number: ")
# print(number)
# a=input("Enter First Number:")
# b=input("Enter Second Number: ")
# result=int(a)+int(b)
# print(result)
# print("The Result of Two Numbers  is",result)

# list("hello")
# #intendation  a tab space 
# if(a==4):
#     print(" a is 4")
# else:
#         print(" a is not 4")

# #while loop in python
# num=int(input("How many time you want to print hello:"))
# i=0
# while i<num:
#       print("Hello")
#       i+=1

#Gueesing Number...........
counter=0
num=random.randint(1,100);
GuessedNum=int(input("Enter the number you wanna Guess:"))
while GuessedNum!=num:
    counter+=1
    if GuessedNum<num:
        print("Guess Higher")
    else:
        print("guess lower")
    GuessedNum=int(input("Enter the number you wanna Guess:"))

print("You Complete it in ",counter, "Attemps")


