import socket

def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    if result == 0:
        print(f"✅ Puerto {port} abierto")
    else:
        print(f"❌ Puerto {port} cerrado")
    sock.close()

if __name__ == "__main__":
    host = input("🌐 IP o dominio: ")
    puertos = input("🔌 Puertos separados por coma (ej: 22,80,443): ")
    for p in puertos.split(','):
        check_port(host, int(p.strip()))
