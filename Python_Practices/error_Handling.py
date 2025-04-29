#1
try:
    num1 = int(input("Number1: "))
    num2 = int(input("Number2: "))
    result = num1/num2
    print(f"Result = {result}")
except ZeroDivisionError:
    print("Denominator can not be zerro!!")

#2
try:
    num = int(input("Enter Integer: "))
    print("The input is Integer!")
except:
    print("The input is not Integer!")

#3
try:
    list = ['Solace', 'Feyuyk', 'Anusay']
    n = int(input("Enter Index rage between 0-2 : "))
    print(list[n])
except IndexError:
    print("The index is out of range!")