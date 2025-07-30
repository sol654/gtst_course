# Anonymity & Blue Teaming

## Anonymity

**Anony**/unknown means **የማይታወቅ** in amharic
- When Black Hat Hackers do Security tests / Cyber Crimes on some target, They will be unknown 
	- This is because they are doing illegal things so they try to Hide their Identity and be anonymous/የማይታወቅ ሰው
- **Anonymity** is Needed in Cyber sec, So when you perform Different tasks Your Identity can be Exposed and this is A Big Problem.
- Keeping your identity private is safe practice. 
	- For example, using a fake name to post messages to a social media platform.
- Anonymity is Simply using a fake Profile/Location/Identity/personality

## Online Privacy

- **Incognito/privacy** tabs in browsers.
- These Programs are simply not logging what we are doing(aka history,cache,cookie) but still the site we visit with this program will have our ip and other informations also our ISP/internet service provider/ will know. 
- Therefore, they dont give as real privacy. So how can we get that?

## Methods of Anonymity

There are several ways to be protected or to be Anonymous on the internet. 
- These methods can change our identity,location or personality.
	1. Proxychains
	2. Tor Network
	3. VPN 
	4. Mac change 
	5. Incognito 
	6. Secured OS 
	7. Temp mail 
	8. Botnets

## What is Proxy Server?

- A **proxy server** is an intermediary server that separates end users from the Server they Access.
- It provides varying levels of functionality, security, and privacy depending on the use case. 
- Proxy means intermediary/መካከለኛ

## Purpose of Proxy Server

- Anonymity 
- Traffic filtering 
- Load balancing 
- Caching

## Types of Proxy Server

While all proxy servers give users an alternate address with which to use the internet, there are several different kinds each with its own features.
- Forward Proxy 
- Reverse Proxy 
- Transparent Proxy

## Forward Proxy

Sits in front of clients and forwards client requests to the internet. 
- It provides IP address security for those in the network and allows for straightforward administrative control.
- Use Cases:
	- Bypassing geo-blocks 
	- Managing the Network Devices

## Reverse Proxy

Sits in front of web servers and forwards client requests to servers.
- Use Cases: 
	- Load balancing 
	- Web acceleration 
	- Application firewall / WAF

## Transparent Proxy

A proxy that does not modify requests or responses; users may not be aware of it.
- Use Cases:
	- Caching 
		- can cache frequently accessed content to improve network performance by reducing bandwidth usage and speeding up access to commonly visited sites 
	- Content filtering / IDS-IPS 
		- For blocking access to specific websites or content.

## Anonymous Proxy

- Masks the client's IP address but identifies itself as a proxy. 
- An anonymous proxy focuses on making internet activity untraceable.
- It works by accessing the internet on behalf of the user while hiding their identity and computer information.
- Use Cases:
	- Basic anonymity without full stealth

## Proxy Protocols

Proxy servers operate using a variety of protocols depending on their intended purpose and the type of traffic they handle.
- **HTTP** Proxy 
	- Handles HTTP traffic. It is used for web browsing, content filtering, and caching.
- **SOCKS** Proxy (SOCKS5, SOCKS4)
	- A general-purpose proxy that works at the transport layer. It can handle any traffic type (e.g., HTTP, HTTPS, SMTP, FTP). 
	- Forwards raw data between client and server, without interpreting it. 
	- SOCKS5 supports authentication, making it more secure than older versions(SOCKS4).

## ProxyChains

- We have seen what proxy is so lets see what Proxy chains are. 
- Proxy chain is simply a chain of proxies. 
- We have a lot of proxy lists so our request will pass through lot of proxies. 
- This will hide our IP and makes us anonymous.
```
eg. 

70.248.28.23 -> 10.248.28.23 -> 65.28.28.24 -> 20.248.2.23 -> 54.56.127.161 -> 154.16.127.161
```
- Here our 1st IP was **70.248.28.23** but the Internet(webserver,...) know as **154.16.127.161**.

## Types of ProxyChains

Based on the Sequence of Proxy Servers we follow on the chaining process, There are 4 Types of proxychains.
1. Dynamic chain 
2. Strict Chain 
3. Round Robin Chain 
4. Random Chain

## Dynamic Chain

- Dynamic Chaining is That way the proxy Servers are chained is as the proxy list given. 
- If there is **any server that is not working** it will be **skipped**. 
- If **any of them doesn’t work** it will be broken and **display errors**.

## Strict Chain

-  All Proxies chained in the order as the are listed. 
- All proxies Have to be up and working, if **one server is not working** it will **display error**.

## Round Robin chain

- It **follows the order of the proxy list** .
- It will **skip if 1 proxy is not working** .
- If all the proxies not working it will **start again and check them**.
	- This makes it different from Dynamic chain.

## Random Chain

- It will choose some Proxy server Randomly and creates chain in random order. 
- Not working will be Skipped! 
- Each Request will be in random sequence of servers.

## Setup

1. Find some Proxy servers to use. 
		- a. google.com 
		- b. https://geonode.com/
		- search "free proxy servers list"
	- Getting Working Free Proxy Server is hard. 
	- Hackers Most of the time Buy Some VIP servers, so they can do anything they want.
	- https://proxyscrape.com/free-proxy-list
	- If you need Paid Proxies: https://floppydata.com/
2. **Open /etc/proxychains4.conf** 
	- A. Turn on any kind proxychain you need 
	- B. Put your proxy servers with format of :
```
<Protocol> <IP> <PORT> <UserName> <Password>

http    192.168.0.3 1810 lamer secret
socks5  77.22.34.1  1080 justu hidden

or if no password and username use:
<Protocol> <IP> <PORT> 

http    19.18.07.3  1810
socks4  77.22.34.1  1080
```

3. Accessing with proxychains
	1. Add “**`proxychains`**” in front of any command.
- Find a working proxy server and you are good to go!
```
~>$   proxychains nmap scanme.nmap.org
~>$   proxychains curl ifconfig.me
```

## T.O.R/The Onion Routing/ Network

- **Tor** is a free overlay network for enabling anonymous communication.
- Built on **free and open-source software and more than 7000 volunteer-operated relays worldwide**, users can have their Internet traffic routed via a random path through the network.
- Tor was initially conceptualized in the mid-1990s by the United States Naval Research Laboratory (US NRL).
- It was **developed for the military to protect sensitive communications and enable anonymous intelligence gathering**.
- Initially called "**Onion Routing**," referring to the **multiple layers of encryption** involved

## How Tor Works

- **Tor Nodes**: A node in a network is any device or point that can send, receive, or process data. 
	- **Entry Node**: The **first relay**, which **knows your IP** address but not your final destination. 
	- **Middle Relays**: **Multiple intermediate relays** that obscure your traffic route. 
	- **Exit Node**: The **last relay** that **decrypts the final layer** and **sends your traffic to the destination server**.
- **Tor** can be **slower** than traditional browsing **due to multiple relays**.
- **Onion Encryption**
	- Data is encrypted in multiple layers, each decrypted at a different node, hence the “onion” analogy
		- Each relay (node) in the Tor network has a public-private key pair/RSA/. 
		- When your data is routed through the Tor network, the client (your device) encrypts the data multiple times, using the public keys of the nodes in the path.

## TorGhost

- Clone it from github  https://github.com/SusmithKrishnan/torghost
- Install tor
- Open it! 
```
>	sudo apt install tor
>	git clone  https://github.com/SusmithKrishnan/torghost
>	sudo pip install requirements.txt
>	sudo python3 torghost.py
>	sudo python3 torghost.py --start
>	sudo python3 torghost.py --stop
```
- Your last Proxy IP will be shown(Public IP)

## VPNs

- VPN means Virtual Private Network. 
- a service that helps you stay private online. 
- A VPN establishes a secure, encrypted connection between your computer and the internet, providing a private tunnel for your data and communications while you use public networks 
- Some VPNS’s doesn’t log user data, That bases on the Policy of the VPN
- There are a lot of VPNS, those are paid and free 
- The paid are more secure and private, There are Some Good Free VPNS 
- Example: Nord VPN, Proton VPN, windscribe VPN,..
- NB. Buying premium VPNS are good

## Types of VPN

### A) SITE to SITE

-  This is most commonly used to join company networks together over the Internet 
- Allowing multiple locations to communicate over the Internet as if they were local. 
- Router + Routers

### B) Remote Access VPN

- Involves the client's computer creating a virtual interface that behaves as if it is on a client's network 
	- **Hacking game** utilizes **`OpenVPN`**, which makes a TUN Interface letting us access the labs 
- When analyzing these VPNs, an important piece to consider is the routing table that is created when joining the VPN.
- it give Additional Network Interface: **`tun0...`**
- These are all my Interfaces on my computer. 
- Foreach interfaces to work and communicate with the router they need to have Routing paths. 
- The Routing Tells To the Computer, that if user requested a data with IP A, it knows which path/route to follow Based on the IP network.

### C) SSL VPN

- Essentially a VPN that is done within our web browser and is becoming increasingly common as web browsers are becoming capable of doing anything.
- a VPN that uses SSL/TLS protocols to create a secure, encrypted connection, allowing remote users to access a private network over the internet through a web browser, without needing specialized client software

## Types of VPN Protocol

- A VPN protocol is the set of rules that govern how data moves between a VPN server and devices connected to it. 
- Every VPN uses a form of encryption to achieve a secure, private connection, but the rules and procedures for creating this connection are established by a particular protocol, each with its own pros and cons.

### 1. OpenVPN

- OpenVPN is a cryptographic protocol that emphasizes security. 
- It’s open source, so users can check for themselves that there’s nothing within the protocols that will compromise their security, and it’s even possible for make modifications tech-savvy users to 
- Sometimes, firewalls can interfere with VPN network access, but OpenVPN is designed to avoid this kind of conflict.

### 2. IPSec / IKEv2

- Internet key exchange version 2 (IKEv2) is often used in combination with Internet Protocol Security (IPSec). 
	- IKEv2 forges a secure tunnel connecting the user to the VPN server, while IPSec provides the encryption and authentication.
- IKEv2 is among the fastest VPN protocols around, making it attractive for VPN users who prioritize speed and streaming.
- IKEv2 is among the most dependable protocols, providing a strong connection to the VPN even when the internet momentarily drops, meaning you don’t have to constantly check if your VPN is working. 
- Although some open-source versions are available for other platforms, IKEv2 was primarily designed for Windows users.

### 3. WireGuard

- Like OpenVPN, WireGuard is an open-source VPN protocol. 
- It’s a relatively new option with promising performance, but it’s still under development and is something of a work in progress. 
- Efficient encryption and high performance make WireGuard one of the fastest VPN protocol options available. 
- WireGuard uses lower bandwidth, making it an ideal solution for mobile.

## Mac Changer

- As We saw MAC address can tell about our Device. 
- SO , if we changed that we can change our device id.
```
>   sudo ifconfig wlan0 down   # It is the first step always
>   sudo macchanger -r wlan0   # change mac with random mac
>   sudo macchanger -s         # Tells current mac and permannent mac
>   sudo macchanger -m 00:ef:3f:aa:ab:cd wlan0  # add your specific MAC
>   sudo ifconfig wlan0 down   # finally down it.
```

## Incognito mode

- This is a mode that browsers have. 
- This will help you to have a browser without logging your history,cookies,cache,.. 
- This will help you when you are try to surf some site but if you don't need the site to know your identity, you can use this because it doesn't have any recording process.
- For firefox: **privacy tab**

## Secure OS

These are Operating systems, that have a security and privacy feature. 
- Windows and Mac OS will record some of your activity also they are not good on privacy and security .
- There for the always Best OS Linux is always recommended when you think about privacy and Security.
- Like,
	- ○ Tails OS    ...like liveboot
	- ○ Whonix OS 
	- ○ Qube OS

## Tails OS
![[Pasted image 20250728072327.png]]

## Temporary mail

While You do some pentest you don't have to expose your email and profile for this purpose u need fake emails, 
- but if you don't have to time create one you can use fake email providers. 
- https://temp-mail.org/ 
- It have a browser extension too

## True anonymity is hard

-  Every server you connect to on the internet,can be a web server, a mail server, or a VPN server, can Expose your IP address. 
	- This is a number that uniquely identifies your internet connection and can be easily traced back to you. 
- Achieving true anonymity on the internet requires good operational security (OPSEC) on your part to ensure your real IP address is not revealed. 
	- Operations security ( OPSEC ) is a process that identifies critical information to determine whether friendly actions can be observed by enemy intelligence 
- Tools that can hide your IP address and protect anonymity include VPNs and the Tor anonymity network, but there’s no solution that can guarantee 100% anonymity. 
	- Tor is sometimes considered to be more anonymous than VPNs due to its decentralized nature, but it comes at the cost of lower performance, ease of use, and stability. 
- Full anonymity is difficult because you must always use anonymity tools for all aspects of your online life, as even a temporary lack of anonymity is sufficient to expose your identity.

## Deep web

- The deep web refers to all the web pages and data that are not indexed by search engines and cannot be accessed through traditional search methods. It includes content that is protected by passwords, databases, and other security measures. 
	- **Examples**: private email accounts, online banking portals, subscription-based websites, and more. 
- Essentially, the deep web is the part of the internet that is not easily accessible to the general public. 
- Developers If they Don't want their site to be Accessed(indexed) by Search Engines they will Include that path in a file called “robots.txt”.

## Robots.txt File

![[Pasted image 20250728073405.png]]

## DARK WEB

- The dark web is a part of the internet that isn't indexed by search engines like deepweb, but this kind of web works on TOR networks ONLY. 
- The dark web is a small portion of the deep web that is intentionally hidden and requires specific software or configurations to access.
- It is unique type of internet world.
- Their **TLD** is **.onion** , this is because it uses TOR networks.
- Also this kinds of links won’t be opened by normal browser.
- For this purpose we need a special .onion Client browser, 
	- **Example**: Tor browser, Onion Browser.
- There are Many Kinds of Website.
	- ○ You can buy credit card numbers, all manner of drugs, guns, counterfeit money, stolen subscription credentials, hacked Netflix accounts and software that helps you break into other people’s computers. 
	- ○ Buy login credentials to a $50,000 Bank of America account, counterfeit $20 bills, prepaid debit cards, or a “lifetime” Netflix premium account. 
	- ○ You can hire hackers to attack computers for you. You can buy usernames and passwords.
- Also there are emailing service sites and normal facebook too(but more secured). 
- As you see This side of internet is little bit dangerous because a lot of evil hackers are there. 
- For this purpose we have to change our identity, so we use Anonymity. 
- ALSO REMEMBER YOUR ISP WON’T ALLOW YOU TO ACCESS IT.

## Accessing Darkweb

- Using Secured OS is recommended, for better Security and Privacy. 
- We can use these OS for more Anonymity, but still the dark web sites are not easy to find. 
- Also TOR browser is so slow, based on your internet speed, it might not show you the correct result.
![[Pasted image 20250728210405.png]]
Tails OS is a Linux Based OS, that on USB drivers only. It flashes anything after you shutdown the PC, also Connects to Tor network automatically when it is turned on

![[Pasted image 20250728210458.png]]

## Tor Browser

This is How Tor browser looks it is almost same with **firefox** but this have more privacy settings.
```
>	sudo apt install torbrowser-launcher
```

## When you try to access websites.

![[Pasted image 20250728210744.png]]

## Hidden wiki

https://thehidden.wiki
![[Pasted image 20250728210938.png]]
![[Pasted image 20250728211054.png]]

## Blue Teaming

- Blue Teaming refers to the defensive side of cybersecurity. 
- During cyber security testing engagements, blue teams evaluate organizational security environments and defend these environments from Cyber Criminals. 
- Focused on protecting an organization’s assets, systems, and networks from cyberattacks. 
- - **Tasks** 
	- ○ Monitor for threats and vulnerabilities. 
	- ○ Respond to incidents quickly and effectively. 
	- ○ Strengthen the organization's security posture through proactive measures.

## Blue Teaming Job Fields

There are Different Fields in Blue Teaming as there were some on Red Teaming side.
1. Security Operations Center (SOC) 
2. Digital Forensics & Incident Response (DFIR) 
3. Cyber Threat Intelligence ( CTI ) 
4. ProActive Pentest

## Security Operations Center (SOC)

- A centralized team and facility responsible for monitoring, detecting, analyzing, and responding to security incidents in real-time. 
- Purpose of a SOC
	- ○ Provide 24/7 threat monitoring and defense. 
	- ○ Act as the first line of defense against cyberattacks.
	- ○ Ensure continuous security visibility across an organization's IT environment.
- Components of a SOC: PPT
	- ○ People: Skilled Person 
	- ○ Ensure continuous security visibility across an organization's IT environment. 
	- ○ Processes: Well-defined workflows for incident detection, response, and escalation. 
	- ○ Technology: Advanced tools like SIEM, threat intelligence platforms, and endpoint detection and response (EDR).

## SOC Tier Breakdown

### SOC Has 3 Levels/Tiers

### Tier 1: Alert Monitoring and Triage 

- Monitors security tools (e.g., SIEM, EDR,XDR) for alerts. 
- Identifies potential threats and determines their severity. 
- Escalates confirmed or suspicious incidents to Tier 2.

### Softwares

On this Fields, The main Players are the Softwares. 
- Those Software will take the network traffic from different Hosts and analyze and try to inform you based on the severity. They Differentiate that with an IOC and IOA.
	- ○ **IOC**: refers to forensic evidence or artifacts that indicate a system or network has already been compromised. 
		- **Ex**: File Hashes, Suspicious IP Addresses, Domain Names 
	- ○ **IOA**: refers to patterns of behavior or actions that indicate an attack is in progress or about to happen. 
		- **Ex**: Unusual Authentication Attempt,Data Exfiltration Patterns, Suspicious API Calls ○ IOA is More Powerful when we came to Detecting APT activities. 
-  Softwares Used on monitoring are 
	- ○ IDS / IPS, SIEM, EDR, XDR,..
- Not This…� https://cybermap.kaspersky.com/  ![[Pasted image 20250728212241.png]]

### IDS / IPS

- IDS (Intrusion Detection System): A tool that monitors network traffic for suspicious activity and generates alerts but does not block the activity. ○ Example: Snort, Suricata, Zeek 
- IPS (Intrusion Prevention System): An advanced system that detects and actively prevents malicious traffic by blocking it in real-time. ○ Ex: Palo Alto Networks, Cisco Firepower, Trellix (formerly McAfee NSM)
![[Pasted image 20250729002110.png]]

![[Pasted image 20250729002221.png]]

## SIEM / Security Information and Event Management

- A system that collects, analyzes, and correlates logs and security events from multiple sources (e.g., firewalls, servers, endpoints) to detect and respond to threats in real-time. 
- Used as Centralized log management, Detect and alert on suspicious activities. 
- Ex: Splunk, IBM QRadar, Elastic Stack (**ELK**), Microsoft Sentinel

## EDR / Endpoint Detection and Response

- EDR: A security solution focused on detecting, investigating, and responding to threats at the endpoint level (e.g., laptops, servers). 
- Features: 
	- Provides real-time monitoring of endpoints. 
	- Detects malware, ransomware, and suspicious activity. 
	- Enables threat containment (e.g., isolate infected devices). 
- Ex: CrowdStrike Falcon, Carbon Black, Trend Micro's EDR

## XDR

- **XDR**: A comprehensive security solution that extends the scope of detection and response beyond endpoints to include network, email, cloud, and more. 
- Features: 
	- Centralizes threat detection across multiple domains (e.g., endpoints, network, email). 
	- Provides a holistic view of the organization's security posture. 
	- Automates correlation and prioritization of threats for faster response. 
- Ex: Trend Micro Vision One, Palo Alto Cortex XDR, SentinelOne Singularity XDR ●
- These Softwares Will Try to Combine Different Alerts And Try to Form the Cyber Kill Chain.

## WAF /Web Application Firewall

- A security solution that monitors, filters, and blocks malicious HTTP/HTTPS traffic to and from a web application. 
- Protect web applications from common vulnerabilities like SQL injection, cross-site scripting (XSS), and more. 
- Ex: Cloudflare WAF, AWS WAF, Akamia WAF

### Tier 2: Incident Response and Investigation

- Performs detailed analysis of escalated incidents from Tier 1. 
- Confirms whether alerts are false positives or genuine threats. 
- Incident Response responsibilities: 
	- Contain threats (e.g., isolating affected systems). 
	- Mitigate and remediate security incidents. 
	- Coordinate response efforts with other teams (e.g., IT, DevOps). 
- Conducts in-depth investigations (e.g., forensic analysis, log correlation).

## Phases of Incident Response

1. **Preparation**: 
	- Train teams and establish roles. 
	- Set up tools for detection (e.g., SIEM, EDR). 
2. **Detection and Analysis**: 
	- Identify potential incidents via alerts, logs, Captures or Malwares. 
	- Analyze the scope and severity of the incident. 
	- Example tools: Splunk, Wireshark, ELK. 
3. **Containment**: 
	- Isolate affected systems to prevent the spread. 
	- Examples: Blocking malicious IPs, quarantining infected devices
4. Eradication: 
	- Remove the root cause (e.g., malware, compromised accounts). 
	- Patch vulnerabilities and clean systems. 
5. Recovery: 
	- Restore systems to normal operation. 
	- Monitor for signs of reinfection. 
6. Lessons Learned: 
	- Conduct a post-incident review. 
	- Document findings to improve future responses.

## NIST Standard of Incident Response

![[Pasted image 20250729003950.png]]

## Log Analysis

-  A log is a record of events, activities, or messages generated by systems, applications, devices, or users. 
- Logs are used to track system activities and are essential for monitoring, troubleshooting, and security analysis. 
- We Can Analyze Different Logs Based on their Format. 
- Those Softwares we Saw on Monitoring Section Use this Logs Files and Analyze and Generate Alerts. 
- When You work As Incident Responder, After Collecting these Logs You have to Analyze it manually to Understand what really Happened.

## Types of Logs

Based on the content and Format:
##### **System Logs**: 
	- Generated by operating systems. 
	- **Examples**: 
		- Login attempts (successful and failed). 
		- File system changes. 
	- Detect unauthorized access or privilege escalation. 
##### **Application Logs**: 
	- Created by software applications. 
	- **Examples**: 
		- API requests and responses. 
		- Errors in web applications. 
	- Monitor application behavior and detect vulnerabilities.

## Application log
```
>	cat /var/log/apt/history.log
```

## System log
```
>	sudo cat /var/log/boot.log.2
```

##### **Network Logs**: 
	- Captured by networking devices (e.g., firewalls, routers). 
	- **Examples**: 
		- Packet logs. 
		- DNS queries. 
		- Connection requests (e.g., SSH, HTTP). 
	- Detect DDoS attacks, port scans, or exfiltration attempts. 
##### **Security Logs**: 
	- Generated by security tools (e.g., firewalls, IDS/IPS, antivirus). 
- **Examples**: 
	- Intrusion alerts from IDS/IPS. 
	- Firewall rule violations.
 - Monitor threats and investigate incidents.

## Network log
```
>	tshark -r smoke.pcapng -c 50
```

##### Web server logs
- Generated by web servers (e.g., Apache, NGINX). 
- **Examples**: 
	- HTTP requests (e.g., GET and POST). ○ Client IP addresses. 
- Detect XSS, SQL injection, or other web-based attacks. 
- Lets See How we can analyze Logs using a simple Web Server Log. 
- To Perform this 1st you have to Know where the Web server logs are located. 
	- Based on our Web Server Class, it is Located in /var/logs i. 
		- So Based on the Web Server type we will take and analyze the access.log file. 
- We will Perform Manual analysis but sometimes you might get automatic Log analyzing softwares, But they miss small Details.

## Web Log Analysis Using Linux

- When analyzing web server logs (e.g., Apache or NGINX logs), Linux commands like grep, awk and sed are highly useful. 
- Analyzing Logs Differ Based on the Log Type, we will Learn a general Methods That you can Implement on any of logs you got.
![[Pasted image 20250729011352.png]]
- Web Log Formats 
	1. UserID 
	2. Date and Time 
	3. Request Path and Method 
	4. Status Code 
	5. Content Length 
	6. Referer 
	7. User-Agent
- Based On our Prior Linux Knowledge We can Manipulate the logs as we need. 
- **Examples**: 
	-  Find Requests from a Specific IP: `grep "192.168.1.1" /var/log/apache2/access.log` 
	- Count Requests by IP Address: `awk '{print $1}' /var/log/apache2/access.log | sort | uniq -c | sort`
	- Filter Requests by Status Code: `grep "404" /var/log/apache2/access.log`
	- Top 10 Requested URLs: `awk '{print $7}' /var/log/apache2/access.log | sort | uniq -c | sort | head -n 10`
	- Find Requests within a Specific Time Range: `grep "25/Jan/2025:10" /var/log/apache2/access.log`
	- Total Bandwidth Used: `awk '{sum += $10} END {print sum}' /var/log/apache2/access.log`

## Detect Possible Attacks

- SQL Injection Attempts: `grep -i "union" /var/log/apache2/access.log` 
- Directory Traversal:` grep -i "\.\./" /var/log/apache2/access.log` 
- Unusual User Agents: `awk -F'"' '{print $6}' /var/log/apache2/access.log | grep -i -E "curl|wget|python"`

## Automation 

You can use Goaccess too
- https://goaccess.io/
![[Pasted image 20250729013218.png]]

### Tier 3: Cyber Threat Hunting/Intelligence

- Focuses on **proactive threat hunting** to uncover hidden threats. 
- To detect advanced persistent threats (APTs), malware, or insider threats that evade automated security tools. 
- CTI will Hunt Threats and Come Up with IOA/IOCs 
- Develops detection rules and fine-tunes SOC tools (e.g., SIEM rules, playbooks). 
- Researches emerging threats and integrates threat intelligence. 
- **CTI** in Action
	- a. Using threat feeds to block known malicious IPs. 
	- b. Leveraging OSINT tools for reconnaissance.
	- Tracking APT (Advanced Persistent Threat) groups through threat intelligence.

## Categories of CTI Tools

1. Open-Source Intelligence (OSINT) 
2. Threat Feeds & Aggregators 
	- a. AlienVault OTX – Crowdsourced threat intelligence.  
	- b. VirusTotal – Scans files and URLs for malware indicators. 
	- c. AbuseIPDB – Checks for malicious IPs. 
	- d. IBM X-Force Exchange – Advanced threat intelligence sharing.
3. Malware Analysis
	- a. **Any.Run** – Interactive malware sandbox.
	- b. **Hybrid Analysis** – Deep malware behavior reports. 
	- c. **Cuckoo Sandbox** – Open-source automated malware analysis.
	- d. **Intezer Analyze** – Code reuse detection for malware classification.
4. Threat Hunting 
	- Sigma – Open rule-based format for SIEMs. 
	- YARA – Tool for malware identification. 
	- GRR Rapid Response – Incident response tool. 
	- Velociraptor – Advanced endpoint monitoring and threat hunting.
5. Dark Web Monitoring
	- DarkTracer – Tracks leaked credentials and cybercrime activities. 
	- Intel 471 – Monitors cybercriminal networks. 
	- DeHashed – Database breach lookup service. 
	- TorBot – Automated OSINT collection from the dark web.
6. Security Information and Event Management (SIEM)
7. Threat Attribution & TTPs Tracking

## Here is the links of the above tools

- **AbuselPDB**: https://www.abuseipdb.com/
- Hybrid-Analysis: https://www.hybrid-analysis.com/
- Any.Run: https://app.any.run/submissions/
- Threat Sharing Platforms, CTI Community Shares their Findings on Different Feeds.


