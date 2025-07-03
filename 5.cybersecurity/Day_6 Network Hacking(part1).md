
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

