### Operators
- Special symbols, performs on variables and Values.
- There are lots of operators type on python:
-> *Arithmetic, Assignment, Comparison, Logical, Bitwise, and Special Operators*
**A**. **Arithmetic Operator**: simple mathematics operators`( +, -, *, /, **, % ).`
     - Inputs have to be in *int, eval, float* only.
**B. Assignment Operator (a == b)**:
   - Addition assignment (a+=b)
   - Remainder assignment (a %= b )
   - Division assignment (a /= b)
   - Exponential assignment `(a **= b)`
**C. Comparison Operator**: to compare variables and returns boolean values (True or False).
          **Operators**: `( ==, !=, >, <, >=, <= )`
          **Eg**.   `print("a > b", a>b)`
**D. Logical operators**: checks if T or F.
          **Operators**: And(`and`), Or( or ), Not(`not`)
          **Eg**.
```
              a = 2
              b = 3
              c = a<b and a>b           # T  and  F`
              print(c)                  # prints:  False
              print(not(c))             # makes negate then print:   True
```
**E. Bitwise operators**: for binary values(bits)-  True(1) and False(0)
         NB.  `bin(x)`     ...gives the binary value of x.
         Eg.   `print(bin(10))`   `#prints: 0b1010`    so, the binary value of 10 is 1010.
         NB.   To reverse use:  `int('bit', 2)` - prints the Decimal number.
         Eg.   `print(int('1010', 2))`   `#prints: 10`
    **Operators**: complement/Not( ~ ), And( & ), Or( | ), Xor( ^ ), Leftshift( << ), Rightshift( >> )
    **Eg**.
```
          print(~12)          # -(12 + 1) = -13   then prints:  -13
          print(~4)           # -(4 + 1) = -5,    prints:  -5
          
          print(10 & 7)       # 1010
                              & 0111
                   Then Prints: 0010 = 2    so prints: 2 
                   
         print(10 | 7)        # 1010
                              | 0111
                   Then Prints: 1111 = 15   so prints: 15
                   
         print(10 ^ 7)        # 1010
                              ^ 0111
                   Then Prints: 1101 = 13   so prints: 13
```
        NB.  For Xor( ^ ), 1^1 == 0  and  0^0 == 0,  else 1.
    NB. Every number has zeroes at the right.   eg,  1010.0000
    eg.   `print(10 << 2)`    # 1010.0000 shifts 2 zeroes to the left: 101000=40. then prints: 40.
        `print(10 >> 2)`    # 1010 shifts two zeroes to the right:10.10 => 10=2. then prints: 2.
##### Indentation
Ye code geba-weta malet.
- Errors may be doomed, If there is not proper indentation.