@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if errorlevel 1 (
    echo Python launcher was not found. Install Python 3.10 or newer and enable Add Python to PATH.
    pause
    exit /b 1
)
py -3 -m venv .venv
if errorlevel 1 goto :error
.venv\Scripts\python.exe -m pip install --upgrade pip
if errorlevel 1 goto :error
.venv\Scripts\python.exe -m pip install -r requirements.txt
if errorlevel 1 goto :error
if not exist .env copy .env.example .env >nul
echo.
echo Python dependencies installed.
echo Edit the .env file and configure MySQL before running run_windows.bat.
pause
exit /b 0
:error
echo Setup failed. Check the error above.
pause
exit /b 1
