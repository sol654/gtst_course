# Steps to pentesting
- Pre-engagement
- Info-gathering
- Scanning
- Gaining access
- Maintain access
- proof of concept(shows the system is able to be hacked)
- post-engagement
# Pre-engagemet step
First step main legal part.
1. **Scoping Questionnaries**: gathered information about the target. time lines, type of testing technique required. **eg**.*Your customer wants a black hat hack.*
2. **Pre-Engagement meeting**: discuss the gathered from the scoping questionnarie and clarify any uncertainity.
###### Here are some Agreements do on this step
- Non-Disclosure Agreement(NDA)
- Rule on Engagement
3. **Kik-OFF meeting**: to officially start the engagement.
# Recon/info-gathering/FootPronting?
**Footprinting = Footprint + Info-gathering**
# Two types of Info-gathering
#### Active and Passive footprinting
1. **Active footprinting**: directly by contacting that person. without permission is illegal.
2. **Passive footprinting**: 3rd party or by checking public sources. **EG**:
- To know the bank working time I can see the posted texts.
- To know the name see username and other profiles.
## Types of Information You gather
a. **Host**: Website, computer... 
b. 
# ONSIT(open source intelligence)
Based on public resources. from websites, search engines, username, domain...
- **ONSIT framework**: we can get a collection of informations b/c it has many tools.
- The site is: www.onsitframework.com
# Shodan
- Lists exposed IOT tools and their informations.
- Search engine for the IOT(internet of things).
**Eg**. search "Android/Webcam/" in www.shodan.io
# Maltego
To link the resources of informations graphically.
**EG**. name and username indicates the photo using arrow graphically.
```
   name ---> photo <---username
```
# A. Website Information Gathering
- About IP, DNS, VHost, subdomain..
### To get IP address
#### 1. **Active recon**
- **ping**  `ping <Website_link>`                 
- **nslookup**  `nslookup <Website_link>`
- **host**:   `host <Website_link>` <br>
**NB**. Don't use WWW/http/https.. just use **domain name** only.
- **EG**:  `host google.com`
#### 2. **Passive recon**
 use site: www.nslookup.io
 or using onsit framework using the "domain name" we can get IPs.
# About dev't Frameworks
- What kinds of programmings, frameworks..
- Use browser Extensions: **Wappalyzer**, **builtwith**. install(add) them and to browser.
**NB**. To install **wappaly**zer on chrome search: wappalyzer chrome. then add extension to chrome. then, search website links on chrome and click the extension icon on wappalyzer. it tells the website framework.
- OR, Linux command: `whatweb geezsecurity.com` 
### To get the web name:
Use the weblink.. or do dt things
### Detail about the domain:
**EG**: command "`whois`", also has a website www.whois.com
```
> sudo apt install whois
> whois
> dig    ...or use this, similar with whois
```
# B. Computer/Phones/
- IP, OS infos, Host name, MAC address, Open services op ports(eg. About sw installed...)
# C. Network
- IP Address 
- Architecture
- Class and Type of Network
- Subnet/vlans
- Host on that NW
- Strength and security on that network
# D. Personal Informations
- Full name
- What the persons love
- friends, status, skills
- To get email, names and locations by phone number use: Truecall
