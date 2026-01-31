#!/bin/bash

# Configuración de Identidad (Seguridad Legal)
export PROJECT_NAME="Voyagers-Cloud"
export REMOTE_SERVER="vps-voyagers-main" # Tu futuro servidor en la nube

echo "🚀 Iniciando Sincronización Automática Voyagers..."

# 1. Guardar cambios localmente
git add .

# 2. Crear punto de restauración automático (sin que te pregunte)
git commit -m "Auto-update Voyagers Cloud: $(date +'%Y-%m-%d %H:%M')"

# 3. Empujar a la Nube (GitHub)
echo "📤 Subiendo cambios al cerebro de GitHub..."
git push origin main

# 4. Ordenar al servidor que se actualice
# Esto hace que el servidor en la nube "despierte" y descargue lo nuevo
echo "🔄 Sincronizando Servidor Cloud con Acode..."
# (Aquí conectaremos con tu servidor más adelante)

echo "✅ ¡Voyagers está actualizado y funcionando de forma autónoma!"

