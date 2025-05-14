import os
import socket

def get_network_info():
    # Get gateway IP
    gateway = os.popen('ip route show default').read().split()[2]
    
    # Get local IP and determine class
    local_ip = socket.gethostbyname(socket.gethostname())
    first_octet = int(local_ip.split('.')[0])
    
    if first_octet < 128:
        ip_class = 'A'
    elif first_octet < 192:
        ip_class = 'B'
    elif first_octet < 224:
        ip_class = 'C'
    else:
        ip_class = 'D/E'
    
    return gateway, local_ip, ip_class

def scan_network(network_prefix):
    print(f"Scanning {network_prefix}.0/24...\nActive hosts:")
    for i in range(1, 255):
        ip = f"{network_prefix}.{i}"
        if os.system(f"ping -c 1 -W 1 {ip} >/dev/null 2>&1") == 0:
            print(ip)

if __name__ == "__main__":
    gateway, local_ip, ip_class = get_network_info()
    network_prefix = '.'.join(gateway.split('.')[:3])
    
    print(f"Gateway IP: {gateway}")
    print(f"Your IP: {local_ip}")
    print(f"IP Class: {ip_class}")
    print(f"Network: {network_prefix}.0/24\n")
    
    scan_network(network_prefix)
    