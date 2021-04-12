@echo off
if exist app\venv\ (
    app\venv\Scripts\activate & python app\main.py & deactivate
) else (
    echo venv not installed please run install.bat...
    pause
)