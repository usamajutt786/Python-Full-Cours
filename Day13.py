#Multiple funtoin or funtions in funtions
def even():
 return "Even"
def odd():
 return "Odd"

    
def funinfun(number):
  if number%2==0:
      return even()
  else:
      return odd()
x=funinfun(9)  
print(x)