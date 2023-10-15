#Alising 
#one or more variables pointing at the same memory loaction is callex alising 
a=5
b=a
c=b
print(id(a))
print(id(b))
print(id(c))

#reference couting 
#How many variables are pointing at the same point is called reference counting 
#it can be calculate like   sys.getrefcount(a) but it is not working on my PC


#Garbage collection 
#When all varibles point to the same address are deleted the the garbage value left at that
#posisiton called garbage collection 

#Mutability 
#Mutability in Python refers to the property of an object that determines whether it
#an be changed after it is created.

