### Nano Text Editor
**GNU-nano:** user friendly, pre-installed, open-source, and free.
eg.    *nano nano.txt*       then:
- ctrl + S = save
- alt + E = Redo
- alt + U = undo
- ctrl + X =exit
others:
- ctrl + shift + c = Copy
- ctrl + shift + x = Cut
- ctrl + shift + p = pest
NB. in nano editor *^ = ctrl* 
In NANO file If there is astricx means, file is not saved.
- **ctrl + r**    ...to append other files content read to our text file using **path**. 
eg. open nano file then click  *ctrl + r*  then enter the path of the other(appended) file.
### linux user management
- Every user has group.
- If you create user, group also be created. so you can add other users in to the group.
- each user has their own files and applications.
- **command** for to know the current **user** is   *whoami*
- to add user use command    **sudo adduser solace1**
NB. *adduser* needs some detailed information.
- The first user(eg. solace) has greater power.
      Root id = 0
      Normal User id = 1-999
      eg.  1000    ...id for first user.
         1001   ....2nd user id
         1999   ...last user's id
     eg. 1998 ...is ID for 999's user.
     **NB**.  *sudo adduser xy1*    ...needs detailed information.
         *sudo useradd xy2*    ...simpler
     NB. To create user go to **/home** and be in **su**  or use **sudo**.
 If you create user with *useradd*, it will not create a home directory for user. 
 */etc/skel*   ...files for new users to make them user!
 In *adduser*, If you don't need some information, just click **enter**.
 **NB**. If **[Y/n]**, if y is capital, by default you can click **enter** to say *yes*.
 - */etc/passwd*    ...users file and about newly created any useradd or adduser user files.
 - /etc/shadow   ...passwords of users but (encrypted password).
       eg.   *sudo cat /etc/shadow*       ....it needs sudo bc shows passwords of users.
           *cat /etc/passwd*              ....shows user Id, group Id... and other infos of users.
If user id is full(1999), to add new user start the id with 2.   eg. 2000
NB.   if you create user with *useradd*, the user's shell type is **sh** and has no **password**.
     but, *adduser* user's shell type is **Bash** by default.  check:   *cat /etc/passwd*
 - I you want to use **cat /etc/shadow**, be in root or use sudo.
          eg. *sudo cat /etc/shadow*
- To know ID, use command '*id* ' in /home directory.
       eg.  *id*               ...shows the current user's id.
          *id root*          ......the id is 0. bc it is root.
          *id solace*       ...shows is of *solace* user.
*id* command shows *uid=user id,   gid=group id......*.