#1
import random
num = random.randint(1, 5)
while True:
    try:
        guessing = int(input("Enter your guss from 1-5: "))
        if guessing == num:
            print("Congrats!! You got it!")
            break
        else:
            print("guessing not match! please try again!")
    except:
        print("your input is not number or not valid! Try again!")

#2
number = int(input("Enter number: "))
sum = 0
while number >= 1:
    sum = sum + 1
    number = number / 10
print(f"The digit of the number is: {sum}")
