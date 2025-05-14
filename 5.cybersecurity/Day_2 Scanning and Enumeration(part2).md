# UDP scan

- [ ]  This is a method to scan if any service/port is using UDP

- [ ] protocol like: **SNMP** 
- **NB**: HTTP needs **TCP**.

- [ ] ● when speed is necessary. like stream

- [ ] When we send UDP packet to server, If the response is:
- UDP response: **OPEN**
- ICMP response: **CLOSED**
- ICMP unreachable: **FILTERED**
- No response: **OPEN / FILTERED**<br>
**NB**. Mostly we will consider: **closed**, **filtered**, **open / filtered**...  are **Closed Port.**
```
EG.   sudo nmap -sU 192.169.56.1
```

```

● Syntax:

     sudo nmap -sU IP

-There are some ports work on UDP, SO we need UDP scan SO when you do Pentest do UDP and TCP scans together:-

● Syntax:

     nmap -sU -sV -sS 192.168.28.104

```

**MIXED EXAMPLES**: We can use stealth(TCP) and UDP.
```
So/n:   sudo nmap -sU -sT google.com
        sudo nmap 192.168.52.1 -sT -sU
```
  **NB**. As blue team: we can see udp requests.
  

# Xmas Scan

- ● Here, The 1st thing to send is ***FIN/PSH/URG*** instead of ***SYN***.

- ● If there is response like **RST flag** Then the system is **close**

- ● If there is **no response** the system is **open**.

```

● Syntax:

    sudo nmap -sX IP

Eg:  sudo nmap -sX 192.168.7.9
```

- [ ] **Red Teamer Perspective**

- Mostly we will consider: **closed**, **filtered**, **open / filtered**...  are **Closed Port.**
- If the result is **OPEN**, the port is **Open**.

- [ ] **Blue Team Perspective**

- The server shows `[FIN, PSH, URG]` instead of SYN request.

  
  

## SUMMARY

### **Nmap Scanning Methods:**

1. **TCP Connect (TCP Scan):**

    - A full three-way TCP handshake is performed (***SYN → SYN/ACK → ACK***).

    - Reliable but easily detected by firewalls and IDS.

2. **TCP SYN (Stealth Scan):**

    - Sends only a SYN packet;

        - if SYN/ACK is received, the port is open;

        - if RST, it's closed.

    - Does not complete the handshake, making it stealthier than TCP Connect.

3. **UDP Scan:**

    - Sends UDP packets to the target;

        -  if no response, the port is assumed open or filtered;

        - ICMP "port unreachable" indicates it's closed.

    - Slower and less reliable due to firewalls and packet filtering.

4. **Xmas Scan:**

    - Sends a TCP packet with ***FIN, URG, and PSH*** flags set.

        - If there is no response, the port is considered open;

        - RST means it's closed.

    - Effective against older systems but easily detected.

  
  

# Operating System Detection

- A technique used by Nmap to identify the operating system (OS) and version running on a target machine.

```

● Syntax:

   ○ sudo nmap -O IP       ...OS detection only

   ○ sudo nmap -A IP       ...OS detection including version

● Example:
  ○ sudo nmap 132.78.89.89 -A
  
```


  

# Banner Grabbing

- ● Banner Grabbing is a technique of ***Exfiltrating*** Version of some Service.

- ● The "**banner**" refers to the ***text or metadata*** that a service or application sends back when you connect to it, which often contains details about the *software, its version, and sometimes even the operating system.*
- **Banner Grabbing** means getting version. so, this is called: **Version Enumeration**. 

```

● We Use -sV Flag to get the Version and Service Detail

● Syntax:

     ○ nmap -sV IP

○ Example:
    ○ nmap -sV 192.168.78.2     ..displays port versions
    ○ nmap 192.168.78.2 -sV
```

  Or, Using **netcat**:
```
  syntax :  
      nc IP port      ...for fixed port.
  Example:
     nc google.com 80       ...displays:  8:0.41-0ubuntu0 0.24w
```

For a **single port** with **nmap**: 
```
nmap localhost -sV -p 80
```

For **website**: 
```
whatweb IP
```

## Scan Speeds

- ● When nmap do its scan, it have a time waiting, after sending 1 packets to a host.

- ● There are 5 time waitings.

```

● The nmap time template is -T<0-5>

○ Insane -T5 = waits only 0.3 seconds for the response. After 15min nmap gives up.

○ Aggressive -T4 = waits only 1.25 seconds for the response. recomended.

○ Normal -T3 = This is a default nmap timing. 

○ Polite -T2 = This are the slowest timing. not been detected.

○ Sneaky -T1 = Slow scan, waits 15 seconds between probes. not been detected.

○ Paranoid - T0 = waiting 5 minutes between sending each probe.

  

their syntax are:-

    nmap -T<0-5> IP

Eg:
    nmap -T4 google.com
    nmap -p- geezsecurity.com -T5

```

  

# Nmap Script Engine( NSE )

- ● Nmap is capable of running some script on ports and services.

- ● These scripts are written in **lua-programming language**.

- ● These scripts are located in **/usr/share/nmap/scripts**

- ● Nmap contains a total number of 589 scripts (Version 7.70), there are a lot of scripts that are useful but not all of them works perfectly, it’s like other tools a better for that particular task, so we’ll look at how we can use the powerful NSE and what scripts to use.

```

● You can Write your own script too if you can do lua

● Syntax:

   ○ nmap -sC IP

   ○ nmap --script scriptname.nse IP

   ○ Nmap -p 22 –-script ssh* IP         ..use the scripts name start with ssh
   
   ○ Nmap –-script vulnerse.nse localhost    ...extension .nse is not neccessary
```

Best Example:
```
nmap -sV -A -sS -p 21 10.1.1.1 --script ftp\*_


-> This scans -sV(version, banner grabbing), -A(OS with Version), -sS(stealth scan), -p(port), --script ftp\*_ (scans NSE scripts start with ftp).
```
##### Some Known Scripts:
- [ ] **`--script banner`**   (grabbing some details)
- [ ] **`--script broadcast`**   (reveals broadcast informations)
- [ ] **`--script vuln`**   (test if the ports are vulnerable)
```
Eg:
nmap -p 80 --script banner
```

# Nmap Outputs

- [ ]  Nmap Can Save your output using the “***-oG|-oX|-oN”***

    -  `-oG` -> For Greppable formats

    -  `-oX` -> for xml formats

    -  `-oN` -> for Normal Saving Formats

```
  eg:
>  nmap 192.168.1.2 -oG xx.txt    ..we can grape it(grape xx.txt)
  
>  nmap 192.168.1.2 -oX xx.txt    ..to check with softwares
>  
>  nmap 192.168.1.2 -oN xx.txt    ..similar format with the output
```

# Nmap Verbose

- ● Displaying More Information and Logging them is called Verbose.
- Those informations are run in the background.

```

● You can also add -v flag to Call verbose

     ○ -v - little detail

     ○ -vv - more detail

     ○ -vvv - much more details(more recommended)

```
```
Eg: 
>  nmap 120.1.0.1 -sC -v   ...displays each steps

>  nmap geethsecurity.com --script vuln -T4 -vv -oN geezsecurity.txt
```

## Nmap firewall evasion

**Evasion**: means avoid.
**Firewall Evasion Techniques**: Using nmap bypassing or circumventing firewall protections using the Nmap tool.
- Evade detection by **firewalls** or intrusion detection systems (**IDS**).
- **IDS** (Intrusion Detection System) is a security technology designed to monitor network traffic or system activities for signs of malicious behavior, policy violations, or other unauthorized activities.

### Firewall Evasion Techniques

1. Decoy Scan 
2. Fragment packets 
3. MAC Address Spoofing 
4. Source Port Manipulation


## 1. Decoy Scan

- By creating many fake IPs, send request to one port. so blueteamers can't identify our IP which one is the right IP. 
- You can **specify multiple decoy IP addresses** using the -D option within the Nmap command. 
- 
```
>   nmap -D decoy1, decoy2, decoy3 .... [Target IP]
```
- You Can Make Nmap to **add some random IPs** 
```
>   Nmap -D RND:5 … [Target IP

...This can create randomly 5 IPs

```

```
example:
>   sudo nmap google.com -D RND:5
```


## 2. Fragment Packets

- Fragmented requests refer to the technique of sending packets in smaller fragments rather than as whole packets.
- This is done to **evade detection by firewalls, intrusion detection systems (IDS), or intrusion prevention systems (IPS)** that rely on analyzing entire packets to detect malicious activity.
- To Perform this:
```
>   nmap -f -p21 [Target IP]
```

```
eg:
sudo nmap google.com -f -p80 -vv
```
**Blue Team Side**: hides us, server shows fragmented IP.


## 3. MAC Address Spoofing

- By changing our MAC, bc If MAC is blocked we can't do anything, so we must change it to another fake MAC.
- To do this:
```
  nmap -spoof-mac Apple/MAC_ADDRESS -Pn IP
```

```
sudo nmap google.com -spoof-mac Dell -pn  -p80
```


## 4. Source Port Manipulation

○ You can Take Your Home. Then You went to Mini-Market(Suq). 
- ■ Source IP: Your Home | Destination IP: Suq 
- ■ Source Port: Your Main Gate | Destination Port: the suq window

- [ ] ● The source port identifies the specific application or process on the client device that initiated the communication. 

- [ ] ● The destination server uses the source port of incoming requests to send replies back to the correct application on the client.

- **Example**: A client's HTTP request might use source port 12345, and the server sends its response back to this port.

- **NB**: If the other ports are blocked and one port is available to enter, we use the manipulated port. there fore by this technique the unallaweded(actual) port gains access to enter.
- **To do this**:
```
 >   nmap -g [PORT] -p 21 IP
```

```
EG: 

>   sudo nmap google.com -g 8080    ...enter with 8080 only if                                                                 the allowed port is 8080.
```
**NB**. Nmap using random ports, when we don’t specify specific one

