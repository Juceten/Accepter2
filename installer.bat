@echo off
setlocal EnableDelayedExpansion

rem Check if app is installed
if exist app\venv\ (
    set /p uninstall=The app is already installed. Do you want to uninstall it? [y/n] 
    echo.
    if /i "!uninstall!"=="y" (
        echo Uninstalling app...
        app\venv\Scripts\activate & pip uninstall -y -r app\requirements.txt & deactivate & rmdir app\venv /s /q
        echo App successfully uninstalled.
    ) else (
        echo Skipping uninstallation...
    )
    echo To install the app, please run the script again.
    pause
) else (
    set /p install=The app is not installed. Do you want to install it? [y/n] 
    echo.
    if /i "!install!"=="y" (
        echo Installing app...
        python -m venv app/venv
        app\venv\Scripts\activate & pip install -r app\requirements.txt & deactivate
        echo App successfully installed.
    ) else (
        echo Skipping installation...
    )
    echo To uninstall the app, please run the script again.
    pause
)
