import nmap
import sys
import socket

if len(sys.argv) != 3:
    print(".python_nmap.py <host_address> <port_range>")
    sys.exit(0)

hostaddress = sys.argv[1]
portrange = sys.argv[2]
ipaddress = socket.gethostbyname(hostaddress)

print("_______________" * 6)
print("        please wait, Scanning The Host " + ipaddress)
print("_______________" * 6)

try:
    nmscan = nmap.PortScanner()
    nmscan.scan(hostaddress, portrange)
except nmap.PortScannerError as e:
    print("Nmap error:", str(e))
    sys.exit(0)
except Exception as e:
    print("Unexpected error:", str(e))
    sys.exit(0)

for host in nmscan.all_hosts():
    print("     Host : %s (%s)" % (host, hostaddress))
    print("        State : %s" % nmscan[host].state())
    
    for proto in nmscan[host].all_protocols():
        print("__________" * 6)
        print("protocols : %s " % proto)

        lport = sorted(nmscan[host][proto].keys())
        for port in lport:
            print("        port : %s \t state : %s " % (port, nmscan[host][proto][port]['state']))
            