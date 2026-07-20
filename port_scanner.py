import socket
import time

print("=" * 40)
print("      NETWORK PORT SCANNER")
print("=" * 40)

target = input("Enter Target IP / Domain: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid IP Address or Domain!")
    exit()

start_port = int(input("Enter Start Port: "))
end_port = int(input("Enter End Port: "))

print("\nScanning Target:", target_ip)
print("-" * 40)

start_time = time.time()

report = open("scan_report.txt", "w")
report.write("NETWORK PORT SCAN REPORT\n")
report.write("=" * 40 + "\n")
report.write(f"Target : {target}\n")
report.write(f"IP     : {target_ip}\n\n")
report.write("Open Ports:\n")

open_ports = 0

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)

    result = s.connect_ex((target_ip, port))

    if result == 0:
        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown"

        print(f"Port {port} OPEN ({service})")
        report.write(f"Port {port} OPEN ({service})\n")
        open_ports += 1

    s.close()

end_time = time.time()

print("-" * 40)
print("Scan Completed")
print("Total Open Ports:", open_ports)
print("Time Taken:", round(end_time - start_time, 2), "seconds")
print("Report saved as scan_report.txt")

report.write("\n")
report.write(f"Total Open Ports : {open_ports}\n")
report.write(f"Time Taken : {round(end_time - start_time,2)} seconds\n")
report.close()