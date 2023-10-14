#Edting and deleting string in python 
#it is not possible to edit or delete the string in python 
#OPeratiions on string 
s1="Hello" 
s2="World"
print(s1+" "+s2)

print(s1==s2)

print(s1<s2)

print(s1>s2)

print("H" in s1)

for i in s1:
    print(i)
#use string in loop
en=int(input("Enter the number"))
for i in range(1,11):
    result=i*en
    print(i,"x",en,"=", i*en)