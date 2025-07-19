import socket

def scan_ports(target, start_port, end_port):
    print(f"\n[*] Scanning {target} from port {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        sock.close()

    print("\n[*] Scan complete.")

# --- Input from user ---
try:
    target = input("Enter target IP or hostname: ")
    start_port = int(input("Enter start port (e.g., 20): "))
    end_port = int(input("Enter end port (e.g., 100): "))

    scan_ports(target, start_port, end_port)

except ValueError:
    print("[-] Please enter valid numbers for ports.")
except socket.gaierror:
    print("[-] Hostname could not be resolved.")
except KeyboardInterrupt:
    print("\n[-] Scan cancelled by user.")
except Exception as e:
    print(f"[-] Unexpected error: {e}")
