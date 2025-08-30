# Managing Services

Services can be started, stopped, and managed using system control tools.

## System Control Commands

### Using systemctl
```bash
sudo systemctl start <service_name>    # Start service
sudo systemctl stop <service_name>     # Stop service
sudo systemctl enable <service_name>   # Start service at boot
sudo systemctl disable <service_name>  # Disable service at boot
sudo systemctl status <service_name>   # Check service status
```

### Using service command
```bash
sudo service <service_name> start
sudo service <service_name> stop
sudo service <service_name> status
# Also supports enable, disable, etc.
```

**Example**: Starting Apache web server
```bash
sudo systemctl start apache2
sudo service apache2 start
```

## Null Device (/dev/null)

The null device acts as a "bit bucket" for discarding unwanted output.

### Output Redirection
- **STDERR** (Error output): File descriptor `2`
- **STDOUT** (Standard output): File descriptor `1`

### Redirecting Output
```bash
# Redirect errors to file
command 2> file_name

# Redirect errors to null device (discard)
command 2> /dev/null

# Redirect standard output to file
command 1> file_name

# Redirect standard output to null device
command 1> /dev/null
```

**Example**: 
```bash
sudo systemctl start apache3 2> xy.txt      # Save errors to file
sudo systemctl start apache3 2> /dev/null   # Discard errors
```

> **Note**: `/dev/null` is always empty and acts like a black hole for data.

## Symbolic Linking

Symbolic links create shortcuts to files or directories (similar to Windows shortcuts).

### Creating Symbolic Links
```bash
ln -s source_file_path link_name
```

**Example**:
```bash
ln -s ~/fold1/fold2/fold3/fold4/fold5/file.txt sol
```

Symbolic links appear with `l` permission prefix and show the target path:
```
lrwxrwxr-x sol -> /home/solace/fold1/fold2/fold3/fold4/fold5/file.txt
```

## Alias

Aliases create custom names for command sequences.

### Creating Temporary Aliases
```bash
alias rex="ls -la"
```

### Permanent Aliases
Add to shell configuration files:
- **Bash**: `~/.bashrc`
- **Zsh**: `~/.zshrc`
- **Fish**: `~/.config/fish/config.fish`

**Example** for Bash:
```bash
nano ~/.bashrc
# Add to file:
alias rex="ls -la"
```

## Wget

Download files from websites or servers:
```bash
wget [options] [URL]
```

**Example**:
```bash
wget http://tldp.org/LDP/intro-linux/intro-linux.pdf
```

## Find Command

Search for files and directories with various criteria.

### Basic Syntax
```bash
find [search_path] [option] [search_pattern]
```

### Examples
```bash
find / -name "linux"                    # Find files named "linux" from root
find /home -perm 777                    # Find files with 777 permissions in /home
find /home/solace -type f -perm 4000    # Find SUID files in user directory
find -type d | find -type f             # Find both directories and files
find / -type f -perm 1000 > /dev/null   # Find sticky bit files, discard output
```

## Tmux Terminal Multiplexer

Tmux helps organize terminal sessions with multiple windows and panes.

### Configuration
Create `~/.tmux.conf` with:
```
unbind C-b
unbind l
set -g prefix C-a
unbind %
bind e split-window -h
bind o split-window -v
set -g base-index 1
setw -g pane-base-index 1
```

### Tmux Commands
- **Split horizontally**: `Ctrl+A` then `o`
- **Split vertically**: `Ctrl+A` then `e`
- **Exit**: `Ctrl+A` then `x` or type `exit`
- **Create tab**: `Ctrl+A` then `c`
- **Rename tab**: `Ctrl+A` then `,` (comma)
- **Switch tabs**: `Ctrl+A` then tab number
- **Switch partitions**: `Ctrl+A` then arrow keys

> **Note**: The super key prefix is `Ctrl+A` in this configuration.

