import os
import platform
import subprocess
import sys

def mostrar_banner():
    try:
        with open("banner.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("⚠️  No se encontró banner.txt")

def limpiar_pantalla():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def ejecutar_herramienta(ruta_script):
    """Ejecuta un script de Python de la carpeta tools"""
    try:
        subprocess.run([sys.executable, ruta_script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al ejecutar {ruta_script}: {e}")
    except FileNotFoundError:
        print(f"❌ No se encontró el archivo: {ruta_script}")
    input("\n🔹 Presiona Enter para volver al menú...")

def menu():
    print("\n" + "="*40)
    print("🔧 SELECCIONA UNA HERRAMIENTA:")
    print("="*40)
    print("1. 📡 Ping Tool")
    print("2. 🔬 Advanced Banner")
    print("3. 🎯 Banner Grabbing")
    print("4. 🔌 MAC Lookup")
    print("5. 📍 IP Geolocation")
    print("6. 🔒 SSL Checker")
    print("7. 🔄 Port Checker")
    print("0. 🚪 Salir")
    print("-"*40)

def main():
    while True:
        limpiar_pantalla()
        mostrar_banner()
        menu()
        opcion = input("👉 Opción: ")

        if opcion == "0":
            print("\n👋 ¡Gracias por usar Network Analysis Mx!\n")
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
            print("❌ Opción no válida. Intenta de nuevo.")
            input("\n🔹 Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
