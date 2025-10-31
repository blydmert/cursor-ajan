@echo off
REM AI Music Composition Assistant Startup Script for Windows

echo.
echo ?? AI M?zik Kompozisyon Asistan? Ba?lat?l?yor...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ? Python bulunamad?. L?tfen Python 3.9+ y?kleyin.
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo ? Node.js bulunamad?. L?tfen Node.js 16+ y?kleyin.
    pause
    exit /b 1
)

echo ? Gerekli ara?lar kontrol edildi
echo.

REM Backend setup
echo ?? Backend ba??ml?l?klar? y?kleniyor...
cd backend

if not exist "venv" (
    echo   ? Sanal ortam olu?turuluyor...
    python -m venv venv
)

echo   ? Sanal ortam etkinle?tiriliyor...
call venv\Scripts\activate.bat

echo   ? Paketler y?kleniyor...
pip install -q -r requirements.txt

echo ? Backend haz?r
echo.

REM Frontend setup
echo ?? Frontend ba??ml?l?klar? y?kleniyor...
cd ..\frontend

if not exist "node_modules" (
    echo   ? npm install ?al??t?r?l?yor...
    call npm install --silent
) else (
    echo   ? node_modules zaten mevcut
)

echo ? Frontend haz?r
echo.

REM Create .env files if they don't exist
if not exist "..\backend\.env" (
    echo ?? Backend .env dosyas? olu?turuluyor...
    copy ..\backend\.env.example ..\backend\.env
)

if not exist ".env" (
    echo ?? Frontend .env dosyas? olu?turuluyor...
    copy .env.example .env
)

echo.
echo ?? Sunucular ba?lat?l?yor...
echo.
echo   Backend:  http://localhost:8000
echo   Frontend: http://localhost:3000
echo   API Docs: http://localhost:8000/docs
echo.
echo Durdurmak i?in Ctrl+C tu?lar?na bas?n
echo.

REM Start backend in new window
cd ..\backend
start "AI Music Backend" cmd /k "venv\Scripts\activate.bat && python app.py"

REM Wait for backend to start
timeout /t 3 /nobreak >nul

REM Start frontend in new window
cd ..\frontend
start "AI Music Frontend" cmd /k "npm start"

echo.
echo ? Sunucular ba?lat?ld?!
echo.
pause
