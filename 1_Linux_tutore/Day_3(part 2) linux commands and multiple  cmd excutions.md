# Essential Linux Commands for Cybersecurity

## Basic File and Directory Operations

### `pwd` - Print Working Directory
Displays the current directory path starting from the root directory (`/`)

**Example**: `pwd`

### `echo` - Display Text
Outputs text strings passed as arguments

**Basic usage**: `echo "Hello world!"`

**Output redirection**:
- `echo "My first!" > newfile.txt` - Creates new file with text
- `echo "my second" >> existingfile.txt` - Appends to existing file

### File Viewing Commands
- **`cat`** - Display entire file content: `cat text.txt`
- **`less`** - Interactive file viewer (press `q` to exit): `less text.txt`
- **`head`** - Show first 10 lines: `head text.txt`
- **`tail`** - Show last 10 lines: `tail text.txt`

### File and Directory Management
- **`touch`** - Create empty files: `touch sol` or `touch sol feyo.md anu`
- **`mkdir`** - Create directories:
  - `mkdir fold1` (single directory)
  - `mkdir fold1 fold2 fold3` (multiple directories)
  - `mkdir -p sol/tes` (create nested directories)
  - `mkdir "Sol Tes"` (directory with spaces)

- **`clear`** - Clear terminal screen (or `Ctrl + L`)

- **`rm`** - Remove files/directories:
  - `rm x y` (remove files)
  - `rm -r foldx` (recursive removal)
  - `rm -i fold1` (interactive prompt)
  - `rm -f fold1` (force removal)
  - `rm -rf fold1` (force recursive removal)

### File Operations
- **`cp`** - Copy files:
  - `cp file.txt fold` (copy to folder)
  - `cp file.txt fold1/fold2` (copy to subdirectory)
  - `cp file.txt ~/sol\ tes` (copy to path with spaces)
  - `cp -r ab/x` (recursive copy)
  - `cp "text.txt" ../../tmp` (copy with relative path)

- **`mv`** - Move/rename files:
  - `mv * /root` (move all files to root directory)

## Text Processing Commands

### `grep` - Global Regular Expression Print
Search for patterns in files

**Basic usage**: `grep 'my' file.txt`

**Options**:
- `-i` - Case insensitive: `grep -i 'my' text.txt`
- `-c` - Count matches: `grep -c 'my' text.txt`
- `-l` - Show filenames only: `grep -l 'my'`
- `-r` - Recursive search: `grep -r 'my' folderName`
- `-v` - Invert match: `grep -v 'my' text.txt`
- `-n` - Show line numbers: `grep -n 'my' folderName`
- `-o` - Show only matched pattern: `grep -o 'my' file.txt`

**Cybersecurity Applications**:
- `grep -ran HTB` - Recursive search showing line numbers (searches binary files)
- `grep -rno HTB` - Recursive search showing line numbers and exact matches

### `wc` - Word Count
Count lines, words, and characters

**Usage**:
- `wc xx.txt` - Lines, words, and bytes
- `wc -l xx.txt` - Line count only
- `wc -w xx.txt` - Word count only
- `wc -c xx.txt` - Byte count

## Command Chaining and Text Processing

### Multiple Command Execution
- **`&&`** - AND operator (run second command only if first succeeds)
- **`||`** - OR operator (run second command only if first fails)
- **`|`** - Piping (output of first command as input to second):
  - `cat file.txt | wc -l` (equivalent to `wc -l file.txt`)

### `sed` - Stream Editor
Powerful text processing for large files (ideal for log analysis and network data)

**Syntax**: `sed [options] 'command' file`

**Examples**:
- `cat temp.txt | sed 's/sol/solace/'` - Replace first occurrence per line
- `cat log.txt | sed 's/sol/solace/g'` - Replace all occurrences (global)
- `cat log.txt | sed '/pattern/d'` - Delete lines containing pattern

### `awk` - Text Processing Tool
Ideal for structured data extraction (CSV files, logs, etc.)

**Basic syntax**: `awk '/pattern/ {action}' file.txt`

**Examples**:
- `awk '{print $1, $3}' file.txt` - Print columns 1 and 3 (space-separated)
- `awk '/pattern/ {print $0}' file.txt` - Print entire lines matching pattern
- `cat file.txt | awk '{print $3}'` - Print third column

**Field Separators**:
- `awk -F "," '{print $3}' log.text` - Use comma as delimiter

**Special Variables**:
- `NR` - Record (line) number: `awk -F "," 'NR<=4{print $1}' eg.txt`
- `NF` - Number of fields: `awk -F"," '{print $NF}' eg.txt` (last column)

**Advanced Examples**:
- `awk -F "," '/6/ {print $2}' file.txt` - Pattern matching
- `awk -F "," '$3>3000 {print $3}' file.md` - Conditional filtering
- `awk -F "," '{print $0}' eg.txt` - Print entire file
- `awk -F "," '{sum+=$4}END{print "Total: ", sum}' eg.txt` - Column summation

---

