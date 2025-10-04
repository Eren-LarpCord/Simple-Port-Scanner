import socket
import threading

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        sock.close()
    except:
        pass

def scan_target(ip, start_port, end_port):
    print(f"\nScanning target {ip} from port {start_port} to {end_port}...")
    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

if __name__ == "__main__":
    while True:
        target_ip = input("\nEnter target IP address: ")
        print("Full range supported: 1 to 65535 (like nmap).")
        start = int(input("Enter start port (default 1): ") or 1)
        end = int(input("Enter end port (default 65535): ") or 65535)

        scan_target(target_ip, start, end)

        again = input("\nDo you want to scan another target? (y/n): ").strip().lower()
        if again != 'y':
            print("Exiting scanner.")
            break
