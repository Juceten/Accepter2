@echo off
if exist app\venv\ (
    app\venv\Scripts\activate & pip uninstall -y -r app\requirements.txt & deactivate & rmdir app\venv /s /q  & pause
) else (
    echo venv is not installed...
    pause
)