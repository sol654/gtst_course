## Input Handling

1. **Bash read**

- **read**: is used to accept inputs while the script is running.
**syntax**: `read -p "Text to display" var`    '-p' is to display(prompt)
       `read -sp "Enter password:" var`    '-sp' is silent prompt(hidden texts like password).
       `read -a var`    '-a' is array(list), to accept many values.
eg.
```
>  nano xy.sh

#! /bin/bash
read -p "Enter Name: " name
read -sp "Enter Password: " pw
echo "Hello $name, Your password is: $pw"
```
to run:
```
>   /bin/bash xy.sh
>   Enter Name: solace
>   Enter Password:
>   Hello solace, Your password is: 1234
```
Array Example:
```
>  nano xy.sh

#! /bin/bash
echo "Enter Names of Students: "
read -a names
echo "The first and third students are: ${names[0]} and ${names[2]}."
```
to run give +x permission then:
```
>  ./xy.sh
>  Enter Names of Students: 
>  Sol Feye Anuzi Johnson Nicola
>  The first and third students are: Sol and Anuzi.
```

2. **Arguments**
- You can use $1, $2, $3.....$9 to accept the inputs.
- before running the code.
- **NB**. `$0` holds file name here.
Eg.
```
> nano xx.sh

#! /bin/bash
echo "Hi $1 Your father name is $2. yeah?"
```
to run this:
```
>  /bin/bash xx.sh Solace Tesfaye
>  Hi Solace Your father name is Tesfaye. yeah?
```
## Comments
"`#`"    ..for single line comment.
```
<<COMMENTS
...multiple lines of comment...
COMMENTS
```
### Bash Sleep
- To make slow (a good waiting) on our Script.
Eg.
```
#! /bin/bash
echo "Let me think your name for 3 seconds."
sleep 3s            # waits 3seconds to display the next.
echo "I got it! Your name is: solace"
```
## Operations
- For mathematical operation use: `$(( epression ))`
Eg.
```
#! /bin/bash
a=3
b=4
echo  "sum = $((a+b))"
```
**A**. **Arithmetic Operations**
- `( +, -, *, /, %, **)`
**B. Assignment Operators**
- Increment: `let "a+=3"`
- Decrement: `let "a-=3"`
- Multiply:  `let "a*=4"`
- Divide:  `let "a/=5"`
Eg.
```
x=10
y=6
z=0
let "z=$((x+y))"
echo "Add = $z"
```
**C. Comparison**
- **Alphabetic Comparison** and **Sign Comparison**.
- **Sign Comparison**:` (>, <, >=, <=, !=, ==)`
- **Alphabetic Comparison**:
  -Greater than: `-gt`
  -Less Than:  `-lt`
  -Greater than and equal to: `-ge`
  -Less than and equal to:  `-le`
  -Equal:  `-eq`
  -Not equal:  `-ne`
## If..else Conditions
- In Bash there is no indentation, in place of indentaton we use: `then`
- Bash if..else has close tag:  `fi`
**syntax**:
```
#! /bin/bash
if [condition]
then
..body..
else
..body..
fi
```
**NB**. `[condition]` is for Alphabetic conditions and Strings.  So for numeric (symbolic) comparisons use double circle bracket: `(( conditions ))`
Examples for square bracket:
```
#! /bin/bash
if [2 -gt 1]     # you used alphabetic here
then
echo "Hii"
else
echo "bye"
fi
```

```
#! /bin/bash
Name="Nat"
if ["$Name" = "Nathan"]
then
echo "Hi Nathan."
else
echo "Not Nathan."
fi
```

```
#! /bin/bash
read -sp "Enter password" pw
if ["$pw" = "1234"]     # you used alphabetic here
then
echo "Correct!!"
else
echo "Incorrect!!"
fi
```

Examples for double circle brackets;
```
#! /bin/bash
if ((2>1))     # you used symbolic comparison here
then
echo "Hii"
else
echo "bye"
fi
```

```
#! /bin/bash

read -p "Enter Numbers: " Num
echo
if (( "$((Num % 2))" == 0 ))
then
echo "Even."
else
echo "Not even."
fi
```
## Nested If:
```
#! /bin/bash

if [$1 -gt 50]
then
echo "Number is > 50."
if (( "$(($1 % 2))" == 0 ))
then
echo " and it is Even"
fi
fi
```
## If_else for logical operators eg:
```

#! /bin/bash
if[[10 -eq  10 && 5 -gt 4 || 3 -eq 4 || 6 -lt 7]]
then 
echo "Condition is True!!"
fi
```
