#!/usr/bin/env python3
import ssl
import socket
from datetime import datetime
from colorama import init, Fore, Style
init(autoreset=True)

def check_ssl(hostname, puerto=443):
    """Verifica certificado SSL/TLS de un dominio"""
    print(Fore.CYAN + f"\n🔒 Verificando SSL/TLS en {hostname}:{puerto}")
    
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as sock:
            sock.settimeout(10)
            sock.connect((hostname, puerto))
            cert = sock.getpeercert()
        
        print(Fore.GREEN + "\n" + "="*50)
        print(Fore.YELLOW + "🔐 INFORMACIÓN DEL CERTIFICADO".center(50))
        print(Fore.GREEN + "="*50)
        
        # Información del certificado
        subject = dict(x[0] for x in cert['subject'])
        issuer = dict(x[0] for x in cert['issuer'])
        
        info = [
            ("🎯 Dominio", hostname),
            ("🔑 Emitido para", subject.get('commonName', 'N/A')),
            ("🏢 Organización", subject.get('organizationName', 'N/A')),
            ("🔏 Emitido por", issuer.get('organizationName', 'N/A')),
            ("📅 Válido desde", cert['notBefore']),
            ("📅 Válido hasta", cert['notAfter']),
            ("🔢 Versión SSL/TLS", sock.version())
        ]
        
        for label, value in info:
            print(Fore.CYAN + f"{label}: " + Fore.WHITE + f"{value}")
        
        # Calcular días restantes
        fecha_exp = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
        dias_restantes = (fecha_exp - datetime.now()).days
        
        if dias_restantes < 0:
            print(Fore.RED + f"⏰ EXPIRADO hace {abs(dias_restantes)} días")
        elif dias_restantes < 30:
            print(Fore.YELLOW + f"⚠️  Caduca en {dias_restantes} días (próximo a vencer)")
        else:
            print(Fore.GREEN + f"✅ Válido por {dias_restantes} días más")
        
        print(Fore.GREEN + "="*50)
        
    except ssl.SSLError as e:
        print(Fore.RED + f"❌ Error SSL: {e}")
    except socket.timeout:
        print(Fore.RED + "⏰ Timeout - No hay respuesta")
    except Exception as e:
        print(Fore.RED + f"❌ Error: {e}")

def main():
    print(Fore.MAGENTA + Style.BRIGHT + "\n" + "="*50)
    print(Fore.YELLOW + "🔒 SSL CHECKER - NETWORK ANALYSIS MX".center(50))
    print(Fore.MAGENTA + "="*50)
    
    dominio = input(Fore.CYAN + "\n🌐 Dominio (ej: google.com): " + Fore.WHITE)
    puerto = input(Fore.CYAN + "🔌 Puerto [443]: " + Fore.WHITE)
    puerto = int(puerto) if puerto else 443
    
    check_ssl(dominio, puerto)

if __name__ == "__main__":
    main()
