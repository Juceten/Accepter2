@echo off
if exist Accepter2.zip (
    del Accepter2.zip
)
if not exist app\venv\ (
    python -m venv app/venv
    app\venv\Scripts\activate & pip install -r app\requirements.txt & deactivate & pause
) else (
    echo venv is already installed...
    pause
)