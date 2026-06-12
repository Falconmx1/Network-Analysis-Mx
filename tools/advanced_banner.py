import socket

def get_banner(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((host, port))
        sock.send(b"HEAD / HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n")
        banner = sock.recv(1024).decode().strip()
        print("📜 Banner obtenido:\n", banner)
    except Exception as e:
        print("❌ Error:", e)
    finally:
        sock.close()

if __name__ == "__main__":
    host = input("🌐 IP o dominio: ")
    port = int(input("🔌 Puerto (ej: 80, 443): "))
    get_banner(host, port)
