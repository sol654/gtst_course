#!/bin/bash

# Check if two arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <IP_ADDRESS> <NSE_SCRIPT>"
    echo "Example: $0 192.168.1.1 http-enum"
    exit 1
fi

IP_ADDRESS=$1
NSE_SCRIPT=$2

# Check if nmap is installed
if ! command -v nmap &> /dev/null; then
    echo "Error: nmap is not installed. Please install nmap first."
    exit 1
fi

# Run nmap scan with the specified NSE script
echo "Running Nmap scan on $IP_ADDRESS with $NSE_SCRIPT script..."
nmap -sV --script=$NSE_SCRIPT $IP_ADDRESS

echo "Scan completed."
