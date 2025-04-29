### Script Installation
- To clone or download repo link to our linux:
`git clone <link from github repo>`
clone to one path and it makes folder(has files).
- **Script modules**: script dependencies, makes the script functional.
- scripts are made by *python, bash, go, ruby....etc*. They have dependencies(modules or libraries).
1. **python**: to install module : `pip install <modulename>`
so, go to the downloaded python files directory and install requirements file
i. for requirements file:   `pip install -r requirements.txt`
**NB**. For python, module name is specific(**requirements.txt**). but, for **go** it is dynamic.
2. **Go**: to install module:   `go install <module name>`
3. **Ruby**: to install module:   `gem install <module name>`
**NB**. **pip**: is sometimes not pre-installed. and now **pip** is changed to **pipx**.
-So, download(install) pip/x/:   `sudo apt install python3-pip`
- After installed then:   `pip install term(moduleName)`      
for **python** use:    `pip install -r requirements.txt` 
#### Go scripts:
- to install, there are two mothodes:
a. **Old version**:  
    `go get <github link>`
b. **New version**: 
     -**NB**. *go scripts* have **--@latest** at the end
- download the package: `go install <github link>`
- move the file to **/usr/bin/**  ..b/c the default download place is **/home/solace/go/bin**.
   `sudo mv <filename>_/usr/bin` 
 so, After moving the module now it can works properly. 
 To run it just enter the `<scriptName>` only as a command, 
 unless, If you do not move to /usr/bin use: `.go/bin/<file name>` 
 
 **NB**. Sometimes to Install the scripts with simple command, find **Installation or usage** part 
 on the repo and copy the commands and pest to your linux.
### Helping on linux
1. **Manual command(man)**:   eg..  `man awk`
     NB. To get out from man, press 'q'.
 2. **Help command**:     `<your command> -h`    or
                   `<your command> -help`     or
                   `<your command> --help`    ...either of these 3 can work.
      eg.   `awk -h` 
### linux processes and services
- **Processes**: when browser opens, linux loads....
           The program go to memory, and starts process.
           (Foreground programs...     eg. *opening of chrome* )
- **Services**: Background programs that starts automatically or manually. often for system tasks.
         (also, known as **daemons**).
         eg. connecting the wifi to the router.
 To get the processes running in our linux use:  `ps [options]`
 - **commands**:    `ps`                 ....currently running processes in our shell.
             `ps -A`           ....All processes running in our linux.
              `ps -v solace1`       ....programs running on the username solace1.
  - To **stop** the process: `kill [options] [PID]`     or       `killall [programName]`
  NB.  **PID** : process ID for currently running programs.
    **PPID** : parent process ID,(program processes may create another processes
          called: **parent process** ).
          eg.  *When we opens chrome only but, if the chrome opens other programs.*
- **To stop processes(more on kill)**:  
   `kill -19 PID`   ......stop a process
   `kill -18 PID`   ......resume a process
   `kill -9 PID`     ......stop immediately 
               .....There are 31 options. check them!
   NB. You can get programs PID from **`ps`** .
    - To **delete a parent program** that is created(opened) by anther(original) program,
       use the command:   `kill -9 [PPID]`
       eg.  `kill -9 3841`
       or, You can use a program name instead of process ID (PID).
       `killall [process name]`
       eg,  `killall picom`
   BUT, **ps** *can not tell you the realtime processes*. so you can use another tool:  **`top`**
   `top` is installed on linux *by default*.
   or, Use **`htop`** - this is more fun, colorful, and more enhanced. but, It is not pre-installed. so,
   install it  first:   `sudo apt install htop`  
   Then, run it using command:   `htop`
   -It has more features: eg, search(f3), kill(f9), exit(f10)...
### Foreground and Background running of Terminal Commands
- **Foreground method**: processing at the front.
- **Background method**: process at the end of command. 
                 using '**&**' at the end of command or press '**ctrl+Z**' when running command.
             eg.   `sudo apt update&`
                 `sudo apt update`  ...then enter(run) and press '*ctrl+Z*' 
             Then, The command running will gain PID and run at the background.
  To make background programs to foreground use command:  **`fg`**
