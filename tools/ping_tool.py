#!/usr/bin/env python3
import subprocess
import platform
import time
import sys
from colorama import init, Fore, Style
init(autoreset=True)

def ping_continuo(host):
    """Realiza ping continuo hasta que el usuario lo detenga"""
    param = "-n" if platform.system().lower() == "windows" else "-c"
    contador = 0
    exitosos = 0
    
    print(Fore.CYAN + f"\n📡 Iniciando ping continuo a {host}")
    print(Fore.YELLOW + "Presiona Ctrl+C para detener\n")
    time.sleep(1)
    
    try:
        while True:
            contador += 1
            resultado = subprocess.run(
                ["ping", param, "1", host],
                capture_output=True,
                text=True
            )
            
            if resultado.returncode == 0:
                exitosos += 1
                print(Fore.GREEN + f"[{contador}] ✅ Respuesta recibida")
            else:
                print(Fore.RED + f"[{contador}] ❌ Sin respuesta")
            
            time.sleep(1)
            
            # Mostrar estadísticas cada 10 pings
            if contador % 10 == 0:
                porcentaje = (exitosos / contador) * 100
                print(Fore.CYAN + f"\n📊 Estadísticas: {exitosos}/{contador} ({porcentaje:.1f}% éxito)\n")
    
    except KeyboardInterrupt:
        print(Fore.YELLOW + f"\n\n📊 Resumen final: {exitosos}/{contador} paquetes recibidos")
        porcentaje = (exitosos / contador) * 100 if contador > 0 else 0
        print(Fore.GREEN + f"📈 Tasa de éxito: {porcentaje:.1f}%")

def ping_normal(host, cantidad=4):
    """Ping normal con cantidad específica de paquetes"""
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        resultado = subprocess.run(
            ["ping", param, str(cantidad), host],
            capture_output=True,
            text=True,
            timeout=10
        )
        print(Fore.CYAN + resultado.stdout)
        if resultado.returncode == 0:
            print(Fore.GREEN + "✅ Host accesible")
        else:
            print(Fore.RED + "❌ Host inaccesible")
    except subprocess.TimeoutExpired:
        print(Fore.RED + "⏰ Timeout - No hay respuesta")

def main():
    print(Fore.MAGENTA + Style.BRIGHT + "\n" + "="*50)
    print(Fore.YELLOW + "📡 PING TOOL - NETWORK ANALYSIS MX".center(50))
    print(Fore.MAGENTA + "="*50)
    
    host = input(Fore.CYAN + "\n🌐 Ingresa host o IP: " + Fore.WHITE)
    
    print(Fore.GREEN + "\n🔧 Modos de uso:")
    print("   1. Ping normal (4 paquetes)")
    print("   2. Ping continuo (Ctrl+C para detener)")
    
    modo = input(Fore.YELLOW + "\n👉 Selecciona modo [1/2]: " + Fore.WHITE)
    
    if modo == "1":
        cantidad = input(Fore.CYAN + "📦 Cantidad de paquetes [4]: " + Fore.WHITE)
        cantidad = int(cantidad) if cantidad else 4
        ping_normal(host, cantidad)
    elif modo == "2":
        ping_continuo(host)
    else:
        print(Fore.RED + "❌ Modo no válido")

if __name__ == "__main__":
    main()
