def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# More operations can be added as needed

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
operation = input("Enter operation (+ or -): ")

if operation == '+':
    print(add(x, y))
elif operation == '-':
    print(subtract(x, y))
else:
    print("Invalid operation")
