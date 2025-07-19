# Web Penetration Testing


## What is Web Application?

● A web application is a program or software that runs on a web Browser to perform specific tasks. 
- ● WebSites Consists 2 parts.
	- **Front End** / Client side /
		- HTML,CSS,JS(react,angular)
	- **Back End** / Server Side /
		- Example: JS(node.js),Python(Django,Flask),PHP,SQL


### HTML /HyperText Markup language/

**Markup language** refers to a text-encoding system consisting of symbols inserted in a text document to control its structure, formatting, or the relationship between its parts.
- **HTML** is the standard markup language for creating Web pages.
- HTML have elements called Tags.
	- Example: `<a>, <html>...`

- When we search google.com:
	1. DNS resolution
	2. TCP connection
	3. HTTP request and response

# What is web hacking

**Web hacking** refers to exploitation of applications via HTTP which can be done by manipulating the application via its graphical web interface.
- It is The another Big Scope of Cyber Security, Used as *initial access* to Systems.
- **Hacking Process** is almost same on all type of fields.
	- ○ Information gathering 
	- ○ Scanning 
	- ○ Exploiting / Gaining Access 
	- ○ Post-Exploitation / Maintaining Access 
	- ○ Cover-Tracking
- To hack anything you have to know how the thing works.


## How do websites work?

### Web servers

On the hardware side, **a web server is a computer that stores web server software and a website's component files** (for example, HTML documents, images, CSS stylesheets, and JavaScript files).
- A web server connects to the Internet and supports physical data interchange with other devices connected to the web.
- **Web Server Software** is a computer software that **uses HTTP and HTTPS to provide a website**.(by default **port 80,443**)
- There are a lot of softwares that can be installed on the server to Create the web services.
- As we talked previously, servers are just computers. So to be specific and talk about web server, we have to install some web things.


## A. Apache server

● This Server software will help to provide Web contents. 
- ● On linux it comes Built in 
- ● But on windows you can install it with softwares called Xampp and Wampp and will give you localhost web contents 
- ● To Start this server software:
```
sudo systemctl start apache2
```
From now on our computer is acting like a **webserver**.
- **Configuration file**: `/etc/apache2/apache2.conf`
- **Log File**: `/var/log/apache2/access.log`
- **Port Config File**: `/etc/apache2/ports.conf`

## Web Server - apache

By going to out IP on any browser we can get a websites.
- The **default path of apache2** is: `/var/www/html`
```
>	cd /var/www/html
>	ls
	index.html  index.nginx-debian.html
```
So on any web server the websites are running on This path.
- The website you see on the browser when you run your IP is the default web for apache2 the file for this is the “ index.html” from the /var/www/html file.


## B. Nginx Server

- **NGINX** (pronounced "engine-x", NG(next-generation) is a high-performance web server, reverse proxy server, and load balancer.
- It's widely used for serving static content, acting as a reverse proxy for dynamic content, and improving the scalability and performance of websites and web applications.
- To start the server:
```
>	sudo systemctl start nginx
```
- To Check Status:
```
>	sudo systemctl ststus ngnix
	enable/disable....and...active/
```
- **Config file**:` /etc/nginx/nginx.conf`
- **Log File**: `/var/log/nginx/access.log`


## C. Python Server

We can use python to start web servers
- To start the service 
	- ○ `python3 -m http.server <port_Number>`
```
	python3 -m http.server 9090
```
- The python will help you to host website from any path on your computer with any port you need.
- **Example**: I started the web server in ~/rex folder with port 9090 
	- ○ So to access the website I need to type the port with the ip 
		- ■ 192.168.1.7:9090 => will be the site for this



## URL and URI

- ● URI identifies: a resource and differentiates it from others by using a name, location, or both. 
- ● URL identifies: the web address or location of a unique resource. 
- ● URI contains components like a scheme, authority, path, and query. 
- ● URL has similar components to a URI, but its authority consists of a domain name and port. 
- ● URL is part of URI 
- ● A URI aims 
- ● A URL aims to identify a resource and differentiate it from other resources by using the name of the resource or location of the resource. to find the location or address of a resource on the web. 
	- ○ An example of a URI can be, https://www.geezsecurity.com , www.geezsecurity.com ,"mailto:info@example.com" (a URI that specifies an email address) "tel:+1-212-555-1212" (a URI that specifies a phone number) 
	- ○ An example of an URL is https://www.javatpoint.com.

## Parts of URL

A URL consists of five parts:
1. **Scheme**: tells servers which protocol to use when it accesses a page on your website.
2. **Subdomain**:
	- a.  A subdomain in a URL indicates which particular page of your website the web browser should serve up.
		- i. For instance, subdomains like "blog" or "offers" will provide your website’s blog page or offers page.
3. **Top-level domain**: specifies what type of entity your organization registers as on the internet. 
	 - a. Generic Top level domain(gTLD): .gov .org .net 
	 - b. Country code Top-level domain(ccTLD): .et .ru
4. **Second-level domain**: is the name of your website.
5. **Subdirectory**: also known as a subfolder,helps people understand which particular section of a webpage they’re on.

#### Using Routes

Using Files Using Routes www.geezsecurity.com/tech/secret/secret.txt
- geezsecurity.com/activate -> activate.js File will be rendered-> /var/www/html/tech/secret/secret.txt The above is Webs With No Route Configured , but there are some applications who use **Routes**


## DNS

**The Domain Name System ( DNS)**: is the **Phonebook of the Internet**.<br>
- When users type domain names such as ‘`google.com`’ or ‘`nytimes.com`’ into web browsers, DNS is responsible for finding the correct IP address for those sites.
- Browsers then use those addresses to communicate with origin servers or CDN edge servers to access website information.
- This all happens thanks to DNS servers: machines dedicated to answering DNS queries.
- DNS server works on **port 53**.
- The DNS request the goes out from our computer is called “DNS query”.
- There are four servers that work together to deliver an IP address to the client: recursive resolvers, root nameservers, TLD nameservers, and authoritative nameservers.


## DNS Records

● **DNS records (aka zone files)** are instructions that live in authoritative DNS servers and provide information about a domain including what IP address is associated with that domain and how to handle requests for that domain.
- These records consist of a series of text files written in what is known as **DNS syntax**.
- Works on port 53 UDP/TCP
- To Access DNS Record on linux we can use tools like 
	- ○ Nslookup 
	- ○ Dig 
	- ○ Host

## Dig

```
dig google.com
```

## Nslookup

```
	nslookup google.com
```

## host

```
	host google.com
```



# Types of DNS records

### There are Many DNS record Types but lets see some

## A Record ( Address )

● This is a Record on the server that holds **IPv4 Address**
```
>	nslookup --query=A google.com

>	host A google.com
```

## AAAA Record (Quad Address)

- This holds the **IPv6** Of the Domain.
```
>	nslookup --query=AAAA google.com

>	host AAAA google.com
```

## MX Record ( Mail Exchange )

● Directs mail to an email server.
```
>	dig MX google.com

>	host -t MX google.com
```

## NS Record ( Name Server )

● Returns the DNS servers (nameservers) of the domain. Server Where all the DNS records are stored!
```
>	host -t MX insa.gov.et

>	dig NS google.com
```

## SOA(start of authority) Record

https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/
● Stores important information about a domain or zone such as the email address of the administrator, when the domain was last updated, and how long the server should wait between refreshes. 
- ● All DNS zones need an SOA record in order to conform to IETF standards. 
- ● The 'RNAME' value here represents the administrator's email address, which can be confusing because it is missing the ‘@’ sign, but in an SOA record **admin.example.com** is the equivalent of admin@example.com.
```
>	dig SOA google.com
```

## CNAME(canonical name) Record

Record that maps one domain name (an alias) to another domain name (the canonical name).
- Instead of pointing directly to an IP address, it points to another domain that has an A record.
- CNAME record: **writeup.geezsecurity.com → geez.blog.com**
- CNAME records are helpful for managing redirects, subdomains, and ensuring that multiple domain names point to the same website or service.
	- not all subdomains are required to have CNAME records.
```
>	dig CNAME blog.geezsecurity.com
```

## ANY Query

Query type that requests all available DNS records for a particular domain. It essentially asks the DNS server to return all record types associated with the queried domain.
```
>	dig any zonetransfer.me
```


## Package On WireShark

How DNS is Resolved
- Go to '**package detail pane**' -> '**DNS**' -> '**Answers**' -> then you can look the DNS ANY query.

## DNS on local Network

```
>	nmcli dev show | grep 'DNS'
>	nmcli dev show | grep -i 'ip4.gateway'
```
On our local network our, DNS Server is our Router.
```
>	nmap 192.168.241.102 -vvv
```

There are more Records like 
- ○ TXT 
- ○ SRV 
- ○ PTR 
- ○ ...<br>
**NB**. If you wanna Have Advanced knowledge on this Try to learn about "**Zone Transfer**".


# How do websites work.

When you access a website or click a link, it will send a **HTTP request** to the server and get the copy of the website files to the client this is called **HTTP Response**.

## HTTP request and response

The requests and Response are sent and received with a Header.

## HTTP Headers

- The **HTTP headers** are used to pass information between the clients and the server through the request and response header.
- All the headers are case-insensitive, headers fields are separated by colon, **key-value pairs in clear-text string** format.
- The end of the header section denoted by an empty field header(New line).

## Types of Headers

- **General Header**: This type of headers applied on Request and Response headers both but without affecting the database body.
	- A. `Cache-Control: no-cache`
- **Request Header**: This type of headers contains information about the fetched request by the client.
	- A. `Host: example.com`
	- B. `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)`
- **Response Header**: This type of headers contains the location of the source that has been requested by the client.
	- A. `Server: Apache/2.4.1 (Unix)`
	- B. `Location: https://example.com/new-page`
- **Entity Header**: This type of headers contains the information about the body of the resources.
	- A. `Content-Type: text/html; charset=UTF-8`
	- B. `Content-Length: 348`

## Request Headers

This is A header sent to the server. 
- In Request Header There are different kind of headers 
	- ○ Example: GET, Host, Cookie,...
- The 1st line Contains 
	- ○ Request Method 
	- ○ Path: The path where the file/folder is located 
	- ○ Protocol Type: which HTTP protocol ( HTTP 1 , HTTP/1.1) 
-  The 2nd line 
	- ○ Host: the website link
- The 3rd line 
	- ○ Cookie: used to Verify a user
-  The 4th line:
	- ○ User-Agent: used to place the browser information
- 5-7th line:
	- ○ Accept: text/html: The client is requesting HTML content. 
	- ○ Accept-Language: The client is accepting english
- 8th line:
	- ○ Connection: close: Indicates that the client or server wants to close the connection after the current request/response.

## Response Header

This is response from The server to the browser
- 1st line
	- ○ HTTP: Tells the server Protocol 
	- ○ Status Code
- 2nd line 
	- ○ Date: Date of the response sent
- 3rd line 
	- ○ Content-Type: What type of content the server sent Encode type  
- 4th line 
	- ○ Content-length: The number of the alphanumeric and spaces  
- 5th line 
	- ○ Server: type of the web server  
- 6th line 
	- ○ This line is empty used to show that the headers ending, And tells the beginning of the body
- 7th…. Line 
	- ○ The html content

## HTTP request methods

-  The method designates the type of request being made to the web server. 
- The most common types of request methods are GET and POST but there are many others, including HEAD, PUT, DELETE, CONNECT, and OPTIONS. 
- GET and POST are widely supported while support for other methods is sometimes limited but expanding.

## HTTP Parameters

In HTTP requests, parameters can be included in several ways:
- ○ query parameters, 
- ○ path parameters, and 
- ○ body parameters.
<br>Each type serves different purposes and is used in different contexts.

## Query Parameter

**Query parameters** are appended to the end of the URL and are used to pass additional data to the server.
- They are typically used to filter, sort, or modify the data returned by a request.
- These are Used on **GET** Request.
	- ○ To put parameters we will use “ ? “ after that path, and “&" is a separator.
- `EG. https://example.com/login?uname=solace&psword=sol@ce123`
- The Words “*uname*” and “*psword*” Are called: **Parameters**.

## Path Parameters

**Path parameters** are part of the URL path and are used to specify a specific resource or endpoint within a resource.
- They are used in RESTful APIs to specify which resource to operate on.
- Eg. `https://example.com/user/solace`

## Body Parameters

Body parameters are sent in the body of the HTTP request and are typically used to submit data to the server in POST, PUT, or PATCH requests.
```
	The URL:       https://eg.com/login

	The HTTP Req:  POST /login HTTP/1.1
				   HOST: eg.com
				   ..
				   ..
				   username=solace&password=sol@ce123
```

## HTTP Status Code

- The Status-Code element in a server response
- is a 3-digit integer where the first digit of the Status-Code defines the class of response and the last two digits do not have any categorization role.
- There are 5 values for the first digit: 
	- ○ 1xx: Informational 
		- ■ It means the request has been received and the process is continuing.
	- ○ 2xx: Success 
		- ■ It means the action was successfully received, understood, and accepted.
	- ○ 3xx: Redirection  
		- ■ It means further action must be taken in order to complete the request. 
	- ○ 4xx: Client Error 
		- ■ It means the request contains incorrect syntax or cannot be fulfilled. 
	- ○ 5xx: Server Error 
		- ■ It means the server failed to fulfill an apparently valid request

## Some common codes

- ● **200** = request is Successful( **OK** ) 
- ● **301** = The requested page has moved to a new url . ( **Moved Permanently** ) 
- ● **302** = The requested page has moved temporarily to a new url .( **Found** ) => when there is **redirection** 
- ● **400** = The server did not understand the request. ( Bad Request) 
- ● **401** = The requested page needs a username and a password. ( **Unauthorized**) 
- ● **403** = Access is forbidden to the requested page.( Forbidden) 
- ● **404** = The server can not find the requested page.( Not Found) 
- ● **405** = The method specified in the request is not allowed.( Method Not Allowed) 
- ● **500** = The request was not completed. The server met an unexpected condition.( **Internal Server Error**)<br>
There are some exceptions like some websites return 200 but when u see the content it says 404

## Statelessness of HTTP

HTTP is a stateless protocol, meaning each request from a client to a server is independent and does not retain any state information between requests.
- Implications:
	- **No Memory**: The server does not remember past requests.
	- **Each Request is Isolated**: Each request must contain all necessary information.
- Therefore, to help the system to recognize us we can use, **Cookies** or **Tokens**
- **Cookies**: Small pieces of data stored by a web browser on the user's device.
	- Used to maintain stateful information over multiple HTTP requests. 
		- ■ User Data 
		- ■ User Preferences 
			- ● Dark and Light Modes 
			- ● Site Customizations
	- While HTTP itself is stateless, cookies allow servers to maintain stateful sessions.
1. Servers Set Cookies For Users using,
	- “Set-Cookie: user120;” Response header
2. Users Will send Every Request by Including this Cookie with
	- “Cookie: user120; mode=dark” on their Request Header

## Where do you see the headers?

The headers are shown on some methods. 
1. Developers tool(on browser) 
2. Curl 
3. Web Proxy Softwares(burpsuite,caido,..)

## Developers tool

To open it on browser 
- ○ Press Ctrl+shift+ i
- This tools contains lot of things 
	1. **Inspector**: to see and edit the HTML and CSS 
	2. **Console**: to run some Javascript codes 
	3. **Debugger**: used to do debug in runtime 
	4. **Network**: to see the requests and responses 
	5. **Storage**: to store cache and cookies 6. … 
- To get the requests we go to the Network tab

## Curl on linux

- developers use to transfer data to and from a server.
- cURL supports several different protocols, including HTTP and HTTPS, and runs on almost every platform.
- Syntax:
```
		curl [options] [URL]
```

- To get the web content/html/ of the site:
```
	curl https://www.google.com
```

- To change the request method:
```
		curl -x GET https://www.google.com
```

- To see the response headers
```
		curl -I https://www.google.com
```

# Web Proxies

A tool that intercepts and analyzes HTTP/HTTPS traffic between a client (browser) and the web server.
- Used to facilitate security testing by allowing manipulation and examination of requests and responses.
- **Example**: 
	-  Burp Suite 
	-  OWASP ZAP 
	-  ….

## Burp suite

Burp or Burp Suite is a set of tools used for penetration testing of web applications.
- It is developed by the company named Portswigger, which is also the alias of its founder Dafydd Stuttard.
- it supports the entire testing process, from initial mapping and analysis of an application's attack surface, through to finding and exploiting security vulnerabilities.
- Burp Proxies with 127.0.0.1:8080 by default

### Installing

You can Install the Pro Version(cracked) with the following Steps, but u can use the free too
- Burp Suite have 3 versions 
	- ○ Community = free 
	- ○ Enterprise - paid 
	- ○ Professional - paid

- We will install the professional burp.
	- ○ After Downloading it
	- ○ Extract it and go to the path: `unzip burpsuit_pro_v2022.7.zip`
	- ○ On the 1st terminal run:
		- ■` ja va -javaagent:BurpSuiteLoader_v2022.7.jar -noverify -jar burpsuite_pro_v2022.7.jar`
	- ○ On another terminal run:
		- `■ ja va -jar Loader.jar`
	- ● There will be 2 Windows as you see.
	- Then Copy the License code 
		- ○ Use Ctrl-C
	- Paste it to the Burp “Enter License Key” 
		- ○ Use Ctrl-V
	- Click Manual Activation
	- Copy request
	- Paste it on The Loader “ Activation Request”
	- Then Copy The “ Activation Response”
	- Click paste response on Burpsuite.
	- Finally�, Activated Burp PRO!

## Opening Burp

Helps you: 
	- ○ To open project 
	- ○ Create new project 
	- ○ Use Temporary Project 
	- ● Then just click “Start Burp”

## Starting Burp

This is the Home page of Burp.
- There are many tabs as you see on the above.
	- ○ Target: to add targets inscope & see progress 
	- ○ Proxy: to setup proxy IP’s also to intercept and watch requests and responses 
	- ○ Intruder: to Do brute force attacks 
	- ○ Repeater: To do manual checks 
	- ○ Comparer: to compare 2 requests/responses
- When you Try to open burp next time goto the folder and execute this command
- java
	- -javaagent:<ADD_THE_PATH>/BurpSuiteLoader_v2022.7.jar -noverify -jar
	- <ADD_THE_PATH>/burpsuite_pro_v2022.7.jar

## Scoping

We can Limit A domain/IP we won’t to proxy through our burp.
- Target -> Scope -> Add
- Now Burp will only intercept or see Requests and responses from `<added domain/IP>`

## Setting Up Web Proxy

We need to connect our browser with Burp, To Perform Proxy
- To Do this we can set up our proxy setting on our browser or install a proxy plugin = Foxyproxy.
- Now Add The Burp Proxy Address
- ● Add
	- ○ Title: anything u need “Burp”..
	- ○ Proxy IP: 127.0.0.1 
	- ○ Port: 8080 
	- ○ Save
- To Intercept you just click the foxy icon and click burp

## HTTPs Proxying with Burp

For HTTPS sites, You need to Setup Certificate

1. Goto burp/ on browser
	- a. Download the CA Certificate
2. Goto Setting
	- a. Search for Certificates
	- b. View Certificates.
	- c. Import
	- d. Add the cacert
	- e. Tick the 2 boxes
	- f. OK
- DONE

## Demo

1. Turn the Foxy proxy on. 
2. Try to Access Some site 
3. Goto burp Proxy 
		a. HTTP history 
4. Check it, the headers and HTTP requests

## DEMO TIME

You need to learn Burp Suite In Detail.
- https://youtu.be/25QEaNmfRNs?si=vZ1KwjgMp4L-lQZ2

# ATTACKING WEBSITES

## Web Enumeration

Web Enumeration is Gathering Informations about a websites and APIs.
- ● Things We gather: 
	- ○ Development Framework 
	- ○ Directories 
	- ○ Sensitive Files 
	- ○ VHOSTS 
	- ○ Subdomains
- On web Enumeration there is a term called “ **Fuzzing**”
- Fuzzing Reference to Sending random requests to a server and determining a bug based on what the server responds.
	- But we Sometimes Use it when we try to mention an attack called “BruteForce”(they are almost same)

## Directory BruteForce

Directory bruteforce is a technique used in web penetration testing to discover hidden **directories**, files, ,resources on a web server and **ROUTES**.
- How it Works:
	- ○ **Automated Tools**: Tools send a series of HTTP requests, guessing directory and file names based on predefined wordlists
	- ○ **Example**: Trying common names like /admin, /backup, /config, etc.
- Tools To do This
	- ○ Dirb 
	- ○ Dirbuster 
	- ○ goBuster 
	- ○ FFUF
- Analyze Responses: Check **HTTP status codes** 
- for clues: 
	- ● 200 OK: Directory/file exists. 
	- ● 403 Forbidden: Directory exists but is restricted. 
	- ● 404 Not Found: Directory/file does not exist

## Scenario

Let’s See How Critical this Technique is. 
- ● Fuzzed For Directories , and Got /adminfiles/
```
>	dirsearch -u https://[reacted].com/
```
- ● Continued Fuzzing For another Files/Folders Under adminfiles
```
>	dirsearch -u https://[reacted].com/adminfiles/
	
  ......access to all subdirectories is forbidden, no file found via recursive scan. 
```
- lets scan with some extensions. Got an Interesting File called “stats.db” which is database file.
```
>	dirsearch -e xml, json, sql, log, yml, yaml -u https://[reacted].com/adminfiles/
```
BOOM!
- We Downloaded the database and We got uses password Hash.
```
>	wget https://[reacted].com/adminfiles/stats.db

>	sqlite3 stats.db
```

## Subdomain Enumeration

● **Subdomain Enumeration** is the process of identifying subdomains associated with a main domain.
- e.g., blog.example.com where blog is a subdomain of example.com.
- Developers Think Thus Subdomains Won't be Found So, they might do something Vulnerable on the subdomains rather than the main Domain.
- But Hackers use different Methods To Get Subdomains.
- Tools:
	- ○ subfinder 
	- ○ assetfinder 
	- ○ Findomain 
	- ○ subdomainfinder.c99.nl   (website)

## FFUF - Fuzz Faster U Fool

A fast web fuzzing tool designed for penetration testers.
- Useful for finding hidden files, directories, subdomains, and other vulnerabilities
- Written in Go and optimized for speed.
- Syntax:
	- **ffuf -w wordlists -u url -H headers**
	- ○ Subdomains: `ffuf -w wordlist.txt -u https://FUZZ.rexder.com` 
	- ○ Dir Brute: `ffuf -w wordlists.txt -u https://rexder.com/FUZZ` 
	- ○ Vhost: `ffuf -w wordlists.txt -u https://rexder.com/ -H ‘Host: FUZZ.rexder.com’` 
	- ○ With request file: `ffuf -w wordlists -request request.txt`


# COMMON WEB ATTACKS

- ● Injection Attacks 
	- ○ SQLi 
	- ○ XSS 
	- ○ SSRF 
	- ○ SSTI
- ● Broken Access Control 
- ● Business Logic 
- ● File Upload 
- ● Race Condition 
- ● CSRF 
- ● API Testing

## A. Injection Attacks

**Injection attack** occurs when an attacker sends malicious input into a program, exploiting improper input validation or filtering, to alter its execution.
- This Is Performed through the Parameters.

#### Common Types:

- ● **SQL Injection (SQLi)**: Targets databases. 
- ● **XSS (Cross-Site Scripting)**: Targets web browsers. 
- ● **Command Injection**: Targets operating system commands. 
- ● **LDAP Injection**: Manipulates LDAP queries. 
- ● **SSRF** 
- ● **Open Redirect** 
- ● **Host Header** 
- ● **SSTI**

## SQL injection

It is included in Injection Bug.
- ● Here we will add a SQL Query to the search place. 
- ● SQL is a query language used in Backend to retrieve data from database. 
- ● Most of the time used to bypass login pages, Dump Database of The Website.

- eg. `eg@gmail.com and for password use ' or 1=1--`
	- ➔ This is Just Demo, But this is how the Hack happens, 
	- ➔ On the payload Attackers can Craft a SQL query that can cause RCE, Full Database Detail listing and much moreeeee.

## Further

Learn about Tool called SQLMap.
```
>	python sqlmap.py -u "htps://debiandev/sqlmap/mysql/get_init.php?id=1" --batch
```

## Cross-Site Scripting / XSS

It is included in Injection Bug
- ● This Bug is exploited. As the following 
	- ○ If there is a search place and the search place expects a text to search and displays below. 
	- ○ But if we add some html/JS codes on that place, this means it will add the code to the innerHTML 
	- ○ SO our code will be executed!
- allows attackers to inject malicious scripts into web pages viewed by other users.

## Command Injection

**Command Injection** is a type of attack where an attacker executes arbitrary commands on a server or system by manipulating vulnerable applications.
- Exploit an application that allows user input to interact with the operating system (OS) commands.

## SSRF

A vulnerability where an **attacker tricks the server** into making unintended requests to internal or external systems.
- Exploits server-side functionality that fetches URLs or data from other systems.
- Ex: https://geezsecurity.com/fetch?url=http://127.0.0.1:8080/admin

## Path Traversal

A vulnerability that allows attackers to access files and directories outside the intended scope of the web application.
- Exploits improper sanitization of file path inputs.
- eg: The path is www.fodie.com/menus?menu=achnoburger.pdf
- The attacker changed and runs again and got 'shadow ' file.
```
>	 www.fodie.com/menus?menu=../../../../etc/shadow
```

## CSRF

A vulnerability where an **attacker tricks a user** into performing unintended actions on a web application where they are authenticated.
- Exploits the trust a server has in the user's browser.
- Ex: https:/geezbank.com/transfer?from=natan&to=elias&amount=1000

## REMEMBER

All the Injection Attacks are done on some Parameter.

## B. Authorization And Authentication

- What is Authentication? 
	- ○ Definition: Verifying who the user is. 
	- ○ Goal: Confirm the user's identity using credentials like: Passwords
- What is Authorization?
	- ○ Definition: Verifying what the user is allowed to do. 
	- ○ Goal: Control access to specific resources or actions based on permissions.

## Access Control

This is a problem occurred on how a websites control an access of a user. ● If there is a problem on the access control.
- If there is a problem on the access control.
- Then think that normal user can get access of admins or root user.
- This is Good Bug to find because you don’t have that much automation tools.

## Insecure direct object references / IDOR

- ● IDOR is a bug included in Access Control. 
- ● This is a bug that happens when you have an id number 1 
- ● And is abebe is id 1 then if i changed that number to 0 and got another users 

## Brute-Force and Dictionary Attack

- ● It is included in Broken Authentication Bug 
- ● This is a kind of attack that is usually done to a login pages. 
- ● It uses Wordlist and try to check a lot of words in the place of the username and password. 
- ● It is a guessing game but the guess is done with computer.

## C. Business Logic

- ● This Bug is a logic Flow. 
- ● It occurs by the way how the programmer thinks and hackers thinking. 
- ● Think like if You have bank website and it have a purpose of send money. 
- ● Then if i can change add to negative numbers 
- ● And if the site responded by giving me more money and minimizing the amount of the user i planned to send then this is business logic 
- ● Also this is a Good Bug to learn.

## D. Rate limit

-  This is a limiting problem.
- Think like if the developers did made a limit to some task.
- Example: 
	- ○ If there is website , that send an OTP/verification code 
	- ○ And if it doesn't limit to some code sends only. 
	- ○ I can make the site to send 100000 OTPs to ma phone this means 
	- ○ We will make the site to lose a lot of money

## E. File Upload

- ● A security issue where attackers upload malicious files to a web application, exploiting insufficient validation or restrictions. 
- ● Common in applications allowing user-generated content (e.g., images, documents). 
- ● One of Good ways to Get Remote Code Execution( RCE ).

## API(Application Programming Interface)

**API** A set of rules and protocols that allows different software applications to communicate with each other.
- APIs define how requests are made, what data formats are used, and how responses are returned.
- The Purposes are: 
	- ○ Enable applications to interact seamlessly. 
	- ○ Facilitate integration between systems
- Examples: REST , SOAP, Graphql APIs
- We need to Learn API security 
	- ○ APIs expose sensitive data and critical functionality. 
	- ○ They are a major attack surface for attackers, especially in modern applications (mobile apps, IoT, web).

## API Security

##### API Security Testing Process

##### Step 1: Reconnaissance

- Collect API information:
	- ○ API documentation (Swagger, Postman collections). 
	- ○ Endpoints, methods (GET, POST, PUT, DELETE), and parameters. 
	- ○ Authentication mechanisms (JWT, OAuth, API keys). 
-  ● Tools: Postman, Burp Suite, Swagger Inspector.

##### Step 2: Vulnerability Identification

- ● Authentication Testing: 
	- ○ Test for weak/missing authentication mechanisms. 
	- ○ Use invalid tokens, replay tokens, or bypass authentication. 
- ● Authorization Testing: 
	- ○ Exploit 
	- ○ Check access control (e.g., can a normal user access admin endpoints?). BOLA by testing GET /users/1 vs. GET /users/2. 
- ● Input Validation Testing: 
	- ○ Test for SQL injection, command injection, or XSS vulnerabilities. 
	- ○ Tools: SQLmap, Burp Suite. 
- ● Rate Limiting Testing: 
	- ○ Check if the API enforces request throttling. 
	- ○ Tools: Burpsuite, ffuf, or custom scripts

# Web Hacking Methodologies

These are Steps to Hack websites, After Gathering informations about the system Hacking the Application is just Trying to Use the Application and trying things in an intended way.
- There are Different Hacking Methodologies Which Peoples Use. Learning those as Beginner will help you on your Testing
	- ○ Ex: Zseano Methodology, Jhaddix Methodology.

## Learning Roadmap

- You can Follow this Road map, To be Good Web Penetration tester In The following 3 month:
1. Learn Web Development( Learn Basics Not advanced Development)
	- frontend(HTML,CSS,JS) - 1 month
	- backend(Django or php) - 1 week
		- use Youtube resources they will teach you the basics and Quickly(in 5 hrs)
2. Learn Web Attacks
	- You can use https://portswigger.net/web-security/all-topics - 1 month
		- i. Geez Tech Web Playlist
3. Learn Web Enumeration techniques - 3 Days 
	- a. Tools like(VIM,FFUF,SQLMAP,...)
4. Read Testing Methodologies(zseano,jhadix) - 1 weak
5. Do Web challenges ( CTFs ) - 2 weaks
	- HERE YOU ARE A GOOD SKILLED PENTESTER!
6. Try to test Ethiopian Websites(chapa.co)
7. Try to test Foreign Websites(We will learn on Bug Bounty Class)

## Follow this Web Attack Plans

- ➔ 5 Days ◆ SQL injection ( 18 Labs ) 
- ➔ 4 Days ◆ Path Traversal ◆ Command Injection 
- ➔ 4 Days ◆ Business Logic ◆ Info Disclosure
- ➔ 3 Days ◆ Access Control 
- ➔ 4 Days ◆ File Upload ◆ Race Condit
- ➔ 2 Days ◆ NoSQL injection ◆ API testing 
- ➔ 3 Days ◆ XSS ( 15 Labs ) 
- ➔ 2 Days ◆ CSRF ◆ Clickjacking 
- ➔ 3 Days ◆ SSTI ◆ JWT attacks
<br> ● With this You can learn the attacks within 30 Days, You just need to be Committed  and Disciplined.

