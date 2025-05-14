import sys
import socket

if len(sys.argv) != 4:
    print("Usage: python scanner.py <host> <start_port> <end_port>")
    sys.exit(1)

host = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])
print("...Please wait while scanning the host " + host)
for port in range(start, end+1):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((host, port))
        print(f"Port {port}: Open")
        s.close()
    except:
        pass
    