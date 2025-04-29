#Object creating
class computer:
    name = ""
    cpu = ""
solace_computer = computer()    # creating object
solace_computer.name = "HP EliteBook"
solace_computer.cpu = "Intel core i5"
feyo_computer = computer()       # creating another object
feyo_computer.name = "HP pavilion"
feyo_computer.cpu = "Intel core i7"
print(f"My {solace_computer.name} has cpu: {solace_computer.cpu}")

#behavior
class computer:
    name = ""
    cpu = ""
    def run(self):  #Keep indentation and 'self' is for declaring objects
         return "BIOS is good!"
solace_cptr = computer()
solace_cptr.name = "HP"
print(f"Runnung: {computer.run(solace_cptr)}")

#Constracture
class computer:
    def __init__(self, name, cpu):
        self.name = name
        self.cpu = cpu
        def run(self):
            return "BIOS is good!"
solace_cptr = computer("Toshiba", "i7") # creating object and givig values
Nathan_cptr = computer("HP", "i5")
print(f"My computer name is: {solace_cptr.name}")
print(f"Nathan's computer cpu is: {Nathan_cptr.cpu}")

#Inheritance
class Animal:
    def eat(self):
        print("I can eat!")
    def sleep(self):
        print("I can sleep!")
class Dog(Animal):
    def bark(self):
        print("I can Bark!")
dog1 = Dog()
dog1.eat()
dog1.bark()

#Encapsulation
class computer:
    def __init__(self, name, cpu):
            self.name = name
            self.cpu = cpu
            self.price = 1000     # Giving the value for attributes
    def setprice(self, birr):
            self.price = birr
feyo_cptr = computer("HP", "core i7")
solace_cptr = computer("Hp", "core i5")
print(f"The value of solace computer: {solace_cptr.price}")    
        # Prints: 1000
solace_cptr.setprice(2000)   # Changing the value of price
print(f"The updated value of my computer is: {solace_cptr.price}")
        # prints: 2000
        