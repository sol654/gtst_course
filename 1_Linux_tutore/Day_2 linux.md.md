# Linux Fundamentals for Cybersecurity

## What is Linux?
**Linux** is a kernel - the core program that mediates between software and hardware, managing resource allocation. It serves as the foundation for operating systems.

### Historical Background
- **1969**: Unix was developed for PDP-7 by Ken Thompson and Dennis Ritchie (proprietary, not open source)
- **1991**: Linus Torvalds created the Linux kernel and made it open source (written in C programming language)
- **1983**: Richard Stallman launched the GNU Project and Free Software Foundation, creating free software replacements for Unix utilities (BASH, TAR, EMACS, etc.)

The combination of GNU software and Linux kernel created **GNU/Linux** - a complete operating system.

> **Note**: Operating System = Kernel + Software

## Shell Overview
A **shell** is a command-line interpreter (CLI) that enables user-kernel communication. Common shell types include:

- **SH**: Basic shell (original Unix shell)
- **BASH**: Bourne Again Shell (enhanced with coloring and features)
- **ZSH**: Z Shell (extended BASH functionality)
- **FISH**: Friendly Interactive Shell (colorful, user-friendly)

Check your current shell with: `echo $SHELL`

## Operating System Components
Linux distributions contain:
- Kernel
- Software packages
- File system
- Window manager
- Desktop Environment (GUI interface)

### Popular Desktop Environments
- **GNOME**: Modern, visually appealing (similar to Windows 11)
- **KDE Plasma**: Windows-like interface
- **XFCE**: Lightweight and efficient
- **MATE**: Traditional desktop experience

> **Performance Note**: Choose XFCE or MATE for slower hardware; GNOME or KDE Plasma for high-performance systems.

## Why Linux for Cybersecurity?
- **Efficiency**: Optimized performance for various hardware specifications
- **Market Presence**: 
  - 47% of developers use Linux-based systems
  - 32% of websites run on Linux
  - 85% of smartphones use Linux kernels
  - 96.3% of top web servers use Linux
- **Tool Availability**: Most security tools are Linux-native
- **Security**: Enhanced security model and transparency
- **Flexibility**: Over 600 active distributions available

## Linux Distributions
Distributions vary by:
- Modified Linux kernel
- Package selection (GNU utilities)
- Package management system
- Desktop environment

### Popular Distributions for Security Professionals

#### **Kali Linux** (Debian-based)
- Purpose: Digital forensics and penetration testing
- Maintainer: Offensive Security
- Desktop: XFCE
- Package Manager: APT
- Shell: ZSH

#### **Parrot OS** (Debian-based)
- Purpose: Security, privacy, and development
- Options: Security edition & Home edition
- Desktop: MATE
- Package Manager: APT
- Shell: BASH

#### **Garuda Linux** (Arch-based)
- Desktop: KDE Plasma
- Package Manager: Pacman
- Shell: FISH

#### **BlackArch** (Arch-based)
- Advanced penetration testing distribution
- Not recommended for beginners

> **Windows Note**: Windows doesn't have distributions because its kernel is not open-source.

## Installation Methods

1. **Native Installation**: Sole operating system on hardware
2. **Dual Boot**: Multiple operating systems on same device
3. **Live Boot**: Temporary operation from USB drive
4. **Cloud Terminal**: Remote Linux environment (e.g., webminal.org)
5. **Virtual Machine**:
   - Type 1 (Bare-metal): Direct hardware access (VMware ESXi, Proxmox)
   - Type 2 (Hosted): Runs on host OS (VirtualBox, VMware Workstation)
6. **WSL 2**: Windows Subsystem for Linux (terminal-only environment)

---

