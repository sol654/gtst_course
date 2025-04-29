- To change **password** of user (or add password to user) use:
     *sudo passwd < username >*
     eg.  *sudo passwd solace1*          ...then give a password.
 - To change users ID use:   *sudo usermod -u < id > < username >*
      eg.   *sudo usermod -u 1002 solace1*    ...now 1002 is id of solace2
  - also, to change id of the GROUP use:   *sudo usermod -g < id > < username >*
       eg. *sudo usermod -g 1003 solace3*
   - To delete the user:    *sudo userdel -r < user name >*
      eg.  sudo userdel -r solace1      ......delete solace1
  - **NB.** In sh-shell **ctrl + something** is not available. so, **useradd** users are not good.
       eg. ctrl + l    ...can't clear in sh shell
   - To make a home directory personal file for useraddusers use:
       *sudo mkhomedir_helper < username >*
       eg.  *sudo mkhomedir_helper solace1*
   - To change a shell type:   use the command: 
         eg.   sudo usermod solace1 -s  /bin/zsh      ....chsnge the shell type to zsh
             sudo usermod solace1 -s /bin/bash     .....changed the shell type to Bash
#### Some Advanced Group Commands
- To create a new group:    *sudo addgroup < groupname >*
     eg.    *sudo addgroup solaces*       ...the group solaces created
 - Add the User to a Group:  sudo usermod aG < group name> < username >
          eg.  *sudo usermod solaces solace1*   ...added a user *solace1* to a group *solaces*
  - To verify(check the group) use:   *groups < username >*
         eg. *groups solace1*     .....gives username then groupName (solace1 solaces)
 - To remove user from a group:  *sudo gpasswd -d < usrname > < groupName >*
      eg.   *sudo gpasswd -d solace1 solaces*
     then, to verify use:   *groups < username >*
 **NB**. users in the same group can access files of the other users. but can not create file.
  NB. The power of **Local user** is *greater* than other newly created(added) users, because 
     they can not access the **sudo** command, because, they are not added in **sudoers** file.
#### SUDOERS file
- linux/unix administrator use to allocate system rights to the system users.
- To add users to sudoers file, use:  **sudo visudo**
then, displays nano file, so go to down and get "**#user privilige specification**", then
copy from   *root     **ALL=(ALL:ALL)ALL***     to    < username >       < pest here>
     # User Privilege Specification.
	   *root          **ALL=(ALL:ALL)ALL***
       solace1     **ALL=(ALL:ALL)ALL*** 
so, now soalce1 user can access the *sudo* command, so login to solace1 and check it by using *sudo.*
#### linux file permissions
- Every users have **owners and permissions**
- **Owners**: file creators(user and group). eg.     solace1 solaces
- **Permissions**: allowing a permissions to users, groups and others.
Use the **ls -l** then get detail information: 
     **permissions              user    group       size          date                filename**
eg.    *-rw-r--r--         1     solace1 solaces     4096       Dec 19 10:43       file.txt
     drwx-wxr-x      2     solace1 solaces     4086       Mar 10 05:00       fold1*
 so, you get 5 main parts: permissions, owners(user, group), Date, size, and filename.
 - To change the owners of files use the command: *sudo chown < username >:< groupname > filename*
     eg.    sudo chown solace2:solaces file.txt
          sudo chown solace1:solaces fold1
        then, check by **ls -l**. now *solace1* can run fold1 and *solace2* can run file.txt file. but
        the other users can not run this.
#### Permissions: read(r), write(w) and excute(x)
**NB.** *folders and files* are start with *'d' or '-*' respectively. 
      Eg.   d--xrwx---    ,or      -rwx--xrw-
NB.    drwxr-xrw- ....this is for 3 user types respectily by deviding into 3 parts.
         eg.       rwx=for user(U),    r-x=for group,    rw-=other.
eg.   *r-w*  ...can read and excute, not write.
- To change permissions use: **sudo < parameters >**  < flename >
     eg.    chmod +x file(fold)    ...added x-permission to all(u, g and o).*
         or similar with    *chmod a+x silename*
 chmod: helps to change the file parameters :      sudo chmod < parameters > < file name>
- **Numeric representation and symbolic** representation of:
     rear = 4 =r
     write= 2 =w
     excute= 1 =x
 eg.   *chmod a+x file.txt*        ..give *x permission* for all(u, g, o).
     *chmod g+r file.txt*        ..give *r permission* for group.
     *chmod u+x file.txt*        ..give *x permission* for user.
     *chmod 0-w file.txt*         ..removes *w permission* for group.
   bestEg.  
    *chmod a+rwx, u-rw, g-x, o-xw file.txt*    
     ...first gives rwx to all(u,g,x), then removes rw from u, x from g and xw from o.
        so,the permission will be:   ---xrw-r--
 - Using **numeric** we can give permissions: 
  eg.  *chmod 621 file.txt*     ...6=4+2 (r and w)
                       2=w   and
                       1=x.
                    therefor, gives:  -rw--w---x  to file.txt
eg.   *chmod 777 fold1*     ...gives 'rwx'  to all(u,g,o).
                     b/c   7=4+2+1  means(r,w,x).