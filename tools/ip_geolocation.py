import requests

def geolocalizar(ip):
    url = f"http://ip-api.com/json/{ip}"
    try:
        data = requests.get(url, timeout=10).json()
        if data['status'] == 'success':
            print(f"""
📍 IP: {data['query']}
🌍 País: {data['country']}
🏙️ Ciudad: {data['city']}
📌 Región: {data['regionName']}
🗺️ Coordenadas: {data['lat']}, {data['lon']}
📡 ISP: {data['isp']}
""")
        else:
            print("❌ IP no válida o privada")
    except:
        print("❌ Error en la geolocalización")

if __name__ == "__main__":
    ip = input("🌐 Ingresa IP pública: ")
    geolocalizar(ip)
