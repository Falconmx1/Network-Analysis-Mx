import socket

def banner_grabbing(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((host, port))
        if port == 80:
            sock.send(b"HEAD / HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n")
        elif port == 21:
            pass  # FTP
        elif port == 22:
            pass  # SSH
        banner = sock.recv(1024).decode().strip()
        print("🎯 Banner:", banner)
    except:
        print("❌ No se pudo obtener banner")
    finally:
        sock.close()

if __name__ == "__main__":
    host = input("🌐 IP o dominio: ")
    port = int(input("🔌 Puerto (21, 22, 80, 443, etc): "))
    banner_grabbing(host, port)
