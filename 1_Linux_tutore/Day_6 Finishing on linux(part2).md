### Managing Services
- services can be started or stopped.
- To manage system we can use tools called: '**systemctl**' or '**service**'
-**Syntax**: 
     `sudo systemctl start <service name>`   ...start service.
     `sudo systemctl stop <service name>`    ...stop service.
     `sudo systemctl enable <service name>`    ...start service when computer boots.
     `sudo systemctl disable <service name>`   ...stop service when computer boots.
     `sudo systemctl status <service name>`   ...checks status, if service is started or stopped.
 -**other ways**:
      `sudo service <service name> start`
      `sudo service <service name> stop` 
      `sudo service <service name> status` 
               ...ETC(you can use enable, disable and so on..)
       eg. `sudo systemctl start apache2`
         `sudo service apache2 start` 
#### Null Device (A bit bucket)
- found in **/dev/null**
- If you do not want to see errors on your screen and you do not want to save them to a file, you can redirect them to **/dev/null**
- On shell output there are 2 things:
  -STDERR = **2**    ..ignore Error outputs.    eg. ...not found...
  -STDOUT = **1**   ...ignore successful(correct) output.  eg.  ..password updated successfully!
- To redirect errors from command result we do 
   `command 2> file_name(or /dev/null)`
- To redirect error-free output:
  `command 1> file_name(or /dev/null)`
NB. If you use file_name instead of  /dev/null  ..you will save the output to the text file.
 eg.   **`sudo systemctl start apache3 2> xy.txt`**
    this will save the output to xy.txt file.
but, If you want to not to save and to do not look the error output use: /dev/null
 eg.  `sudo systemctl start apache3 2> /dev/null`
NB. you can save any commands output in to some text file or insert it to /dev/null.
If you check /dev/null, it is empty always. because its use is just like a Blackhole or Bermuda.

### Symbolic Linking
- It is the same as windows shortcut.
- For existing files/folders, we can create a shortcut programs.
eg. If we want to access this path ~/fold1/fold2/fold3/fold4/fold5/file.txt  we can create a symbolic       link:    `ln -s ~/fold1/fold2/fold3/fold4/fold5/file.txt sol`  
**NB**. If the file has symbolic linking, the permission (ls -l) will start with "**l**" not with ('-' or 'd').
 eg. 'lrwxrwxr-x' and in file/Folder name there is the linked file path:
    eg.  " sol->/home/solace/fold1/fold2/foold3/fold4/fold5/file.txt "
- **Syntax**:
     `ln -s source_filePath fileName`
 **NB**. If we create symbolic linking in home directory, we can access it in a home directory only.
     but, If we want to use it in root(/) directory, use '~/'  .  eg. `~/sol`
### Alias 
- used to give a name to to **a bunch of command**.
Eg.  If I want to name `ls -la` 'rex' so any time I want to get output of 'ls -la' I just type `rex`:
      `alias rex="ls -la"` 
     but, it does not work after you closed terminal, so you have to create (add) to the shell configuration file :
     **for**:
         **Bash**: `~/.bashrc`
         **Zsh**: ~/.zshrc
         **Fish**: ~/.config/fish/config.fish
 eg.  My terminal is Bash, so enter the command first, enter `nano ~/.bashrc`    and go to file and
     scroll at the end and get "**#see more ls aliases**". then add:  *`alias rex="ls -la"`*
### Wget
- To download tools from websites or servers.
- command: `wget [options] [link]`
-EG.  `wget http://tldp.org/LDP/intro-linux/intro-linux.pdf
### Find
- To search files, folder, musics, videos...
- **syntax**:
     `find [search path] [option] [search word]`
 - **Commands**:
     `find / -name "linux"`    ...finds with the name 'linux'. start from root path.
     `find /home -perm 777`    ...searches with permission that has 777. start from home                                                            directory.
     `find /home/solace -type f -perm 4000` ...find a text file with SUID(special file                                                                                           permission).
     `find -type d | find -type f`   ...find files or directories.
     eg.  `find / -type f -perm 1000 > /dev/null` 

#### Tmux
 - tmux is use to classify our terminal work.
   - first install it. and then to run it you have to configure it:
   - To configure it:
    -use the command:   `nano .tmux.conf`
    then type:
         unbind C-b
         unbind l
         set -g prefix C-a
         unbind %
         bind e split-window -h
         bind o split-window -v
         set -g base-index 1
         setw -g pane-base-index 1
     copy this and pest to your terminal's nano to access tmux.

Therefore :
- To split horizontally:  ^A then o
- To split vertically:  ^A then e
- To exit:  ^A then x , or just type `exit`
- To create tab:  ^A then c
- To rename the tab:  ^A then ,(comma) 
- To switch tabs:  ^A then < numbers >
- To switch partitions:  ^A then < arrows >
-For more you can google but be aware of our super key is ^A .
#### Linux privilege escallation
