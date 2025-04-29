
### Function
- A block of code, performs a single task.
- divide a complex problem in to smaller chunks.
EG.  To create a blue circle you can use two functions:
    - coloring function and
    - circle function
**NB**. so, you have to use **DRY** rule(don't repeat yourself).
#### Function Types(two)
1. **Standard library functions**: builtin functions.   eg.  *print(), len(), input()*
2. **User-defined functions**: create our own functions.
- To **create a function** we use a keyword "`def`".
**syntax**:
```
        def fun_name():
            # Function body
```
Eg.
```
     def great():
         print("Hello World!")
```
- To **call the function** use:   "`fun_name(arguments)`"
Eg.    `great()`

**Eg1**.
```
    def sol():      # create a function
         print("I'm solace.")
    def xy():
         print("My name is xy.")
     sol()
     xy()
```
#### Function Arguments
Eg.
```
    def add_num(num1 = 1, num2 = 3):
          sum = num1 + num2
          print(sum)
    def add_numbers(num1, num2):
         sum = num1 + num2
         print(sum)
    add_num()                # prints: 4
    add_numbers(5, 6)        # prints: 11
```
    
Eg1.
```
    def user(fname, lname):
           print(f"Hello {fname} {lname}!")
     def display(age):
           print(f"You are {age} years old!")
     fname = input("Enter firstName: ")
     lname = input("Enter lastName: ") 
     age = input("Enter your age: ")
     user(fname, lname)
     display(age)
```

#### Return statement
```
def sol(num1, num2):
     sum = num1 + num2
     return(sum)
print(sol(10, 20))
```
#### Recursion
- Calling the function itself in its own function.
- Defining something in terms of itself.
**Syntax**:
```
      def recurse():
          recurse()    # recursive call
```
         
**Eg**.
```
    def factorial(x):
        if x == 1:
            return 1
        else:
            return x * factorial(x-1)     # calling again itself
```

- **Cons of recursion**: complex to understand(memorize),  Takes a lot of memory 
   and They are hard to debug.
### Anonymous / Lambda functions
- If functions have no name.
- For simple codes.  eg,  If the code ends with one line.
**Syntax**:    `lambda argument(s): expression`
**Eg**.
```
    great = lambda : print("Hello World!")
    great()
```
**Eg**2.
```
    numbers = lambda a, b: a+b
    print(numbers(10, 20))
```
    
- To run function taker functions(a function that uses function as argument).
  we use lambda.
#### 1. Filter Function
eg.
```
    def is_even(n):
        return n%2==0
    nums = [3, 2, 6, 8, 4, 2, 9]
    evens = list(filter(is_even, nums))
    print(evens)
```
`# or`
```
      nums = [3, 2, 6, 8, 4, 2, 9]
      evens = list(filter(lambda n: n%2==0, nums))
      print(evens)
```
#### 2. map function
eg1.
```
    nums = [3, 2, 6, 8, 4, 2, 9]
    def doub(n):
          return n*2
    doubles = list(map(doub, nums))
    print(doubles)
```
`# Or` 
```
       nums = [3, 2, 6, 8, 4, 2, 9]
       doubles = list(map(lambda n: n*2, nums))
       print(doubles)
```
#### The append keyword
eg. 
```
    num = []      # frst empty
    num.apend(40):       # added 
```
