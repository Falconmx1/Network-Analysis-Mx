import subprocess
import platform

def ping(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        result = subprocess.run(
            ["ping", param, "4", host],
            capture_output=True,
            text=True,
            timeout=10
        )
        print(result.stdout)
        if result.returncode == 0:
            print("✅ Host responde")
        else:
            print("❌ Host sin respuesta")
    except subprocess.TimeoutExpired:
        print("⏰ Timeout - No hay respuesta")

if __name__ == "__main__":
    host = input("🌐 Ingresa host o IP a hacer ping: ")
    ping(host)
