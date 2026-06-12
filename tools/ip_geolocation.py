#!/usr/bin/env python3
import requests
import webbrowser
import json
import os
from colorama import init, Fore, Style
init(autoreset=True)

def geolocalizar(ip):
    """Obtiene geolocalización completa de una IP"""
    print(Fore.CYAN + f"\n📍 Geolocalizando IP: {ip}")
    
    # Usar ip-api.com (gratuito, sin API key)
    url = f"http://ip-api.com/json/{ip}"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if data['status'] == 'success':
            print(Fore.GREEN + "\n" + "="*50)
            print(Fore.YELLOW + "📍 INFORMACIÓN DE GEOLOCALIZACIÓN".center(50))
            print(Fore.GREEN + "="*50)
            
            info = [
                ("🌐 IP", data['query']),
                ("🌍 País", f"{data['country']} ({data['countryCode']})"),
                ("🏙️ Ciudad", data['city']),
                ("📍 Región", data['regionName']),
                ("📌 Código Postal", data.get('zip', 'N/A')),
                ("🗺️ Latitud", data['lat']),
                ("🗺️ Longitud", data['lon']),
                ("📡 ISP", data['isp']),
                ("🏢 Organización", data.get('org', 'N/A')),
                ("🌐 AS", data.get('as', 'N/A')),
                ("🔌 Zona Horaria", data['timezone']),
                ("📱 Mobile", "Sí" if data.get('mobile') else "No")
            ]
            
            for label, value in info:
                print(Fore.CYAN + f"{label}: " + Fore.WHITE + f"{value}")
            
            print(Fore.GREEN + "="*50)
            
            # Guardar en archivo JSON
            with open(f"geolocation_{ip}.json", "w") as f:
                json.dump(data, f, indent=2)
            print(Fore.GREEN + f"💾 Datos guardados en: geolocation_{ip}.json")
            
            # Preguntar si quiere ver en mapa
            ver_mapa = input(Fore.YELLOW + "\n🗺️ ¿Abrir en Google Maps? [s/N]: " + Fore.WHITE)
            if ver_mapa.lower() == 's':
                url_mapa = f"https://www.google.com/maps?q={data['lat']},{data['lon']}"
                webbrowser.open(url_mapa)
                print(Fore.GREEN + "🌍 Abriendo mapa en tu navegador...")
            
            return data
        else:
            print(Fore.RED + f"❌ Error: {data.get('message', 'IP no válida')}")
            return None
            
    except requests.RequestException as e:
        print(Fore.RED + f"❌ Error de conexión: {e}")
        return None

def mi_ip():
    """Obtiene la IP pública del usuario"""
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=10)
        ip = response.json()['ip']
        print(Fore.GREEN + f"\n🌐 Tu IP pública es: {Fore.YELLOW}{ip}")
        return ip
    except:
        print(Fore.RED + "❌ No se pudo obtener tu IP pública")
        return None

def main():
    print(Fore.MAGENTA + Style.BRIGHT + "\n" + "="*50)
    print(Fore.YELLOW + "📍 IP GEOLOCATION - NETWORK ANALYSIS MX".center(50))
    print(Fore.MAGENTA + "="*50)
    
    print(Fore.GREEN + "\n🔧 Opciones:")
    print("   1. Geolocalizar mi IP")
    print("   2. Geolocalizar IP específica")
    
    opcion = input(Fore.YELLOW + "\n👉 Selecciona [1/2]: " + Fore.WHITE)
    
    if opcion == "1":
        ip = mi_ip()
        if ip:
            geolocalizar(ip)
    elif opcion == "2":
        ip = input(Fore.CYAN + "🌐 Ingresa IP a geolocalizar: " + Fore.WHITE)
        geolocalizar(ip)
    else:
        print(Fore.RED + "❌ Opción no válida")

if __name__ == "__main__":
    main()
