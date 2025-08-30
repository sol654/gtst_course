# Linux File System Hierarchy

## Introduction
Linux uses a standardized file system hierarchy that organizes files and directories in a specific structure. Understanding this hierarchy is essential for system administration and cybersecurity work.

## Key Directories

### `/` - Root Directory
- The top-level directory in the Linux file system
- **Note**: `/` (root directory) is different from `/root` (root user's home directory)

### `/bin` - Essential User Binaries
- Contains essential command binaries for all users
- Examples: `cat`, `ls`, `cp`, `mv`, `rm`
- Accessible by both normal and root users

### `/boot` - Boot Loader Files
- Contains files needed for system boot process
- Includes kernel images, bootloader configurations

### `/dev` - Device Files
- Contains device files representing hardware components
- Examples: `/dev/tty1` (terminal), `/dev/usbmon0` (USB device)

### `/etc` - Configuration Files
- Stores system-wide configuration files
- Contains start/stop shell scripts for services
- Important files:
  - `/etc/hosts` - Local domain name resolution
  - `/etc/passwd` - User account information
  - `/etc/resolv.conf` - DNS resolver configuration

### `/home` - User Home Directories
- Contains personal directories for each user
- Users cannot access other users' home directories without permission
- Example: `/home/solace` for user "solace"

### `/lib` - Essential Libraries
- Contains shared libraries needed by binaries in `/bin` and `/sbin`
- Library naming convention: `ld*` or `lib*.so*`

### `/media` - Removable Media Mount Points
- Temporary mount directory for removable media
- Example: `/media/cdrom` for CD-ROM drives

### `/mnt` - Temporary Mounts
- Used for temporarily mounting filesystems

### `/opt` - Optional Software Packages
- Contains third-party application software
- Example: Google Chrome, proprietary software

### `/sbin` - System Administration Binaries
- Contains essential system binaries for root user
- Normal users require `sudo` to access these commands

### `/tmp` - Temporary Files
- Stores temporary files that are deleted on system reboot

### `/usr` - User Utilities
- Contains user-accessible programs and utilities
- Subdirectories: `/usr/bin`, `/usr/sbin`, `/usr/lib`

---

# Linux Text Editors

## Types of Text Editors

### Command-Line Text Editors
- **Vim** - Vi Improved (powerful, modal editor)
- **Nano** - Simple, beginner-friendly editor
- **Emacs** - Extensible, customizable editor
- **Neovim** - Modern Vim fork

### Graphical Text Editors
- **VS Code** - Microsoft's cross-platform editor
- **Sublime Text** - Proprietary code editor
- **Gedit** - GNOME desktop environment editor
- **Plume** - Lightweight graphical editor

---

# Vim Editor Guide

## About Vim
- **Vim** (Vi Improved) is an enhanced version of the original Vi editor
- Powerful but has a steep learning curve for Windows users
- Operates in multiple modes for different functions

## Vim Modes

### 1. Normal Mode (Default)
- Default mode when opening Vim
- Used for navigation, copying, pasting, and deleting
- Cannot insert text in this mode

### 2. Insert Mode
- Enter by pressing `i`
- Allows text insertion and editing
- Press `Enter` for new lines
- Return to Normal mode with `Esc`

### 3. Command Mode
- Access by pressing `:` in Normal mode
- Common commands:
  - `:w` - Save file
  - `:q` - Quit Vim
  - `:wq` or `:x` - Save and quit
  - `:q!` - Force quit without saving
  - `:w!` - Force save
  - `:u` - Undo last action
  - `:%!bash_command` - Execute bash command on text
    - Example: `:%!grep fun eg.txt`

### 4. Visual Mode
- Used for text selection and manipulation
- Enter with:
  - `v` - Character-wise selection
  - `Shift + V` - Line-wise selection
  - `Ctrl + V` or `Ctrl + Q` - Block-wise selection
- Operations in Visual mode:
  - `d` - Delete selected text
  - `y` - Yank (copy) selected text
  - `p` - Paste copied text

## Basic Vim Usage
1. Create/open file: `vim filename.txt`
2. Press `i` to enter Insert mode
3. Type your text
4. Press `Esc` to return to Normal mode
5. Use `:wq` to save and exit

---

