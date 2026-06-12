import ssl
import socket
from datetime import datetime

def check_ssl(hostname):
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as sock:
            sock.settimeout(5)
            sock.connect((hostname, 443))
            cert = sock.getpeercert()
        print("🔒 Certificado SSL/TLS válido")
        print(f"📅 Emitido para: {cert.get('subject', '')}")
        print(f"🗓️ Válido hasta: {cert['notAfter']}")
        expira = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
        dias = (expira - datetime.now()).days
        print(f"⏳ Días restantes: {dias}")
    except Exception as e:
        print("❌ Error SSL:", e)

if __name__ == "__main__":
    dominio = input("🌐 Dominio (ej: google.com): ")
    check_ssl(dominio)
