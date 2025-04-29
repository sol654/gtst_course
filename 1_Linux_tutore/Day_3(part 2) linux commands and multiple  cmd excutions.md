**pwd** :print working directory(current path).   NB, All directories path is start with *root directory (/)*.
**echo** :display line of text(string) that are passed as argument. echo [string]
      eg. *echo "Hello world!"*
      - *output redirecting*: write output to text file using '>' .  
        eg. *echo "My first!" > newfile.txt*     ...so new txt file is created.
      - if we want existing file we use '>>' .
          eg. *echo "my second" >> existingfile.txt*
**cat/head/tail/less** :these synopsis are used for similar purpose. but, they have dt ways to use.
       eg. *cat text.txt*   ...displays all lines text.
     **less** :has similar use with **cat** but it uses *text editor* to open the file, click 'q' to exit from *less*.
           eg. *less text.txt*
     **head** :displays only 10 lines of text from *up*.   
           eg. *head text.txt*
     **tail** : also displays only 10 lines of text but from *last*.  
              eg. *tail text.txt*
**touch** :create files(empty text files).
      eg. (*touch sol*):one file   ..or..  (*touch sol feyo.md* anu):3 files
**mkdir** :create folder (make a directory). 
        eg. (*mkdir fold1*)  ..or.. (*mkdir fold1 fold2 fold3*)
      eg2. *mkdir -p sol/tes*       ...means(mkdir sol , cd sol , mkdir tes)
      eg3. *mkdir "Sol Tes"*        ...if folder name has space use quotation
**clear** :clear the screen. or click (*ctrl + l*)
**rm** :remove files.     eg.  (*rm x*)  ..or..  (*rm x y*)
     eg. *rm -r foldx*    ..if the folder has different files inside *foldx* (recurceive).
     eg. *rm -i fold1*    ..ask to delete.
     eg. *rm -f fold1*    ..foce delete.
     best eg. *rm -rf fold1*         .....the combination of r and f.
**cp/mv** :copy/move        
       eg.  *cp file.txt fold*      ...copy file to folder
       eg2.  *cp file.txt fold1/fold2*      ...if path is similar with fold1
       eg3.  *cp file.txt ~/sol\ tes*       ...using path NB.(sol\ tes = "sol tes").
       eg4.  *cp -r ab/x*         ...to copy all recurseive files.
       eg5.  *cp "text.txt" ../ ../tmp*     ...back twice and copy to folder tmp.
       mv_Eg.  **mv * /root**       ...move all things.
**grep** :global search for regular expression. search the line of pattern and display the lines.
      eg.  *grep 'my' file.txt*       
         *grep -i 'my' text.txt*                ...case insensetive.
         *grep -c 'my' text.txt*               ...count lines number.
         *grep -l 'my'                            ...display file name.
         *grep -r 'my' folderName*       ...search text in folder(recurceively)
         *grep -v 'my' text.txt*                ...displays lines that has not 'my'.
         *grep -n 'my' folderName*       ...displays the lines that has 'my' and tells each line by                                                           counting.
         *grep -o 'my' file.txt*                ...displays only the word 'my' in every lines that have 'my'.
     **NB.** How **hackers** use **grep**??
         1,  **grep -ran HTB**          ....**a** -searches the pattern from binary files(from ZIP files) and                                                    displays line.
                Therefore, **ran**: recurse, search pattern and display line, shows line number.
         2, **grep -rno HTB**          ....recurse, shows number of line, shows specific word(pattern).
**wc** :word count.  
       eg. *wc xx.txt*               ...shows lines number, number of words, byte(storage)
         *wc -l xx.txt*           ...shows number of lines in text.
         *wc -w xx.txt*         ...shows number of words in text.
         *wc -c xx.txt*          ...shows byte or storage.
##### Multiple command excutions
- **And**(&&): if both commands work without error.
- **OR(||)**: the second command is  like option.
         - if the first command is correct the second will not be changed.
- **PIPING( | )**: the first command output is as the input for second command.
      eg.    *cat file.txt | wc -l*            ....it is equal with ( *wc -l file.txt* )    

**sed** :stream editor(for large processing files line by line)
    - filter text & text replacement,
    - select pattern and delete line
    - efficient text manipulation for tasks like *network info gathering and pentesting logs*.
    NB. *log files* -databases(login and signin infos).
    synthax: *sed [options] 'command' file*
    eg.  *cat temp.txt | sed 's/sol/solace/'*            .....replaces sol with solace.
- if it finds the word more than 1 time in one line.    use   *'s/sol/solace/g'*     ....replaces all sol with solace not only the first sol.
	   eg.   *cat log.txt | sed 's/sol/solace/g'*
- to delete line:  use    '/pattern/d'
       eg.   *cat log.txt | sed '/pattern/d'*        ...delete the line of the pattern.

**awk** :versatile command-line-text-processing tool.
    - scan text and extract data in **structured** file.
    - allow field based(row and collumn).
       like **csv** files(comma separated values).
    csv_Eg. 
     ID, name, dep, sec
     10, Sol, cs, 3
     11, Feye, IT, 2
     12, Ume, cs, 3  
     ---    
     $1, $2, $3, $4 .......this means column1, column2, column3, column4
 syntax: *awk '/pattern/ {action}' file.txt*
    eg.   *awk '{print $1 $3}'* file.txt*        .......prints column1 and column3
  or,  *awk '/pattern/ {print $0}' file.txt*        ...NB. $0 means all columns.
       therefore, this syntax says "print lines matching 'pattern'"
      eg. *cat file.txt | awk 'print $3'*       ...prints the second column.
   NB, **awk**: by default determine: *columns if they are separated by **space()***.
       here, space is known as :**Delimiter**. to change delimiter use  *-F "sign"*
       eg, *cat log.text | awk -F "," '{print $3}'*           ... *-F ","* means awk uses comma as column                                                                                            separater.
- **NR**: line(record) number. ...(row number)
  eg, *cat eg.txt | awk -F "," 'NR<=4{print $1}'*     ...displays the first 4 datas of column1.
- **NF**: number of fields in the current record.
  eg, *cat eg.txt | awk -F"," '{print $NF}'*      ...displays the last column data.
 *some examples*:
       *cat file.txt | awk -F "," '/6/ {print $2}'*     ..checks pattern 6 then prints column2.
       *cat file.md | awk -F "," '$3>3000 {print $3}'*  ..prints the data of column3 if > 3000.
       *cat eg.txt | awk -F "," '{print $0}'*   ....prints the whole text file.
       *cat eg.txt | awk -F "," '{sum+=$4}END{print "Total: ", sum}'*    ..adds all $4 and displays total.
