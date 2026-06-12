#!/bin/bash
# Network Analysis Mx - Instalador para Linux

echo "================================================"
echo "   NETWORK ANALYSIS MX - INSTALADOR LINUX"
echo "================================================"
echo ""

# Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo "[1/5] Verificando Python..."
if command -v python3 &>/dev/null; then
    echo -e "${GREEN}[OK] Python 3 encontrado${NC}"
else
    echo -e "${RED}[ERROR] Python 3 no encontrado${NC}"
    echo "Instalando Python..."
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip
fi

echo ""
echo "[2/5] Instalando dependencias..."
pip3 install colorama requests

echo ""
echo "[3/5] Dando permisos de ejecución..."
chmod +x network_analysis_mx.py
chmod +x tools/*.py

echo ""
echo "[4/5] Creando acceso directo en el escritorio..."
cat > ~/Desktop/Network-Analysis-Mx.desktop << EOF
[Desktop Entry]
Name=Network Analysis Mx
Comment=Herramienta de análisis de red
Exec=$PWD/network_analysis_mx.py
Icon=utilities-terminal
Terminal=true
Type=Application
Categories=Network;Security;
EOF

chmod +x ~/Desktop/Network-Analysis-Mx.desktop
echo -e "${GREEN}[OK] Acceso directo creado${NC}"

echo ""
echo "[5/5] Instalación completada!"
echo ""
echo "================================================"
echo -e "${GREEN}   ¡INSTALACIÓN EXITOSA!${NC}"
echo "================================================"
echo ""
echo "Para ejecutar la herramienta:"
echo "  1. Desde el escritorio: Doble clic en Network-Analysis-Mx"
echo "  2. Desde terminal: python3 network_analysis_mx.py"
echo ""
