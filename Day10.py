def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

def calculate(operation, a, b):
  if operation == "+":
    return add(a, b)
  elif operation == "-":
    return subtract(a, b)
  elif operation == "*":
    return multiply(a, b)
  elif operation == "/":
    return divide(a, b)
  else:
    raise ValueError("Invalid operation")

# Get the user's input
operation = input("Enter an operation (+, -, *, or /): ")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Calculate the result
result = calculate(operation, a, b)

# Print the result
print(f"{a} {operation} {b} = {result}")
