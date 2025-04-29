## BASH

**Bash**: Bourne Again Shell.
**Script**: holds shell commands
- First bourne shell is *sh*.
### Uses of bash
- Script development 
- Simplifying linux ability
- Automating tasks
- Developing Hacking skill
## Starting with Bash
**Bash**: has extension: '`.sh`' 
Files have executable permissions
Editors: Vscode, nano, VIM, gedit, cherrytree...
*Eg*.  `nano fileName.sh`     or in VScode: New file -> fileName.sh
## Displaying outputs
- Start with **shebang**: `#! /bin/bash`  or `#! /bin/sh`
- Then: `echo "Hello World"` 
- To run:  `/bin/bash fileName.sh`
- or, To run with '`./`' , give file permission to the file: `chmod +x fileName.sh`
  then use:  `./fileName.sh`
Eg.
```
    #! /bin/bash
    echo "Hello world"
    echo "Welcome"
```
Then run:  `./fileName.sh`
If we enter `echo` between two echos, it wil create a new line.
# Variables 
`var_name = 'values'`      ...not correct
`var_name=value`            .....correct
- No need of space when you create a variable.
Eg.
```
    #! /bin/bash
    Name="Sol"
    Sport="Game"
    echo "Your name is $Name, you love ${Sport}s"   
```
    "${ }" is used remove the space after variable. Eg. in the above code ${Sport}s displays: Games
NB. Use splited terminals like this:
```
nano hello.sh      #open a bash file      
#! /bin/bash       #shebang     
<<COMMENTS                  
..a lines of codes..             
COMMENTS
```                            
In the other terminal run the code:
## set
- Gives many values for many variables.
```
    #! /bin/bash
     set sol feye anus xy
     echo $1 $3           # displays: sol anus
```
## System Variables
- Declared by the system:
```
#! /bin/bash
echo $Bash                      # place of our bash files
echo $SHELL                    # our shell type
echo $BASH_VERSION    # 
echo $PWD                      #
echo $HOME                    # our home directory
echo $PATH
echo $USER
```
- Here are so many  system variables:  LANG, TERM, MAIL, EDITOR, USER, SHELL...
- If we use:  `echo $PATH`  ..it tells some commands and scripts path that we can run them without using `./` simply by writing the command only.
# Variables and Datatypes
**Syntax**:  `var=("list1" "list2" "list3" "list4")` ..declaring array.
To display `${var[0]}`  ...displays:  `list1`
- To display all elements:  `${var[@]}`
- To get the indexes:   `${!var[@]}`
- To get the length:   `${#var[@]}`
- To add elements to the array:  `var[6]=list7`
- To remove element:  `unset var[2]`  ..removes: `list3`
Eg.
```
>  nano hello.sh

#! /bin/bash
var=("sol" "feye" "xy" "xz")
unset var[0]
echo ${var[@]}
```
To run use another terminal and type each:
```
>   chmod +x hello.sh     # gives execution perision
>   ./hello.sh          # run the code
```

**Best Example:**
```
#! /bin/bash
var=("sol" "feye" "anux" "letex" "umex")
echo "My name is: ${var[0]}"
echo "The whole list is: ${var[@]}"
echo "The indexes are: ${!var[@]}"
echo "The length is: ${#var[@]}"

echo "Enter names separated by space: "

read -a names
echo "Wait for 3 seconds only..."
sleep 3s
echo "The names You entered are: ${names[@]}"


```
