# Script Installation

To clone or download a repository to your Linux system:
```bash
git clone <link from github repo>
```
This creates a folder with the repository files at the specified path.

**Script modules** are dependencies that make scripts functional. Scripts can be written in Python, Bash, Go, Ruby, etc., and each has its own dependency management:

## Python
To install Python modules:
```bash
pip install <modulename>
```
Navigate to the downloaded Python files directory and install from requirements file:
```bash
pip install -r requirements.txt
```
> **Note**: Python uses a specific `requirements.txt` file name, while Go uses dynamic module names.

## Go
To install Go modules:
```bash
go install <module name>
```

## Ruby  
To install Ruby modules:
```bash
gem install <module name>
```

> **Note**: `pip` may not be pre-installed. The modern alternative is `pipx`. To install pip:
```bash
sudo apt install python3-pip
```
Then install modules with:
```bash
pip install term(moduleName)
```
For Python, always use: `pip install -r requirements.txt`

### Go Scripts Installation
There are two methods:

**Old version**:
```bash
go get <github link>
```

**New version**:
> **Note**: Go scripts typically use `@latest` at the end
```bash
go install <github link>
```
Move the file to `/usr/bin/` since the default download location is `/home/solace/go/bin`:
```bash
sudo mv <filename> /usr/bin
```
After moving, the module will work properly. Run it by simply entering the script name as a command. If not moved to `/usr/bin`, use: `./go/bin/<file name>`

> **Note**: For easy installation, check the **Installation or Usage** section in the repository and copy the commands to your Linux terminal.

# Linux Help System

1. **Manual command (man)**: 
```bash
man awk
```
> Press 'q' to exit the manual.

2. **Help command**:
```bash
<your command> -h
<your command> -help  
<your command> --help
```
Any of these three formats will work. Example: `awk -h`

# Linux Processes and Services

- **Processes**: Programs loaded into memory when executed (e.g., opening Chrome - foreground programs)
- **Services**: Background programs that start automatically or manually for system tasks (also known as **daemons**), e.g., WiFi connection to router

To view running processes:
```bash
ps [options]
```

Commands:
- `ps` - Currently running processes in your shell
- `ps -A` - All processes running on your Linux system  
- `ps -v solace1` - Programs running under username solace1

To stop processes:
```bash
kill [options] [PID]
```
or
```bash
killall [programName]
```

> **Note**: 
- **PID**: Process ID for currently running programs
- **PPID**: Parent Process ID (when program processes create other processes)

Example: When Chrome opens additional programs.

**Process control options**:
- `kill -19 PID` - Stop a process
- `kill -18 PID` - Resume a process  
- `kill -9 PID` - Stop immediately (force kill)
> There are 31 kill options - check the manual for details.

You can find program PIDs using `ps`. To delete a parent program created by another program:
```bash
kill -9 [PPID]
```
Example: `kill -9 3841`

Alternatively, use the program name instead of PID:
```bash
killall [process name]
```
Example: `killall picom`

> **Note**: `ps` doesn't show real-time processes. Use `top` (pre-installed) or install `htop` for enhanced functionality:
```bash
sudo apt install htop
htop
```
`htop` features: search (F3), kill (F9), exit (F10), and more.

# Foreground and Background Execution

- **Foreground method**: Process runs in the terminal foreground
- **Background method**: Process runs behind the scenes using:
  - `&` at the end of the command, or
  - `Ctrl+Z` during command execution

Examples:
```bash
sudo apt update&
```
or
```bash
sudo apt update
```
Then press `Ctrl+Z` - the command will gain a PID and run in the background.

To bring background programs to the foreground:
```bash
fg
```

