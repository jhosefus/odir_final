#!/bin/bash

echo "Creando entorno virtual..."
python3 -m venv odir_env

echo "Activando entorno virtual..."
source odir_env/bin/activate

echo "Instalando dependencias..."
pip install -r requirements.txt

echo "Creando carpetas necesarias..."
mkdir -p data images diagrams modules

echo "Inicializando CSV vacío..."
touch data/odir_metadata.csv

echo "Proyecto listo. Ejecutar con: source odir_env/bin/activate && python main.py"
