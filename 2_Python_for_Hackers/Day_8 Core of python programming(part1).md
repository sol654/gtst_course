### Indexing and Slicing
**Indexing**: eg.
```
            lang = ['amharic', 'Eng', 'oro']
            index       0        1      2
    Negative indexing  -3       -2     -1
```
eg.  `print(lang[-1])`        #...prints:  oro
- Calling texting by index is also works for *strings* and *tuples*.
   eg.
```
     name = ('hello', 2, 22)
     print(lang[-3])    #.....prints: hello
```
- For string indexing:
   eg.
```
      name = 'Solomon'
      print(name[0])      #...prints:  S
      print(name[-3])     #...prints:  m
```
#### Slicing
- to access a section by slicing operator ':'
**syntax**:  `myList = [start:stop:step]`
  eg.
```
     name = "No 1 is Nathan"
     print(name[8:14:1])     #...prints: Nathan
```
  - Index counts start from 0.
  NB. When you start with '8' - counts from x, When you stopes at '14' - ends at(with) '13', 
      and The step is:  if the step is '1' , You count the slicing string indexes one by one.
  eg.
```
      name = 'Sol The Best'
      print(name[8:12:1])     #...prints: Best
      print(name[8:12:3])     #..prints:  Bt
      print(name[4:7:2])      #..prints:  Te
      print(name[0::1])       #..prints:  Sol The Best
```
      
eg2.
```
      name = 'No 1 is Nathan'
      print(name[8:14])        #...prints:  Nathan
      print(name[8:])          #...prints:  Nathan
      print(name[8:-1])        #...prints:  Natha
```
#### Slicing for list
eg.
```
name = ['Ehio', 'Banana', 'China', 'Apple']
print(name[::])`       #..prints: ['Ehio', 'Banana', 'China','Apple']
print(name[-1:0:-2])   #..prints: ['Apple', 'Banana']
print(name[-2:-5:-2])  #..prints: ['China','Ethio']
```
**B/c.**
```
    indexing `['Ehio', 'Banana', 'China', 'Apple']`
     normal       0       1         2        3
     negative    -4      -3        -2       -1
       step       1       2         3        4
    -Ve step     -4      -3        -2       -1
```
eg.  `print(name[::-1])`    #..prints:   'Apple', 'China', 'Banana', 'Ehio',
#### User Input Handling
- **Two types of inputes**: by *input function and by argument*.
1. **By Function**: 
    **Syntax**:  `var = input('Text to display: ')`
    Eg.
```
      name = input("Enter your Name: ")
      print(f"Your name is {name}")        # Sol
      print("Your Type: ", type(name))     # Tells the type:  string
```
If you want to change the input type to Integer:
eg.
```
    num = int(input("Enter number: "))    
    print(type(num))       #...prints:  <class INT>
```
**NB**.  Instead of `int()` you can use `float()`, `complex()` or `eval()`.
NB. `eval()` = `int()`
2. **By Argument**: accepts input on command line(Terminal).
            - Enter data before running the code.
        **Syntax**:
```
               import sys
               name sys.argv[1]
               print(f"Hello {name}")
```
            - Accepts only one data. 
             eg.  Sol   not   Sol Tes      ....or use quote "Sol Tes" now it is like a single data.
 - Open CMD line and write:  `python .\xy.py Sol`     ...prints "Sol" ,  .\xy.py is the path with file.
   **Eg**.
```
	 -    import sys
	      num sys.argsv[1]
	      print(f"Your Num = {num}")
```
    - open terminal then write:  `python xy.py 10 11`      ...prints only: 10  b/c the argv is 1.
   If `num sys.argv[2] and  python xy.py 10 11        #....prints: 11`
**Eg**.
```
     import sys
     firstname = sys.argv[1]
     lastname = sys.argv[2]
     print("Hello {firstname}: your Father name is {lastname}")
```
 NB.  If the file path is *C:\Users\Adminstrator\Videos\xy.py* use:  **cd Videos** to get the file to run.
      Then run:  **python xy.py Solomon Tesfaye**
      **Or** use a full path:  `python C:\Users\Administrators\Videos\xy.py sol Tes`
**NB**. To open the Terminal click:  **ctrl + J** 