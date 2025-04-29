**print(obj='', sep='', end='')** 
eg.  `print('my mame is','Solace')`     ....outputs:  my name is solace
eg2. `print('my name is','solace',sep=':')`     ...outputs:  my name is: solace   ...has a              separater':'

eg3.
```
  print('my name is','sol',sep=':',end='-')
  print('Tes')
                 ....The output:   my name is: Sol-Tes
```

eg4. 
```
 print('sol', end=',')
 print('Tes')
 print('Ens')             ..outputs: Sol,Tes
                                     Ens

```
eg5.
```
print("My name is\n sol")    ...'\n' makes a new line.
print("My name is\t sol")    ...'\t' makes a TAB.

```
**NB**. *Print* in pseudocode is: **DISPLAY**
**Comment**: for a single line:  `#comment`
          for multiple line: ` ''' lines of comment...  '''`
**Keyword**: is a pre-defined, has a special meaning for compiler.  
      eg.  False, except, lambda, is...
**Variable**: 
```
        gtst = 10
        print("I am", gtst, "Years old!"
```
    **NB**. You can use the term '**DECLARE**' for pseudocode.
   - You can change variables by declaring again.
- IF you use:`f` 
     eg.   
```
     gtst = 10
     print(f"I'm {gtst} years old.")
```
#### DataTypes
- Neumeric, String, sequence, Mapping, set, Boolean
**A**. **Numeric**: Int, float or Complex types.
       eg. num=2+j    .....complex datatype.
**B**. **String**: `var = ''` or `var = ""`
     eg.
```
        xy = "sol"
        print("The Datatype of", type(xy))       ....tells the type:  String
```
**C. Sequence Datatype**: there are 2 types *List*  and *Tuple*
1. **List**: separated by comma and enclosed by square bracket.
    eg. 
```
       language = ['swift', 'java', 'python', 10, 20]`
       print(language)        ...#prints all
       print(language[2])     ...#prints: *python*
```
    NB. You can add or modified *list*
       eg.  `language.append("C++")`     ..#added 'C++' to the list.
- NB. to declare a list with Pseudocode:
  EG.  `DECLARE a list called 'language' containing "x", "y", "z"`
1. **Tuple**: the only difference is Tuple can not be modified.
      - and we use parenthesis and comma for Tuple.
      eg.
```
           lang = ('C++', 'java', 'swift', 200)
           print(lang[0])            #...prints:  C++
```
**D. Dictionary Data**: unordered collection.
    - stores elements in **key:value** pairs.
    - it uses *curly brace{} to enclose, comma(to separate), and ':' to pair key:value*
    eg.   
```
         capital_city = {'Ethiopia':'AA', 'Italy':'Rome', 'England':'London'}
         print(capital_city[Italy])     #..prints:  Rome
         print(capital_city)           #...prints all
```
NB. If we want to use in **Pseudocode**:
eg.
```
    DECLARE a dictionary "fruits" with the following values:
               Mango = 12
               Apple = 30
               Banana = 25
```
