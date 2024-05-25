#!/bin/bash

activate=$(find . -type f -name activate | grep .)
if [ $? -eq "0" ]; then 
    echo '[+] Entorno virtual encontrado...'
else
    echo '[+] Creando entorno virtual de nombre .venv'
    python3 -m venv .venv
    activate=".venv/bin/activate"
fi

echo '[+] Activando entorno virtual'
source $activate
echo '[+] Instalando dependecias'
pip3 install -r requirements.txt &>/dev/null

if [ $? -ne "0" ]; then
    echo '[!] Algo ha salido mal.'
    exit 1
fi



# Windows
python -m venv .
Scripts\activate
pip install -r requirements.txt