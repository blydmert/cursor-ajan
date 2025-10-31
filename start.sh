#!/bin/bash

# AI Music Composition Assistant Startup Script

echo "?? AI M?zik Kompozisyon Asistan? Ba?lat?l?yor..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "? Python 3 bulunamad?. L?tfen Python 3.9+ y?kleyin."
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "? Node.js bulunamad?. L?tfen Node.js 16+ y?kleyin."
    exit 1
fi

echo "? Gerekli ara?lar kontrol edildi"
echo ""

# Backend setup
echo "?? Backend ba??ml?l?klar? y?kleniyor..."
cd backend

if [ ! -d "venv" ]; then
    echo "  ? Sanal ortam olu?turuluyor..."
    python3 -m venv venv
fi

echo "  ? Sanal ortam etkinle?tiriliyor..."
source venv/bin/activate 2>/dev/null || source venv/Scripts/activate 2>/dev/null

echo "  ? Paketler y?kleniyor..."
pip install -q -r requirements.txt

echo "? Backend haz?r"
echo ""

# Frontend setup
echo "?? Frontend ba??ml?l?klar? y?kleniyor..."
cd ../frontend

if [ ! -d "node_modules" ]; then
    echo "  ? npm install ?al??t?r?l?yor..."
    npm install --silent
else
    echo "  ? node_modules zaten mevcut"
fi

echo "? Frontend haz?r"
echo ""

# Create .env files if they don't exist
if [ ! -f "../backend/.env" ]; then
    echo "?? Backend .env dosyas? olu?turuluyor..."
    cp ../backend/.env.example ../backend/.env
fi

if [ ! -f ".env" ]; then
    echo "?? Frontend .env dosyas? olu?turuluyor..."
    cp .env.example .env
fi

echo ""
echo "?? Sunucular ba?lat?l?yor..."
echo ""
echo "  Backend:  http://localhost:8000"
echo "  Frontend: http://localhost:3000"
echo "  API Docs: http://localhost:8000/docs"
echo ""
echo "Durdurmak i?in Ctrl+C tu?lar?na bas?n"
echo ""

# Start backend in background
cd ../backend
source venv/bin/activate 2>/dev/null || source venv/Scripts/activate 2>/dev/null
python app.py &
BACKEND_PID=$!

# Wait for backend to start
sleep 3

# Start frontend
cd ../frontend
npm start &
FRONTEND_PID=$!

# Wait for both processes
wait $BACKEND_PID $FRONTEND_PID
