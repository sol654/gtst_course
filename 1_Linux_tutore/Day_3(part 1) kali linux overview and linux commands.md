### Tools in kali linux(common mostly used tools)
1, **Information gathering**: maltego, nmap, recon-ng.
2, **Vulnerability Analysis**: nikito, nmap.
3, **web application analysis**: burpsuite, sqlmap, wpscan, zap.
4, **Database assessment**: sqlmap, jsql injection, SQLite data..
5, **password attack**: hashcat, john, wordlists
6, **wireless attack**: aircrack-ng, wifite, reaver
7, **reverse engineering**: make a research about how the system is build. 
                - apktool, ghydra, NASM shell
8, **Exploitation tool(metlefiya)**: metasploit, search sploit, sqlmap
9, **Sniffing and Spoofing(manefnef)**: for listining or hijacking networks.
                - wireshark, hamster
10, **post exploitation**: focuses on *maintaining access*.
                - powersploit, backdoor
11, **Forensics**: research and investigate a cyber attacks.
          - hashdeep(more and mostly used tool), foremost
12, **Reporting tool**: after some forensic you will get a data so will write report.
             - maltego, recordmydesktop(using video)
13, **social engineering**: backdoor, maltego, social engineering
14, **system services**: buttons to start some services.
             - the whole tools are bests use them
15, **usually used applications**: softwares for some basic purposes.

NB. search about **Hybernate** on google.
#### Folder Manager
1, **Dolphin**: on *KDE plasma*- has windows like folder manager
2, **Thunar**: on *gnome and **ubuntu***
3, **Nautilus**: on *ubuntu* mostly
NB. on windows folder managers are premimum not free.
### 5 Parts of terminal
- username = solace
- Hostname = Hantermachine
- current directory = path
- privilege = $-(user), #-(root)
- command place = _ 
- home directory = ~
- $ = user (privilege)
- root (power) = # 
eg. 
> (solace @ Huntermachine)-[~]
> $_                                                                   [~]=> shows path

Home Directory = [~]
local directory = [.] ...current directory
all directory = [*]     ...* * shows all directories
~ = home/xx    (home directory)
### commands
-commands have options and arguments
**command --option argument**
eg. Math --add 1 1
*Command*: is a small program that used to do one task well.

**ls**: 
ls ...(blue=folder, white=txt, and others)
ls -l ...creared date, by user, permition
ls -a ...list with hidden files
ls gtst ..list files in gtst folder
ls -R ...files in all folder
ls -Rla ...the combination of (-R i and a)
NB. If the file name is started with dot(.) = Hidden file

**cd**:
cd / ...root directory
cd , cd ~ ...Home directory
cd ..    ...back once
cd ../ ..    ...back twice
cd grst ...get in to gtst folder
cd 'folder one'   .....if the folder name has space