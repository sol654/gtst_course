
Privilege Escalation
```
sudo -l     ..get /usr/bin/vim
sudo vim  
:!bash
```
ssh:
```
ssh solace@128.09.78.8
ssh -p solace@128.09.78.8
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
