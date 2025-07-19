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

