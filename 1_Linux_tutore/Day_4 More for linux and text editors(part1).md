### linux file Heirarchy
- linux(unix) has a special file system(a directory structure that the OS uses).
- **File System**:
      - for windows(**local Disk C**)
      - for linux(**root directory(/)**)
NB. **root directory(/)** and **/root** are different becouse,
      - /(root) is normal users 'root directory'. but,
      - /root is root user's file place. normal user can't access it.
   **/bin** :binary files (commands) directory. for normal user in a single user:
         eg, cat, ls, cp.......   NB. both normal and root users can access it.
  **/boot** :boot loader files.
  **/dev** :Essential devises files.
      - terminal, usb, or any other devises attached to the system. 
        eg, /dev/tty1,  /dev/usbm0mo
  **/etc** :et cetera ..contain *configuration files of all programms.*
      - has ***start/stop** shell scripts* for programms.
           eg, /etc/hosts, /etc/passwd, /etc/resolve.config
      NB. **/etc/hosts** :gives *domain name for IP addresses*.
             eg, 192.168.1.1 = ex.com
  **/home** :has different users personal files, but you cannot access other users personal file.
         you must login in to the user.
        eg. your home directory /home/solace
  **/lib** :libraries essential for the binaries in /bin and /sbin.
     - library filenames are either lb* or lib*.so*.
  **/media** :mount points for removable medias. such as CD-ROM.
        - temporary mount directory.
        eg, /media/cdrom   ...for CD-ROM.
  **/mnt** :Temporarily mounted file. 
  **/opt** :optional application software packages. 
       -if you install other than linux applications like Chrome.
   **/sbin** :essential system binaries. commands for **root user** only.
       -NB. If normal user want to access these commands you have to use **sudo** command.
  **/tmp** :here you can create temporary files. but, if system rebooted it will be deleted.
  **/usr** :(user utilities) ..to make other users can access our linux, 
      but you can limit the accessible commands.
      eg, /usr/bin,  /usr/sbin.....
#### Text Editors
- They are programs or commands. has two methods
  **1, linux command line text editors** :eg. Vim, Nano, Emacs, Neovim....
  **2, linux Graphical Text editors** :eg, sublime, vscode, Gedit, plume....

  ### VIM
    Before vi :unix was the line editor. able to see and edit one line.
    - Then **(vi improved)**.
    - **vim editor** is:
         -very powerful
         -but at the same time it is cryptic(having or seeming to have a hidden meaning).
         -hard to learn for window users. bc it has 4 MODES.
     ### Modes for vim
     NB. to use  vim editor to have to pass 4 modes.
     First create file with vim eg.  *vim file.txt*
     1. **Normal mode**: here you can not write, save, exit.. vim is by default normal mode.
     2. **Insert mode:** (*click i* ) ..now you can write. (*click enter*)=new line.
     3. **Command mode:** (*click esc*) ..now you can *save, quite, save and quite, force save and      quite, undo, Execute bash commands*. then:
         :w + enter    ... to save.
         :q + enter    ... to quit.
         :w! or :q! or :wq! + enter    ... to foce save and quit.  (! this is force)
         :u     ....undo.
         :%!BashCommand       .....to write bash command.
               eg. :%!grep fun eg.txt
       4. **Visual mode**: allow block of text to manipulate(select, copy, pest, delete).
          - To get in to visual mode there are several ways.
              -If *character wise* visual mode *click 'v'* .
              -If *line wise* visual mode  *click '(shift + v)'*
              -If *Block wise* visual mode *click '(ctrl + v) or (ctrl + q)'*
          - To **delete** selected text  *click 'd'*.
          - To **copy** selected text  *click 'y'*.
          - To **pest** selected text  *click 'p'*.