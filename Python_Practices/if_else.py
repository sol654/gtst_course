#1.
var = input("Enter a number: ")
if var.isdigit():
    num = int(var)
    if num %2 ==0:
        print("Even")
    else:
        print("Odd")
elif var == "":
    print("Nothing entered!")
else:
    print("Invalid! please enter number!")

#2
num = int(input("Enter an integer: "))
if num > 0:
    print("Positive number.")
elif num == 0:
    print("Zero.")
else:
    print("Negative number.")

#3
score = float(input("Enter your score: "))
if score >= 80:
    print("you got 'A'")
elif score >= 65:
    print("You got 'B'")
elif score >= 50:
    print("You got 'C'")
else:
    print("You're failed!")

#4
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 > num2 and num3:
    print(f"The largest numbet is {num1}")
elif num2 > num1 and num3:
    print(f"The largest number is {num2}")
else:
    print(f"The largest number is {num3}")