#!/usr/bin/env python3
# Network Analysis Mx - Versión PRO
# Con colores, menú mejorado y todas las funcionalidades

import os
import platform
import subprocess
import sys
import time

# Intentar importar colorama, si no está, instalarlo automáticamente
try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
except ImportError:
    print("Instalando colorama...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])
    from colorama import init, Fore, Back, Style
    init(autoreset=True)

def mostrar_banner():
    """Muestra el banner con colores"""
    limpiar_pantalla()
    try:
        with open("banner.txt", "r", encoding="utf-8") as f:
            banner_texto = f.read()
        # Colorear el banner
        print(Fore.CYAN + Style.BRIGHT + "=" * 50)
        for linea in banner_texto.split('\n'):
            if "NETWORK ANALYSIS MX" in linea.upper():
                print(Fore.YELLOW + Style.BRIGHT + linea.center(50))
            elif "ANALIZA" in linea.upper() or "HERRAMIENTAS" in linea:
                print(Fore.GREEN + linea.center(50))
            else:
                print(Fore.CYAN + linea.center(50))
        print(Fore.CYAN + Style.BRIGHT + "=" * 50)
    except FileNotFoundError:
        print(Fore.RED + "⚠️  No se encontró banner.txt")

def limpiar_pantalla():
    """Limpia la pantalla según el SO"""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def mostrar_carga(mensaje):
    """Animación de carga"""
    print(Fore.YELLOW + mensaje, end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    time.sleep(0.5)
    print(Fore.GREEN + " ✓")

def ejecutar_herramienta(ruta_script):
    """Ejecuta un script de Python de la carpeta tools"""
    try:
        mostrar_carga(f"🔄 Iniciando herramienta")
        result = subprocess.run([sys.executable, ruta_script], check=True)
        return result
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"❌ Error al ejecutar {ruta_script}: {e}")
    except FileNotFoundError:
        print(Fore.RED + f"❌ No se encontró el archivo: {ruta_script}")
    input(Fore.CYAN + "\n🔹 Presiona Enter para volver al menú...")

def mostrar_info_sistema():
    """Muestra información del sistema"""
    print(Fore.MAGENTA + "\n💻 Información del Sistema:")
    print(Fore.WHITE + f"   SO: {platform.system()} {platform.release()}")
    print(Fore.WHITE + f"   Python: {platform.python_version()}")
    print(Fore.WHITE + f"   Arquitectura: {platform.machine()}")

def menu():
    """Menú principal con colores"""
    print(Fore.CYAN + Style.BRIGHT + "\n" + "═" * 50)
    print(Fore.YELLOW + Style.BRIGHT + "🔧 SELECCIONA UNA HERRAMIENTA".center(50))
    print(Fore.CYAN + "═" * 50)
    
    opciones = [
        ("1", "📡", "Ping Tool", "Envío de paquetes ICMP"),
        ("2", "🔬", "Advanced Banner", "Obtención de banners"),
        ("3", "🎯", "Banner Grabbing", "Extracción de información"),
        ("4", "🔌", "MAC Lookup", "Consulta de fabricantes"),
        ("5", "📍", "IP Geolocation", "Localización en mapa"),
        ("6", "🔒", "SSL Checker", "Validación de certificados"),
        ("7", "🔄", "Port Checker", "Escaneo de puertos"),
        ("0", "🚪", "Salir", "Cerrar herramienta")
    ]
    
    for num, icono, nombre, desc in opciones:
        if num == "0":
            print(Fore.RED + f"   {num}. {icono} {nombre} - {desc}")
        else:
            print(Fore.GREEN + f"   {num}. {icono} {nombre} " + Fore.WHITE + f"- {desc}")
    
    print(Fore.CYAN + "═" * 50)

def main():
    """Función principal"""
    while True:
        limpiar_pantalla()
        mostrar_banner()
        mostrar_info_sistema()
        menu()
        
        opcion = input(Fore.YELLOW + "\n👉 Ingresa tu opción [0-7]: " + Fore.WHITE)
        
        if opcion == "0":
            print(Fore.MAGENTA + "\n👋 ¡Gracias por usar Network Analysis Mx!")
            print(Fore.CYAN + "🔐 Mantén tu red segura. ¡Hasta pronto!\n")
            time.sleep(1)
            break
        elif opcion == "1":
            ejecutar_herramienta("tools/ping_tool.py")
        elif opcion == "2":
            ejecutar_herramienta("tools/advanced_banner.py")
        elif opcion == "3":
            ejecutar_herramienta("tools/banner_grabbing.py")
        elif opcion == "4":
            ejecutar_herramienta("tools/mac_lookup.py")
        elif opcion == "5":
            ejecutar_herramienta("tools/ip_geolocation.py")
        elif opcion == "6":
            ejecutar_herramienta("tools/ssl_checker.py")
        elif opcion == "7":
            ejecutar_herramienta("tools/port_checker.py")
        else:
            print(Fore.RED + "❌ Opción no válida. Intenta de nuevo (0-7)")
            input(Fore.CYAN + "\n🔹 Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
