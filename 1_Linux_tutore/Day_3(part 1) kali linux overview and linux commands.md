# Essential Kali Linux Tools and Terminal Basics

## Commonly Used Kali Linux Tools

### 1. Information Gathering
- **Maltego**: Intelligence and forensics application for link analysis
- **Nmap**: Network discovery and security auditing tool
- **Recon-ng**: Web reconnaissance framework

### 2. Vulnerability Analysis
- **Nikto**: Web server vulnerability scanner
- **Nmap**: Network exploration and security auditing

### 3. Web Application Analysis
- **Burp Suite**: Web application security testing platform
- **SQLMap**: Automatic SQL injection and database takeover tool
- **WPScan**: WordPress vulnerability scanner
- **OWASP ZAP**: Zed Attack Proxy for web app security testing

### 4. Database Assessment
- **SQLMap**: Automated SQL injection tool
- **jSQL Injection**: Lightweight SQL injection tool
- **SQLite Database Browser**: SQLite database management tool

### 5. Password Attacks
- **Hashcat**: Advanced password recovery tool
- **John the Ripper**: Password cracking utility
- **Wordlists**: Password dictionaries for brute-force attacks

### 6. Wireless Attacks
- **Aircrack-ng**: WiFi network security auditing tool suite
- **Wifite**: Automated wireless attack tool
- **Reaver**: WPS PIN attack tool

### 7. Reverse Engineering
- **APKtool**: Reverse engineering Android applications
- **Ghidra**: NSA-developed reverse engineering framework
- **NASM Shell**: Netwide Assembler shell

### 8. Exploitation Tools
- **Metasploit**: Penetration testing framework
- **Searchsploit**: Exploit database search tool
- **SQLMap**: Database exploitation tool

### 9. Sniffing and Spoofing
- **Wireshark**: Network protocol analyzer
- **Hamster**: Sidejacking tool for session hijacking

### 10. Post Exploitation
- **PowerSploit**: PowerShell post-exploitation framework
- **Backdoor Factory**: Patch PE, ELF, and Mach-O binaries

### 11. Forensics
- **Hashdeep**: Compute and manage hash sets
- **Foremost**: File carving and recovery tool

### 12. Reporting Tools
- **Maltego**: Data visualization and reporting
- **RecordMyDesktop**: Desktop video recording for documentation

### 13. Social Engineering
- **Social Engineering Toolkit**: Penetration testing framework
- **Backdoor Factory**: Binary backdoor creation
- **Maltego**: Information gathering for social engineering

### 14. System Services
- Various service management tools for starting/stopping security services

### 15. Utility Applications
- Basic software tools for general purposes

> **Note**: Research **Hibernate** for advanced persistence techniques in cybersecurity.

## File Managers in Linux Environments

- **Dolphin**: Default file manager for KDE Plasma (Windows-like interface)
- **Thunar**: Lightweight file manager for XFCE and GNOME environments
- **Nautilus**: Default file manager for GNOME (Ubuntu)

> Unlike Windows, Linux file managers are free and open-source.

## Terminal Structure Breakdown

A typical Linux terminal prompt contains:
- **Username**: Current user (e.g., `solace`)
- **Hostname**: Machine name (e.g., `Huntermachine`)
- **Current directory**: Path indicator
- **Privilege level**: 
  - `$` = Regular user privileges
  - `#` = Root (administrator) privileges
- **Command input position**: `_` cursor

**Example prompt:**
```
solace@Huntermachine:~$ _
```

**Directory Indicators:**
- `~` = Home directory
- `.` = Current directory
- `*` = All directories (in certain contexts)

## Basic Linux Commands

### Command Structure
```
command --option argument
```
**Example:** `math --add 1 1`

### Essential Commands

#### `ls` - List Directory Contents
- `ls` : Basic listing (blue = folders, white = text files)
- `ls -l` : Detailed listing with permissions, owner, date
- `ls -a` : Show all files including hidden files
- `ls folder_name` : List contents of specific folder
- `ls -R` : Recursive listing of all subdirectories
- `ls -Rla` : Combined options (recursive, long format, all files)

> **Note**: Files starting with `.` are hidden files

#### `cd` - Change Directory
- `cd /` : Root directory
- `cd` or `cd ~` : Home directory
- `cd ..` : Move up one directory level
- `cd ../..` : Move up two directory levels
- `cd folder_name` : Enter specific folder
- `cd 'folder name'` : Access folders with spaces in name (use quotes)

---

