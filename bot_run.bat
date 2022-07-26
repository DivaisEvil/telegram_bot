@echo off


call %~dp0venv\Scripts\activate

cd %~dp0telegram_bot

set TOKEN=5415950001:AAFD0FEr3BpXSuxsRghwEspEOiPqSOHBESs

python bot_telegram.py

pause