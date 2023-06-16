import socket
import threading
import time

def get_local_ip():
    try:
        host = socket.gethostname()
        ip = socket.gethostbyname(host)
        return ip
    except socket.gaierror:
        print(f'Error: Could not retrieve local IP address')
        return None

def port_scan(host, start_port, end_port):
    open_ports = []
    threads = []

    def scan_port(port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(port,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return open_ports

# Specify port range
start_port = 1
end_port = 1024

# Retrieve local IP address
ip = get_local_ip()
if ip:
    # Call port_scan function with specified arguments
    open_ports = port_scan(ip, start_port, end_port)

    # Print results
    print(f'Open ports on {ip} between {start_port} and {end_port}: {open_ports}')


time.sleep(10)


