# Network Tools Project

A simple Python project for basic network analysis using two custom tools.

## Contents

1. **`network_sniffer.py`**  
   A packet sniffer built using the Scapy library, designed to capture and display network packets.

   ### Features:
   - Captures a fixed number of packets.
   - Prints a summary of each packet.
   - Saves the captured data to a text file (`network_log.txt`).

2. **`port_scanner.py`**  
   A simple tool to scan for open ports on a target IP address using the socket library.

   ### Features:
   - Accepts a domain or IP address as input.
   - Checks predefined common ports (e.g., 21, 22, 23, 80, 443).
   - Prints which ports are open.

## How to Run

Make sure Python is installed on your system.

### Run Packet Sniffer:
```bash
python network_sniffer.py
