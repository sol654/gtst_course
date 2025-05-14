-  2nd step of phase of Ethical Hacking.
 - To check the gathered informations if real or to collect more additional informations.
 - Active phase of probing identifies vulnerabilities, services, open ports, and more.
 - Scanning focus more on **system** than peoples.
## The Reconnaissance VS Scanning
#### Reconnaissance
- Focuses on broad, highlevel info about the target.
- Publicly available addresses and domain names. Organizational structures and employee details( Social engineering issues ).
- Website vulnerabilities, exposed subdomains...
#### Scanning
- Focuses on technical, low-level and details about target systems.
- Open ports, services, OS, service versions, Network topology..
- Specific vulnerabilities in the systems and services.
  

- [ ] **Why do we do scanning?**

    - It helps to Identify HOST’s System informations

         - Operation System

         -  Service versions

    - To Discover Open Ports

    - To Discover Live Systems

  
  

#### Network Scanning

● This is a method of Scanning a network and getting more informations.

● There are Many kinds of scanning methods and tools for different purpose.

- ○ For Network mainly: NMAP,netdiscovery

- ○ For Subdomain: Sublist3r,subfinder,amass

- ○ For website: Nikto, Nuclei, Nessus..


  

## Nmap - Network Mapper

- ● Nmap is A network **scanning** and exploring tool used by network and security experts.

- ● It is used to scan **Network,Ports,OS**,...

- ● It is made for ***windows*** and ***linux***

- ● On kali linux it is built in tool.

- ● To check the existence of nmap on your system = `nmap --version`

- **NB**. To download for windows: www.nmap.org

#### Live System Discovery

 - Discovering live system means, Checking up and running hosts(clients/servers) on a network.
- We use ping for getting "IP",  but HOW IN WORKS?
  

#### Ping Sweep

- ● This is a method of checking if host is up or down.

- ● It uses ICMP(Internet Control Message Protocol) packets for checking purpose

- ● It sends Echo request and waits for response if there is **Echo reply** then that system is up!
- To check the server is 'up':
```
ping google.com      ...you can use domain name
ping 123.0.0.1       ...or use IP address of the server
```
  Then, It tells the **ICMP_SEQ**(Internet control message protocol _ sequence`[order: 1, 2, 3...]`). If there is the missed number, there must be "**Down**" message.
  

```

➔ From echo requests we can gather the following informations

◆ OS type

● Windows ( 32 byte )

   ○ ttl=108

● Linux ( 64 byte )

   ○ ttl=64

◆ Connection stability

● Time

NB. By looking the TTL and the byte, we can identify the OS. but not always.

Mostly used for blue teaming purpose. but not always bc they are chengable.
```

- [ ] **➔ TTL : time to live**

- ◆ determines how long a packet should exist in the network before being discarded

- ◆ **Decrementing TTL**: Each time the packet passes through a router (a hop), the TTL value is decreased by 1. After passing 64 routers, becomes 0. 

- ◆ **TTL Expiration:** If the TTL reaches 0, the packet is discarded, and an ICMP "Time Exceeded" message is sent back to the sender.

- And also the **Time** tells the delaying time of the process.
  (request to server and then replay to host).
```
In linux the result of ping is like this:

~>  ping 192.168.11.12

<  PING 192.168.11.12 (192.168.11.12) 56(84) bytes of data.
<  64 byte from 192.168.11.12: icmp_seq=1 ttl=64 time=1.54ms
<  64 byte from 192.168.11.12: icmp_seq=2 ttl=64 time=0.64ms
<  64 byte from 192.168.11.12: icmp_seq=3 ttl=64 time=2.84ms

NB. If the order of icmp_seq order is missed or other format of output is contained bn these messages, there must be DOWN message.

```


#### Nmap ping sweep

- ● Nmap can perform ping sweep too.

```

● Syntax:

    nmap -sn IP        ...-sn(no port scan)

```
 Then, tells "It Is UP" and "Latency time" & also "How many hosts are UP" and total time.
  

- [ ] **How do we Identify all hosts on a network?**

- ● ping can take 1 host only??

- ● Nmap can scan the whole range.

- ● You can do the ping sweep with little modification on the IP

```

● Syntax:

 nmap -sn NetworkAddress-255

 nmap -sn NetworkAddress/networkBits(subnet mask)   ..CIDR notation.

```
NB. The Network Bits depend on the IP class /subnet/.
- **NB**: This will **not work on Virtual Machine** network. use: **Wifi-Adapter**. or u can use liveboot, dualboot, mainboot... <br>
**Example**: Find how many users are UP or DOWN in your wifi, using your wifi IP.<br>
**SOL/N**: 
- First check **the IP**:  `ip a`   wlan1-->inet,  let: 192.168.9.9/24 
- To check the **whole users**:  `nmap -sn 192.168.9.0/24`
- We can get the IP of the users and tells "UP".
- **OR**, we can use:   `nmap -sn 192.168.9.0-255`

#### warning++

- ● Some Organizations or system admins, will block any **ICMP** requests in Firewall.

- ● Here the ping sweep wont work, and when you try this it says “host is down” but it is normally up.


● To make it work we just skip(Jump) Ping requests and ask for additional things:
```
Syntax:

   nmap -Pn IP

```
**EG**.  `nmap -Pn 192.168.8.0/24`

- ● This method will Jump host discovery because it will take the ip as Up and try to do port discoveries.
#### Nmap works
**Eg**. `nmap scanme.nmap.org`
1. live discovery (Host Discovery): check if live(**UP**), then,
2. Open port discovery and then lists **states** and **services**.
- If nmap is running click any key to look the percent.
- **Nmap**: works additionally "DNS Resolving"(change domain name to IP address).
# Port
## What is PORT?

- ● Port is ***process-specific*** or an ***application-specific*** construct serving as a communication ***endpoint*** by (TCP/UDP), which is used by the Transport Layer protocols of Internet Protocol suite, such as User Datagram Protocol (***UDP***) and Transmission Control Protocol (***TCP***).
## Two types of Ports
1. **Physical Ports**: used for pluging socket kind things in our computer. eg. (flash, USB, Earphone... )
2. **Software Ports**: we mainly talks about them. (logical ports). like: doors for services, applications... etc logically.

- ● **PORT** is like a door for some purpose/service. 

- On computer there are different **65,536** ports with different job(like the window and door)

- ● **1-1024** = reserved(well known) ports

```

Example:

● HTTP(80) - unsecured Web port

● HTTPS(443) - secured web port

● FTP(21) - File transfering port

● SSH(22) - Secure shell port

```
  

#### Port status

- [ ] **Ports can be on different status**

- ##### Open ports

○ THESE are ports open for accepting any requests.

○ Having an open window can lead to any kind of gas(ጭስ) or air getting to our house.



- ##### Closed ports

```

○ THESE are ports which not accepting any request but there is some service running on it.

○ Ex: Having your home door close.

      ■ still the door helps sometime, but not for now

```

- #####  Filtered ports
○ These are ports which nmap is not sure of being open or closed.
  
#### Open port discovery

- When you access **websites** port(80, 443, 8080) are open mostly.
- For **servers** port 22(ssh) is open mostly.
- Without Intention forgot closing, leads to attack.
- ● We can use nmap to check which port is **open/closed**

- ● And this is called port discovery

```

● Syntax:

    ○ nmap IP(Domain)      ..=> only the 1000 ports

    ○ nmap -p port1, port2, port3 IP(Domain) => only port 1,2,3

    ○ nmap -p- IP(Domain) => All the 65K port

```
**NB**. **Port Scan**: works by sending a connection(TCP request) to specific port.
##### Blue team Perspective
From similar IP sends dt ports to the computer. this shows that the person trying to scan open ports.
## Netcat

**We can use Another Trick with netcat**

- *if we want to connect with another ip adderss by port*.
- **NB**. Using python we can connect dt ports using socket.
```
Syntax:  nc -nv IP port   ...tells OPEN or FAILED(connection refused)
nc -nv 192.168.1.3            ...if open connects(succeded)
```
NB. Options can be first or next.. no problem.
- EG. `nmap -p 1000 google.com`   ==  `nmap google.com -p 1000`


# Scanning methods

- [ ] **Nmap scans network in different modes**

   1. TCP connect (TCP scan)

   2. TCP SYN (Stealth scan)

   3. UDP scan

   4. Xmas scan

  

# TCP Scan

-  This is Nmap’s Default Scan.

-  it is reliable

- It is connection oriented.

-  This is Because it uses 3-way HANDSHAKE!!!

  

- [ ] **● What is 3-way handshake?**

   -  When you establish a TCP connections there is something going behind the scenes

   -  What was the packet sent while the Ping sweep, it was the ICMP.

    - ○ Here When we start connection we will send a Synchronization flag.

    - ○ When the server got and accepted our request it will reply with Synchronization and Acknowledgment.

     - ○ Finally, we will send Acknowledgement or Reset(RST) and continue because we have connection/network now.

  

```

CP scan works like this, so nmap will send the SYN request to the

ports and if they reply with SYN/ACK nmap will reply with ACK

BOOM!!! That port is open!! Else the port is closed/filtered.

  

Syntax of tcp scan:

      nmap -sT IP

```

  

EXAMPLE :- 
```
nmap -sT google.com
```

- [ ] **Red Teamer Perspective**

  - **Note**: By Default Nmap Performs ***TCP*** Scan Whether You provide ***-sT*** or not

  

- [ ] **Blue Team Perspective**

   -  As you can See there is A 3 way Handshake this means, this scan is a TCP scan.

  

#### Stealth Scan.

- ● This is TCP scan but here we dont send the last ACK flag.

- ● But we send the RESET flag.

```

● Syntax:

    sudo nmap -sS IP

● Example:

    sudo nmap -sS geezsecurity.com -p 80, 8080, 13
```

It checks open ports but don't make a connection, early. but now a days, at first stage at first stage when we send syn, it will be registered.
