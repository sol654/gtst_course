# E. Application/software/ analysis
### Static analysis:
- Analyze the code without excution.
- which program, framework...
### Dynamic analysis:
- Their logic and function.
- Request to server
# Reverse Image Search
- search with images 
- use sites: 
   www.tineye.com
   www.labnol.org/reverse
   www.images.google.com
- **EG**. If you don't know the place in the image's background...
# Google Dorking
- Using google operators optimizing the search results.
- Identifies the vulnerabilities of websites..
- **Powerful** skill for Hackers.
#### 1. Basic Operators
- For **inclusion** ( + ): eg. sol + feyo + jit + jimma   The result must have sol..feyo..jit..jimma..
- For **exclusion** ( - ): eg. Antivirus-software      means "Antivirus" without "software" 
                Eg. Nathan -youtube -geethtech
- Search for **exact term** ( "" ):  eg.  "Solomon Tesfaye"
- **Any word**(wild card): eg.  `Hacker*Hailu`  -It places something between Hacker and Hailu.
- Boolean OR ( | ): eg. "Sol" | "Umex"
#### 2. Advanced Operators
   NB. Dont use space after operators.
- **intitle**: word or phrase found in the title. 
     eg.  intitle:"Hackers of Ethiopia"  eg2.  intitle:geethtech
    -  **NB** intitle:"index of" or intitle:index.of ...tells some datas, passwords, messages
- **inurl**: specific term in URL(link).
    - **EG**. inurl:".geethsecurity.com" 
    - inurl:"/db.sql"
    - inurl:"/admin"
- **site**: any datas in that website. use domain names to search.
    - **EG**. site:geethtech.com
    - Sites with subdomains use (.) eg. site:.google.com
    - Ethiopian sites eg. ` site:*.et`
- **filetype/ext:** resultes with their extensions. 
     - Passwords.. eg.  `password filetype:xls`
     - Hacking book.. eg.  `Hacking filetype:pdf`
     - or use `ext` eg. `"Hacking Book" ext:pdf`
- **intext**: eg. `intext:"Hacking in ethiopia is"`
#### 3. Mixed Operators
Example:
```
intitle:"index of" site:*.et
url:/admin site:*.et
site:*.et "password" filetype:sql
password ext:sql
inurl:ftp 'password' filetype:xls
"mysql dump" filetype:sql intext:password
ftp site:*.et "Password"      ...we can hack with ftp.
site:*.et "api-key"
site:*.et "password" filetype:txt
inurl:ftp "password" ext:xls
intitle:webcamxp inurl:8080     ...cameras
intitle:index of /etc/ssh     ..tells exposed files containing passwords.
```
- Mostly passwords are stored in .sql and .xls
- **File transfer password server(ftp)**  - we can login using ftp. we can control sites with it.
- **api-keys** and **secret keys** also used for hacking purpose.

## Google Hacking Database
- It tells us how to use operators of google dorking to find different vulnerable devices.
- Use the link www.exploit-db.com or search it on google "google hacking database".
### Hackers power
Hackers cat get any thing using operators and others..
eg. password containing files..  intitle:index of /etc/password
# GooFUZZ
- Written with **GO**-script, download it from github, then `cd goofuzz` and check about how to use in **wordlist** .
- It is used for **Google dorking** purpose in terminal.
- -t(target), -w(path, dictionary)..   check them in wordlist of goofuzz.
- **EG**. `./GooFUZZ -t insa.gov.et -e txt`
- **NB**. If you want to run Bash commands in Fish terminal use: `bash -c <any bash commands>`
# Shodan Dorking
  It tells the total results around the world, country level, city level...
  Create a shodan account and then search:
- **title:"geeth"**
- **os:"android"**    ..the operator systems can be windows...
- **port:8080**         ..to search specific port
- **http.html:"Ethiopia is"**    ...in google dorking: *intext*
- **org:"Ethio telecom"**      ...Organization
- **product:Apache**        
- **city:"Addis Ababa"**
- **ssh -port:22**       ..SSH on non standard ports.
- **hostname:"google.com**"      ...in google dorking: *site*   (search with domain)
- **port:80**         ...http(open ports), spefic ports
- **country:ET**    ...for country use short writing systems eg. Germany=DE, Ethiopia=ET
- **Best Example**. **`os:"windows"  org:"Ethio Telecom"  ATM  port:8080`**
- **NB**. The **ATM**s OS is windows. and to connect with ATM use **RDP**...(for hacking)
- **RDP** means Remote Desktop Protocol.
# Github Dorking
- Sensetive informations like: db_credentials, ftp  credentials, and much more. on search bar of github.
- **Eg**. `chapa.co  API_secrete`
- We can use **Regex**.  using:  `/ /`<br>
Eg.
```
chapa.cu /^api/ or ^.*key
telebirr /api.*key/
DB_password ethio
/mongoDB+.password/ ethio
mongoDB+.//      ...running technique of mongoDB password and username
```
- You get number of Repos, commits, and dt languages.
- API, api_key, key, password, secrete, DB_password, admin..<br>
**NB**. To hack **ATM** find **RDP**(Remote Desktop Protocol) 
**NB**. **Shodan** can tells the number of results in country or city level.
- In github there are many sensetive keys. **Eg**. **"Authorization Bearer"**
