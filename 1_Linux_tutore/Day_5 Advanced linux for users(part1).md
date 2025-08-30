# Linux User and Permission Management

## User Account Management

### Password Management
```bash
# Change or set user password
sudo passwd <username>

# Example
sudo passwd solace1
```

### User ID Modification
```bash
# Change user ID
sudo usermod -u <new_id> <username>

# Example
sudo usermod -u 1002 solace1

# Change group ID for user
sudo usermod -g <group_id> <username>

# Example
sudo usermod -g 1003 solace1
```

### User Deletion
```bash
# Delete user and remove home directory
sudo userdel -r <username>

# Example
sudo userdel -r solace1
```

### Home Directory Creation
```bash
# Create home directory for useradd users
sudo mkhomedir_helper <username>

# Example
sudo mkhomedir_helper solace1
```

### Shell Type Modification
```bash
# Change user's default shell
sudo usermod -s /bin/<shell_type> <username>

# Examples
sudo usermod -s /bin/zsh solace1    # Change to ZSH
sudo usermod -s /bin/bash solace1   # Change to Bash
```

> **Note**: SH shell has limited functionality (e.g., `Ctrl+L` for clear doesn't work)

## Group Management

### Group Operations
```bash
# Create new group
sudo addgroup <groupname>

# Example
sudo addgroup solaces

# Add user to group
sudo usermod -aG <groupname> <username>

# Example
sudo usermod -aG solaces solace1

# Verify group membership
groups <username>

# Example
groups solace1

# Remove user from group
sudo gpasswd -d <username> <groupname>

# Example
sudo gpasswd -d solace1 solaces
```

> **Note**: Users in the same group can access each other's files but cannot create files in other users' directories without explicit permissions.

## Sudo Privileges Management

### Granting Sudo Access
```bash
# Edit sudoers file safely
sudo visudo
```

In the sudoers file, add the following line under "User Privilege Specification":
```
<username> ALL=(ALL:ALL)ALL
```

Example:
```
# User Privilege Specification
root    ALL=(ALL:ALL)ALL
solace1 ALL=(ALL:ALL)ALL
```

> **Warning**: Always use `visudo` to edit sudoers file as it validates syntax before saving.

## File Permissions and Ownership

### Understanding File Permissions
Use `ls -l` to view detailed file information:

```
permissions  links  user    group   size    date        filename
-rw-r--r--   1      solace1 solaces 4096    Dec 19 10:43 file.txt
drwx-wxr-x   2      solace1 solaces 4086    Mar 10 05:00 fold1
```

- First character: `-` for files, `d` for directories
- Next 9 characters: permissions divided into three groups of three:
  - User (owner) permissions
  - Group permissions  
  - Other (everyone else) permissions

### Changing File Ownership
```bash
# Change file owner and group
sudo chown <username>:<groupname> <filename>

# Examples
sudo chown solace2:solaces file.txt
sudo chown solace1:solaces fold1
```

### Permission Management with chmod

#### Symbolic Notation
```bash
# Basic syntax
chmod <who><operation><permissions> <filename>

# Examples
chmod a+x file.txt        # Add execute permission for all
chmod g+r file.txt        # Add read permission for group
chmod u+x file.txt        # Add execute permission for user
chmod o-w file.txt        # Remove write permission for others

# Complex example
chmod a+rwx,u-rw,g-x,o-xw file.txt
```

#### Numeric Notation
Permissions are represented numerically:
- Read (r) = 4
- Write (w) = 2  
- Execute (x) = 1

```bash
# Syntax
chmod <user><group><other> <filename>

# Examples
chmod 621 file.txt    # rw--w---x
chmod 777 fold1       # rwxrwxrwx (full permissions for all)
```

### Permission Examples
- `755` = rwxr-xr-x (user: rwx, group: r-x, other: r-x)
- `644` = rw-r--r-- (user: rw-, group: r--, other: r--)
- `700` = rwx------ (user: rwx, group: ---, other: ---)

---

**Best Practices**:
- Use the principle of least privilege when assigning permissions
- Regularly audit user accounts and permissions
- Use groups to manage access rather than individual user permissions
- Always test permission changes in a safe environment before production use

*Note: Proper permission management is crucial for system security. Always understand the implications of permission changes before applying them.*

