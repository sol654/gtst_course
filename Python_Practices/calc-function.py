def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mult(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1 / num2
x = float(input("Enter the First number: "))
y = float(input("Enter the Second number: "))
print(f"Results:\n {x} + {y} = {add(x, y)}\n {x} - {y} = {sub(x, y)}\n {x} X {y} = {mult(x, y)}\n {x} / {y} = {div(x, y)}")
