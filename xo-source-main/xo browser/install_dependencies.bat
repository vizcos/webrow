@echo off
echo Installing Python dependencies...

rem Check if Python is installed
py --version > nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed. Please install Python first. https://python.org
    timeout /t 10
    exit /b 1
)

rem Check if pip is installed
py -m pip --version > nul 2>&1
if %errorlevel% neq 0 (
    echo Error: pip is not installed. Please install pip first.
    timeout /t 10
    exit /b 1
)

rem Install PyQt5
echo Installing PyQt5...
py -m pip install PyQt5

rem Install PyQtWebEngine
echo Installing PyQtWebEngine...
py -m pip install PyQtWebEngine

rem Install pyfiglet
echo Installing pyfiglet...
py -m pip install pyfiglet

rem Install rich
echo Installing rich...
py -m pip install rich

echo Installation complete.
echo You may now run the browser.
