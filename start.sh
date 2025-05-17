#!/bin/bash

# Script para iniciar o Site Lite
echo "Iniciando o Site Lite..."

# Ativar ambiente virtual
source venv/bin/activate

# Iniciar o servidor Flask
cd src
python main.py

echo "Servidor iniciado em http://localhost:5000"
