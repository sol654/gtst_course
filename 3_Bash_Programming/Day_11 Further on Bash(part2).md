# Bash Regex

- Use it on `awk`, `sed` and `grep`.
- Eg.  `cat xy.txt | grep "^.*@.*[a-z]\$"`
 **NB**. You have to use escape(`\`) for '$'. in bash and for other special characters in bash.
 - **EXAMPLE**: number checker

- We use double brackets for our conditions.
- We use `=~` for regex to check with if condition statement. 
```
  #! /bin/bash
  read -p "Enter number: " num
  pattern="[0-9]"     #Checks if pattern is bn 0-9...
  if [[$num =~ ${pattern}]]
  then
  echo "good number!"
  else
  echo "Please enter number only!"
  fi
```
- EX2:  Email validator
```
 #! /bin/bash
 read -p "Enter email: " email
 pattern="^.*@[a-z]\.(com|net)\$"
 if [[$email =~ $pattern]]
 then
 echo "Valid email..."
 else
 echo "Invalid email..."
 fi
```
## Else If (elif)

- Like python "`elif`" -we can use elif in bash.
**Syntax**: 
```
if condition
then
   body
elif condition
then
   body
else
   body
fi

```
**Example**:
```
a=23
if [$a -gt 23]
then
echo "Greater..."
elif [$a -lt 23]
then
echo "Less..."
else
echo "Equal..."
fi
```
# Loop in Bash

- **For loop, while loop, until loop and Select loop**.
## For Loop
**Syntax**:
```
for condition
do
   body
done
```
**Example**:
```
for num in {1..10}        #list of number 1,2,3...10
do
echo num     # displays the whole numbers bn 1-10 vertically.
done
```
Eg, Display array..
```
arr=("list1" "list2" "list3" "list4")
for a in ${arr[@]}
do
echo a      #displays vertically
done
```
EG2:
```
txt="Hello there my name is Solomon Tesfaye."
for i in $txt
do
echo i     # Prints each word(not leter) vertically..
done
```

### For loop without sequence data
EG:
```
for ((i=1; i<=10; i++))
do
echo $i
done
```
**NB**. In (( ))-double bracket, you don't need '$' for variables.
### Slicing in Bash
**NB**.  slicing in bash eg, `{1..10..1}` is equal to slicing in python `[1:10:1]`.
**Example**:
```
for num in {1..10..1}
do
echo $num
done
```
EG2:
for num in {10..0..-2}
do
echo $num
done
## While Loop
**Syntax**:
```
while [expression]
do
   body
done
```
**EG2**: Script to get specified numbers.
```
#! /bin/bash
read -p "Enter Starting number: " snum
read -p "Enter ending number: " enum
while [[$snum -eq $enum]]
do
echo $snum
((snum++))
done

echo "This is the sequence that you want."
```

### Infinite Loop
EG:
```
while :
echo "Welcome infinitely"
done
```
### Terminate Example
```
echo "Count down for website launching"
i=10
while [$i -ge 1]
do
if [$i == 2]
then
echo "Mission abborted..."
break
fi
echo $i
((i--))
done
```
## Continue Statement
- Jumps from some condition.
- Its python equivalent is called: `pass`
**EXAMPLE**:
```
#! /bin/bash
i=0
while [$i -le 10]
do
if [[$i == 5]]
then
echo "Jumps number 5.."
continue
fi
echo "Current number is $i."
done
```

## Until Loop
- Opposite of while loop, because stops the loop when the expression becomes true. 
- **NB**. If "False" then continue to the body and when "True" stops the iteration.
**Syntax**:
```
until [Expression]
do 
   dody
done
```
**Example**:
```
i=0
until [$i -gt 10]     # Until it becomes true, it will continue.
do
echo $i
done
```
## Select Loop
- Creating a simple menu (choise).
- `PS3` - variable, used for set the prompt for user input.
- `esac` - used to close the `case`.
**Syntax**:
```
select var in list
do
   commands of select
done
```
**Example**:
```
#! /bin/bash
PS3="Select the fruit: "
select fruit in "Mango" "Apple" "Banana" "Exit"
do
	case $fruit in 
		"Mango")
			echo "You selected Mango."
		;;
		"Apple")
			echo "You selected Apple."
		;;
		"Banana")
			echo "You selected Banana."
		;;
		"Exit")
			echo "Bye Bye!!."
			break
		;;
		*)
			echo "Invalid Input."
		;;
    esac
done
```
**EG2**: Select the number and check it odd or even.
```
#! /bin/bash
PS3="Enter number bn 1-9."
select num in 
do
	case $num in 1 2 3 4 5 6 7 8 9
		1|3|5|7|9)
			echo "The number is Odd."
			;;
		2|4|6|8)
				echo "The number id Even."
				;;
		*)
			echo "Invalid input."
			break
			;;
	esac
done
```
## Function
**NB**. If you use Arguments $1, $2....$9 you can use $? to call the return value.
- **Syntax**:
```
function_name( ){
  body
}
function name
```
**Example**:
```
Add(){
return $(($1+$2))
}
Add 3 4   # calling the function
echo "The sum: $?"    # calling the return value
```
**EG2**:
```
Add(){
sum=$(($1+$2))
echo "The sum: $sum"
}
Add 3 4
```
## Bash and Linux

**NB**. You can run Bash codes in 1 line.
Eg.
```
for i in {1..5}
do
echo "Hello $i"
done
```
This code can be written as:
```
for i in {1..5} do echo " Hello $i" done
```
**NB**. You can use linux commands in bash file.

EXAMPLE:
```
#! /bin/bash
ls -l
```

```
#! /bin/bash
echo *     # works as ls(display all files in current directory).
```

```
#! /bin/bash
apt update
```
### Interaction with Linux
**NB**. To use in bash commands our to terminal, we must change the shell type to **Bash**. then use commands:  `>   echo *`  ..type in linux terminal, it displays all files and folders in that current directory. but to arrange the lists use loop:   `for i in *; do echo $i; done`
- **NB**.  `pwd == echo $PWD`

**Eg.**   `for i in {1..5}; do echo $i; done`    ..displays 1-5 numbers vertically.
- **Best Example**. let say in our linux directory there are files ..(`ls`):  homefile namefile officefile schoolfile   
-To rename them we can use: `mv`   therefore
```
for i in *; do mv $i old_$i; done
```
Therefore the output will be:
- ls:  old_homefile  old_namefile  old_officefile  old_schoolfile

