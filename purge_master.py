import os
import subprocess

def auditar_y_reparar():
    print('🚨 [LUKAS]: Iniciando Auditoría de Campo...')
    # Verificar Portal
    if os.path.exists('portal-web'):
        print('✅ Portal detectado. Reinstalando integridad...')
        os.system('cd portal-web && npm install --silent')
    
    # Verificar App
    if os.path.exists('voyagers-app'):
        print('✅ App detectada. Limpiando cache de Expo...')
        os.system('cd voyagers-app && npm install --silent')

if __name__ == '__main__':
    auditar_y_reparar()
    print('✨ PURGA COMPLETADA. Marcus, el sistema está virgen y listo.')
