- **Nmap scann result**  `nmap -sV -Pn wgel_host -vvv`:
```bash
Nmap scan report for wgel_host (10.10.197.75)
Host is up (0.22s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel



```

so it has a website(http) and open SSH port(we can connect remotely).

- **when I bruteforce the directories i got interesting file .ssh** <br>
` dirb http://wgel_host`
```bash
==> DIRECTORY: http://wgel_host/sitemap/.ssh/  
```

- **when I browse** 'http://wgel_host/sitemap/.ssh/' I got private key:

![[1.png]]
![[2.png]]
I saved it in txt file(id_rsa).
![[3.png]]
Then i gave a proper permission for the file:
![[3.1.png]]

- **I got the username from the "view page source" of wgel_host**
```c
<!-- Jessie don't forget to udate the webiste -->
```
so, **jessie** is the username.


- **Now I have connected with ssh**:
![[4.png]]


- **To get the user flag just locate it**:
![[5.png]]
![[6.png]]
User Flag = 057c67131c3d5e42dd5cd3075b198ff6

- **To get the root flag you have to you have to use 2 terminals for finding the flag in /root and to listen the responses** NB. Use your tun IP to listen:
![[7.png]]
The Root flag = b1b968b37519ad1daa6408188649263d


## BOOM BOOM BOOM!!
Finally I did it!
![[8.png]]

**Name**: Solomon Tesfaye
 ETHICAL HACKER
