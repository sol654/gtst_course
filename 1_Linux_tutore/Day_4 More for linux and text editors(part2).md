
# Linux Text Editors and User Management

## Nano Text Editor

**GNU Nano** is a user-friendly, open-source command-line text editor that comes pre-installed on most Linux distributions.

### Basic Usage
```bash
nano filename.txt
```

### Essential Shortcuts
- `Ctrl + S` - Save file
- `Alt + E` - Redo
- `Alt + U` - Undo
- `Ctrl + X` - Exit Nano
- `Ctrl + Shift + C` - Copy selected text
- `Ctrl + Shift + X` - Cut selected text
- `Ctrl + Shift + V` - Paste text

> **Note**: In Nano documentation, `^` represents the `Ctrl` key

### File Status Indicator
- An asterisk (`*`) next to the filename indicates unsaved changes

### Advanced Feature: File Appending
- `Ctrl + R` - Insert content from another file into the current file
- Example: While editing, press `Ctrl + R` and enter the path to the file you want to append

---

## Linux User Management

### User and Group Basics
- Every user belongs to at least one group
- Creating a user automatically creates a corresponding group
- Users can be added to additional groups
- Each user has separate files, directories, and application settings

### User Identification
```bash
whoami  # Display current username
```

### Creating Users

#### Using `adduser` (Interactive)
```bash
sudo adduser username
```
- Creates home directory automatically
- Prompts for detailed user information
- Sets up default shell as Bash
- Creates corresponding user group

#### Using `useradd` (Non-interactive)
```bash
sudo useradd username
```
- Does not create home directory by default
- Does not set password automatically
- Uses SH shell by default
- Requires manual configuration

### User ID Ranges
- **Root**: UID 0
- **System Users**: UID 1-999
- **Regular Users**: UID 1000+
  - First user: UID 1000
  - Subsequent users: 1001, 1002, etc.

### Important System Files

#### `/etc/passwd`
Contains user account information (no passwords)
```bash
cat /etc/passwd
```

#### `/etc/shadow`
Stores encrypted passwords (requires root access)
```bash
sudo cat /etc/shadow
```

#### `/etc/skel`
Contains skeleton files copied to new user home directories

### User ID Management
```bash
id          # Show current user ID information
id username # Show specific user ID information
```

Example output:
```
uid=1000(solace) gid=1000(solace) groups=1000(solace),4(adm),24(cdrom)
```

### Default Behavior Notes
- When prompted with `[Y/n]` (capital Y indicates default yes), pressing Enter selects "yes"
- User creation typically requires `sudo` privileges or root access
- For `useradd`, additional steps are needed to create home directory and set password

---

**Best Practices**:
- Use `adduser` for interactive user creation with proper defaults
- Use `useradd` for automated scripting with explicit parameters
- Regularly review `/etc/passwd` and `/etc/shadow` for security auditing
- Understand UID/GID assignments for proper permission management

