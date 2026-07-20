# Network Port Scanner

## Description
A Python-based Network Port Scanner that scans a target IP address or domain to identify open TCP ports using socket programming.

## Features
- Scan any IP address or domain
- Detect open TCP ports
- Display common service names
- Generate scan report
- Measure scan execution time

## Technologies Used
- Python
- Socket Programming

## How to Run

1. Open the terminal.
2. Run the following command:

python port_scanner.py

3. Enter:
- Target IP / Domain
- Start Port
- End Port

## Sample Output

```text
Enter Target IP / Domain: scanme.nmap.org
Enter Start Port: 20
Enter End Port: 100

Scanning Target: 45.33.32.156
----------------------------------------
Port 80 OPEN (http)
----------------------------------------

Scan Completed
Total Open Ports: 1
Time Taken: 40.91 seconds
Report saved as scan_report.txt
```

## Author

Maha Lakshmi
