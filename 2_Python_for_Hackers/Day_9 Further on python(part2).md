# OOP in Python

**Object**: has action and name.
- has attribute(properties) and methods(behaviors, actions or functions).
Eg.  **Our computer**:  has Attributes(cpu, name, RAM..) and behaviors(play music, Run Game...).

**Class**: is a blue print for objects.
**Syntax**:
```
class class_name:    #Class name starts with capital mostly, not always
      #create attributes
obj = class_name()
obj.attribute = value
```
       
Eg.
```
    class computer:
         name = ""
         cpu = ""
    solace_computer = computer()    # creating object
    solace_computer.name = "HP EliteBook"
    solace_computer.cpu = "Intel core i5"
    feyo.computer = computer()       # creating another object
    feyo.computer.name = "HP pavilion"
    feyo.computer.cpu = "Intel core i7"
    print(f"My {solace_computer.name} has cpu: {solace_computer.cpu}")
```

# Giving Behaviors

-  **Giving Behaviors == Creating Methods**
- methods are functions in oop.
Eg.
```
class computer:
    name = ""
    cpu = ""
    def run(self):  #Keep indentation and 'self' is for declaring objects
         return "BIOS is good!"
solace_cptr = computer()
solace_cptr.name = "HP"
print(f"Runnung: {computer.run(solace_cptr)}")
```
# Python constructors
- We can initialize values using **constructors**.
- Here, constructor method:  `__init__(self, variables)`
Eg.
```
    class Bike:
         def __init__(self, name)
               self.name = name
    bike1 = Bike("Mountain Bike")
```
    
eg2.
```
    class computer:
         def __init__(self, name, cpu):
                self.name = name
                self.cpu = cpu
        def run(self):
                return "BIOS is good!"
    solace_cptr = computer("Toshiba", "i7") # creating object and givig values
    Nathan_cptr = computer("HP", "i5")
    print(f"My computer name is: {solace_cptr,name}")
    print(f"Nathan's computer cpu is: {Nathan_cptr.cpu}")
```
# Inheritance in python

**syntax**:
```
    class Old_class:
           # Attributes and behaviors
    class New_class(Old_class)
           # Attributes and behaviors
```

**Eg**.
```
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
```
# Encapsulation in Python

- Bundling attributes and methods inside a single class.
- To change values of attributes and methods.

**Eg**.
```
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
    solace_cptr.setprice(2000)`   `# Changing the value of price
    print(f"The value of solace computer is: {solace_cptr.price}")
           # prints: 2000
```

# Package installation
- To use installed packages in our code: `import package_name`
Eg. 
```
    import sys
    x = sys.argv[2]
```

- In our VScode terminal ('ctrl+j'), we can install packages:
  Eg.   `pip install sys` 
then, we can use the package by importing.
