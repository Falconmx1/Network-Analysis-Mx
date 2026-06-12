import requests

def buscar_mac(mac):
    url = f"https://api.macvendors.com/{mac}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"🔍 Fabricante: {response.text}")
        else:
            print("❌ MAC no encontrada")
    except:
        print("❌ Error en la consulta")

if __name__ == "__main__":
    mac = input("🔌 Ingresa dirección MAC (ej: 00:11:22:AA:BB:CC): ")
    buscar_mac(mac)
