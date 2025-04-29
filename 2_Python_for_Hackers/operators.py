#1. Arithemetic and 2.Assignment Operators
a = 3
b = 4
c = a ** b
print("The power of a^b = ", c)
c = a % b
print("The Remainder a%b = ", c)
c = a / b
print("The Devision a/b = ", c)

#3. Comparison Operators
print("a > b", a>b)
print("a != b", a!=b)

#4. Logical Operators
c = a<b and a>b 
print("Print about 'and' :", c)
c = (a<b) or (a>b)
print("Print about 'or' :", c)
print("About 'not' :", not(c))

#5. Bitwise Operators
print(~12)    # -(12+1)
print(~4)     # -(4+1)
print(10 & 7)  # 1010 & 0111 = 0010 = 2
print(10 | 7)   #1010 | 0111 = 1111 = 15
print(10 ^ 7)   #prints Xor(^) 1010 ^ 0111 = 1101 = 13
print(10<<2)    #101000 = 40
print(10>>2)    #10.10  = 10 = 2

