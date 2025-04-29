# Regular Expressions (Regex)
- Most filter Validation on  any platforms.
- **Patterns** to filter tabs, spaces, texts...
- **Regex**: are used on linux tools like *sed, awk and grep*.
- **NB**: In search bar of **VScode**, first make **ON** regex(*`.*`*), then use patterns like:  `tab`, `\n`...
## Metacharacters
They are symbols for regex patterns.
**Eg**: `.` , `*` , `\` , `^` , `[]` , `{}` , `|` , `+` , `$` , `?` 

- **DOT(`.`)**: filters all lines except new line.
- **CARET(`^`) - Assertion**: get a line that starts with the pattern. 
   **Eg**. `^hello`   -filters line **starts** with hello.
- **DOLLAR(`$`) - Assertion**: filters line **ends** with the pattern.
   **Syntax**:  `PATTERN$`
   **Eg**.  `hello$`   -filters line ends with hello.
- **PLUS(`+`) - Quantity**: get a line that have pattern that occurs **1 and more** time.
   **Eg**.
```
      hellos+   -filters hellos, helloss, hellossss....
```
- **ASTRIKS(`*`) - Quality**:  get a line that have pattern that occur 0 or more time. **Eg:**
```
     hellos*   -filters hello, hellos, hellossss ..etc..
```
- **QUESTION MARK(`?`) - Quantity**: get a line that have pattern that occur 0 or 1 time only. **EG**: 
```
      hello?     - filters only hello or hellos.
```
- **Best Example**: Find a pages that starts with 'n' and ends with com.
```
solution:  ^n.*com$
```
NB. `.+` and `.*` - means everything.
- **CURLI BRACKET(`{min, max}`) - Quantity**: it gives a range for pattern occurrence. **EG**: 
```
  hellos{1, 3}   - filters hellos, helloss and hellosss only.
```
#### Some Equalities
- `{0, } = *`
- `{1, } = +`
- `{0, 1} = ?`
**Best Exercise**: Start with 'n' and ends with 'com' but there must be characters atleast 7-13 chars only.
```
  Solution-1:   ^n.{7, 13}.*com
```
and also:
```
   Solution-2:   ^n.*[a-z]{7,13}.*com
```
### Other Simple Metacharacters
- **(`\w`) - Small w**: to get **alphanumeric** characters only(Letters and Words only).
- **(`\W`) - Capital W**: opposite of (`\w`), filters TABs, Spaces, dots...
- **(`\s`) - Small s**: TABs and White Spaces only.
- **(`\S`): - Capital S**: except spaces.
- **(`\d`) - Small d**: filter digits (numbers only).
- **(`\D`) - Capital D**: except numbers
- **PIPE(`|`) - OR**: to search two different things.
```
  Syntax:   a|b   - filters a and b each.
```
**NB**: To filter dots(.) or other metachars use `\`.      **EG**: `\.` -this filters dots.
- To filter Metacharacters use backslash. **Syntax**:  `\sign`
```
EG:  \*  ,  \^  ,  \.  ,  \$...
```
- **SQUARE BRACKET(`[]`) - Custom pattern**: to create your own patterns.
         - **Syntax**:  `[PATTERN]` 
         - **EG**:   `[a-z]`
    - **Best Example**: `[a-z\dA-z]`  -filters both capital and small letters and digits.
    
- **EX**: Find **emails** from some text file.
```
    so/n:  ^.*@gmail\.*(com|net)$
```
