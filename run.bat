@echo off
chcp 65001 >nul
title Cysic Testnet Launcher
cd /d "%~dp0"
python -c "import rich" 2>nul || (echo Installing dependencies... && pip install rich -q)
python cysic_launcher\main.py
pause
