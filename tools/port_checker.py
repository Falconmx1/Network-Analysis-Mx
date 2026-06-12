#!/usr/bin/env python3
import socket
import threading
from colorama import init, Fore, Style
init(autoreset=True)

def check_port(host, port, timeout=1):
    """Verifica si un puerto está abierto"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except:
        return False

def escanear_puerto_unico(host, puerto):
    """Escanea un puerto específico"""
    if check_port(host, puerto):
        print(Fore.GREEN + f"✅ Puerto {puerto} está ABIERTO")
        servicio = get_servicio(puerto)
        if servicio:
            print(Fore.CYAN + f"   📡 Servicio común: {servicio}")
    else:
        print(Fore.RED + f"❌ Puerto {puerto} está CERRADO")

def escanear_rango(host, puerto_inicio, puerto_fin):
    """Escanea un rango de puertos"""
    print(Fore.YELLOW + f"\n🔍 Escaneando puertos del {puerto_inicio} al {puerto_fin} en {host}")
    print(Fore.CYAN + "="*50)
    
    abiertos = []
    total = puerto_fin - puerto_inicio + 1
    contador = 0
    
    for puerto in range(puerto_inicio, puerto_fin + 1):
        contador += 1
        if check_port(host, puerto):
            servicio = get_servicio(puerto)
            print(Fore.GREEN + f"✅ Puerto {puerto} ABIERTO" + (f" - {servicio}" if servicio else ""))
            abiertos.append(puerto)
        
        # Mostrar progreso cada 10 puertos
        if contador % 10 == 0:
            porcentaje = (contador / total) * 100
            print(Fore.CYAN + f"📊 Progreso: {porcentaje:.1f}% ({contador}/{total})")
    
    print(Fore.GREEN + "\n" + "="*50)
    if abiertos:
        print(Fore.GREEN + f"📡 Puertos abiertos encontrados: {len(abiertos)}")
        print(Fore.WHITE + f"   {', '.join(map(str, abiertos))}")
    else:
        print(Fore.RED + "❌ No se encontraron puertos abiertos")

def escanear_populares(host):
    """Escanea los 20 puertos más comunes"""
    puertos_populares = {
        20: "FTP-Datos", 21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
        53: "DNS", 80: "HTTP", 110: "POP3", 111: "RPC", 135: "RPC",
        139: "NetBIOS", 143: "IMAP", 443: "HTTPS", 445: "SMB", 993: "IMAPS",
        995: "POP3S", 1723: "PPTP", 3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL",
        5900: "VNC", 6379: "Redis", 8080: "HTTP-Alt", 8443: "HTTPS-Alt", 27017: "MongoDB"
    }
    
    print(Fore.YELLOW + f"\n🔍 Escaneando puertos populares en {host}")
    print(Fore.CYAN + "="*50)
    
    abiertos = []
    for puerto, servicio in puertos_populares.items():
        if check_port(host, puerto):
            print(Fore.GREEN + f"✅ Puerto {puerto} ABIERTO - {servicio}")
            abiertos.append(puerto)
    
    if abiertos:
        print(Fore.GREEN + f"\n📡 Total: {len(abiertos)} puertos abiertos")
    else:
        print(Fore.RED + "\n❌ No se encontraron puertos abiertos")

def get_servicio(puerto):
    """Devuelve el nombre del servicio común para un puerto"""
    servicios = {
        20: "FTP (Datos)", 21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
        53: "DNS", 80: "HTTP", 110: "POP3", 111: "RPC", 135: "RPC",
        139: "NetBIOS", 143: "IMAP", 443: "HTTPS", 445: "SMB", 993: "IMAPS",
        995: "POP3S", 3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL", 5900: "VNC",
        8080: "HTTP-Alt", 8443: "HTTPS-Alt"
    }
    return servicios.get(puerto, None)

def main():
    print(Fore.MAGENTA + Style.BRIGHT + "\n" + "="*50)
    print(Fore.YELLOW + "🔄 PORT CHECKER - NETWORK ANALYSIS MX".center(50))
    print(Fore.MAGENTA + "="*50)
    
    host = input(Fore.CYAN + "\n🌐 Ingresa IP o dominio: " + Fore.WHITE)
    
    print(Fore.GREEN + "\n🔧 Modos de escaneo:")
    print("   1. Puerto único")
    print("   2. Rango de puertos")
    print("   3. Puertos populares (25 comunes)")
    
    modo = input(Fore.YELLOW + "\n👉 Selecciona modo [1/2/3]: " + Fore.WHITE)
    
    if modo == "1":
        puerto = int(input(Fore.CYAN + "🔌 Número de puerto: " + Fore.WHITE))
        escanear_puerto_unico(host, puerto)
    elif modo == "2":
        inicio = int(input(Fore.CYAN + "📊 Puerto inicial: " + Fore.WHITE))
        fin = int(input(Fore.CYAN + "📊 Puerto final: " + Fore.WHITE))
        if inicio > fin:
            print(Fore.RED + "❌ Error: El puerto inicial debe ser menor al final")
        else:
            escanear_rango(host, inicio, fin)
    elif modo == "3":
        escanear_populares(host)
    else:
        print(Fore.RED + "❌ Modo no válido")
    
    input(Fore.CYAN + "\n🔹 Presiona Enter para salir...")

if __name__ == "__main__":
    main()
