 These file permissions are mailny user for pentesting.
#### There are three other special file permissions
1. `SUID(s)`: set user ID bit, - add 4 infront of numeric value -> eg. 4000
2. `SGID(s)`: set group ID bit, - add 2 infront of numeric value -> eg. 2467
3. `STICKY(t)`: set other ID bit, - add 1 infront of numeric value -> eg. 1777
eg.  `chmod +s file.txt`  ->   -rwsr-sr-x
                        -gives *s* for only user and group.
     `chmod +t filex.txt`  ->   -rwxr-xr-t
                           -gives *t* for others.
**Numeric Example:** 
    `chmod 6777 file.txt`     ... -rwsrwsrwx
    `chmod 4777 file.txt`     ... -rwsrwxrwx
    `chmod 2777 file.txt`     ... -rwxrwsrwx
    `chmod 1777 file.txt`     ... -rwxrwxrws
**NB.** files that has *special file permission* are different in **color**. 
- If user, group and other all have special file permissions, The file color become **Full green**.
- If *users* only have a special file permission, The file color = **red**.
- If *groups* only have a special file permission, The file color = **yellow**.
- If *others* only have a special file permission, The file color = **green**.
**NB**. special file permissions(s or t) substitutes the Excute(x) permission.
If the owner of that file gives a special file permission to the file, other any users can access 
and run that file like the owner(user:group) of that file.
**Eg**. If root add **suid** bit on some program then Any user got that program, they can run it as root 
     with out the sudo password.
NB. (you can run any programming files using `./`   eg. `./pythonFile` )
For More check youtube videos of Natan(geez Tech) or other videos.
#### Package installing on linux (linux software)
- package managers to install package(sw) from online server repo:  eg. `apt, pkg, pacman...`
- Debian based package managers ....`apt and dpkg`.
- When you install package: there are other things will be downloaded 
     (package dependencies and package metadatas).
- **Package repository**: is site/server, kali linux use to upload packages.
       **link**:  http.kali.org/kali...   repo link.
- get clone and wget are used for to install tools from other github repo or websites.
##### APT (Advanced Package Tool)
- free software-interface, to install linux tool from online server and also 
   to remove packages from our linux system. 
   NB. The old `apt` used as `apt-get`.
**synthax**:    `sudo apt update`    ...shows if tools have some updates
         `sudo apt search <softwareName>`    ....to search from server.
         `sudo apt install <sw name>`     ....to install from server.
         `sudo apt remove <sw name>`      ....remove only the package from our linux system.
         `sudo apt upgrade`                  ........upgrade if there is some upgrades.
         `sudo apt purge <sw name>`        ....removes the package and its dependencies and                                                                  also its metadatas.
NB. package dependencies(modules) makes the package functional. 
    so they must be successfully installed.
#### Linux Command errors
1. *"culd not get lock/var/lib/lists/lock"*
     -this happens when you try to run apt twice at the same time.
     so you must cancel or exit the other one.
2. *"could not open lock/var/lib/dpkg/lock-frontend"*
      -when you do not use **sudo** for apt and run it.
3.  *"unable to locate package"*
       -when you miss-spell the program name. 
       -or, when the name is correct and if the package is not there in github repo.
4. *"The repository 'http://http.kali.org/kali kali-rolling Release' does not have a release file"*
      -happens when there is a problem on the **repository configuration**. sometimes the **link**
      **might be broken**.
      - so search on google and("updated repository configuration link of your distro"), and goto
      `nano /etc/apt/sources.list`    or use the command: `sudo apt edit-sources` 
      and get :
>     #see https://www.kali.org/docs/general-use.....
>       deb http://http.kali.org/kali kali-rolling main.....
       
after you get the above link, you have to **put the correct repository link** from google or gpt.
     The correct and updated repository link is: 
      "`deb http://http.kali.org/kali kali-rolling main contrib non free`" 
      NB. this maight differ based on the distro. so you can you can search your distro upgraded repository link on google or chatGPT.
      **NB**. To access `/etc/apt/sources.list` by `nano`, use command:  
        `sudo apt edit-sources`
        
NB.    Do not close apt while installation.
     Repository errors, if this happened you can fix it with: `sudo apt edit-sources`
     Use google/youtube... or we will see on "footprinting".

#### DPKG(Debian Package Manager)
- differ from *apt* by *apt is an offline or online*, but `dpkg` is offline only.
- If you want to install a package with dpkg, the package has .`deb` extension.
-**Syntax**:
     `sudo dpkg -i <software name>`     .....install package
     `sudo dpkg -r <sw name>`          ..............remove package
     `sudo dpkg -p <sw name>`             ..........purge sw
 