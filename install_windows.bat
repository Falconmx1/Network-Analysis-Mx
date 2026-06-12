@echo off
title Network Analysis Mx - Instalador
color 0A

echo ================================================
echo    NETWORK ANALYSIS MX - INSTALADOR WINDOWS
echo ================================================
echo.

echo [1/4] Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no encontrado
    echo Descarga Python desde: https://www.python.org/downloads/
    echo Asegurate de marcar "Add Python to PATH"
    pause
    exit /b 1
)
echo [OK] Python encontrado

echo.
echo [2/4] Instalando dependencias...
pip install colorama requests

echo.
echo [3/4] Creando acceso directo...
powershell -Command "$WS = New-Object -ComObject WScript.Shell; $SC = $WS.CreateShortcut('%USERPROFILE%\Desktop\Network Analysis Mx.lnk'); $SC.TargetPath = '%CD%\network_analysis_mx.py'; $SC.WorkingDirectory = '%CD%'; $SC.Save()"
echo [OK] Acceso directo creado en el escritorio

echo.
echo [4/4] Instalacion completada!
echo.
echo ================================================
echo    ¡INSTALACION EXITOSA!
echo ================================================
echo.
echo Para ejecutar la herramienta:
echo   1. Desde el escritorio: Doble clic en el acceso directo
echo   2. Desde terminal: python network_analysis_mx.py
echo.
pause
