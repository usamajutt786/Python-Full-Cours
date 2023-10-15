#aliasing
#Mean when we assign value of one variable to another variable it will point the same memory 
#location  when we delete the variable the value remain exist because deletion just cancel the 
#references 
a=5
b=a
c=a
print(id(a))
print(id(b))
print(id(c))
del a
print(id(b))

x="Corona"
y=x
z=y
#print(sys.getrefcount(a))
#SystemExit
print("Hello")