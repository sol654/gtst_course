#### If-else statement
- In python there are three types of *if...else* statements.
1. if
2. if...else
3. if...elif...else
**syntax**:
```
    if condition:
        # Body of statement.
```
	Eg.
```
	    num = 10
	    if num > 0:
		    print("Number is positive.")    # Needs indentation.
```
**NB**. If you use ':',  python indents by default. or To indent click "TAB" key.
- If there is no indentation, It is not in if condition
Eg.
```
if a == b:
    print("True")     # will be checked by if statement.
print("not from if statement.")   # will not be checked by the if statement.
```
#### If....else
Eg.
```
    if 10>9:
         print("True")
    else:
         print("False")
    print("not indented.")
```
**Output**:
```
        True
        not indented
```
#### If....elif....else
- used to increase the conditions. like ...elseif... in c++.
Eg.
```
    if num > 0:
         print("positive")
    elif num == 0:
         print("Zero")
    else:
         print("Negative")
```
### Nasted if statement
**syntax**:
```
       if condition1:
           # statement(s)
           if condition2:          # Inner if statement
              # statement(s)
```
**Eg**:
```
    num = 5
    if num >= 0:
        if num == 0:
            print("Zero")
         else:
            print("Positive")
    else:
        print("Negative")
```
        
###### The function  "`.isdigit()`" checks if input is number.
**Eg**.
```
      num = input("Enter number: ")
      if num.isdigit():
         print("Yes number!")
      elif num == "":
         print("Nothing entered!")
```
### Logical Errors(Exceptions)
- **IndexError**: error related with incorrect indexing.
- **ZeroDivisionError**: number divided by zero.
- **NameError**: incorrect naming of keywords.
- **IndentationError**: related with indentation.
- **ValueError**: related with incorrect input type.     ...ETC...
#### Error Handling
**syntax**:
```
	try:
	    # code that may cause exception.
	except:
	     # code to run, when exception occurs
```
**Eg**.
```
    try:
        num = 10
        deno = 0
        result = num/deno
        print(result)
    except:
        print("denomenator can not be zero(0).")
```
**Eg2**.
```
     try:
        list = [1, 2, 3, 4]
        num = 10
        deno = 0
        print(num/deno)     # number cannot be devided by zero
        print(list[10])      # 10 is out of range of index of list
     except ZeroDivisonError:
        print("Number can not be divided by zero.")
    except IndexError:
        print("The index is out of bound.")
```
### Python loops
- **For loop**
- **While loop**
##### For Loop
**syntax**:
```
     for val in sequence:
        # statement(s)
```
NB. *val* holds the iteration from sequence.  *sequence* represents list, tuple, string and range. 

**Eg**.
```
    languages = ["python", "swift", "java", "go"]
    for language in languages:
         print(language)       # Displays the whole languages list
```
          
**Keywords: "range" and "len"**
"**range**": holds the range from *zero* up to the *number-1*.
"**len**": length of sequence(elements number).
**Eg**.
```
    numbers = range(5)
    print(numbers)       #prints: range(0, 5)
    for i in numbers:
	    print(i)`        #prints:  0, 1, 2, 3, 4, 5
```
Eg2.   
```
     number = int(input("Enter number: "))
     for i in range(number):
	     print(f"{i} * {number} = {i *number}")
```
Eg.
```
    a = (1, 2, 3, 4, 5, 'Hello')
    print(len(a))           # prints: 6
    for i in range(len(a)):
        print(i)            # prints: 0, 1, 2, 3, 4, 5
```
#### While loop
Eg.
```
    i = 1
    n = 5
    while i <= n:
        print(i)
        i = i+1
```
**Infinite loop: 'True'**
Eg.
```
     while True:
        print("solace")    # prints: solace  ...infinite times
```
**NB**.   **For loop**: usually when interaction of numbers is known, 
but, **while loop**: is usually used when the number of interactions are unknown.
NB. You can use "`break`" to terminate the infinite loop.
Eg.
```
    while True:
        print("solace")
        break
    # the output will be one "solace" only.
```

**Ex.** Make a right ange triangle using for loop.
```
		*
		**
		***
		****
		*****
```
**Code**:
```
   num = 5
   for i in range(1, 6):
       print("*"*i)
```
       