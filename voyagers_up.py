import subprocess
import os

def lanzar_imperio_background():
    print('🚀 [AKI]: Desplegando servicios en segundo plano...')
    
    # Lanzar Web (Puerto 3000) sin bloquear
    subprocess.Popen('cd portal-web && start /b npm run dev', shell=True)
    
    # Lanzar App (Puerto 8081) sin bloquear
    subprocess.Popen('cd voyagers-app && start /b npx expo start', shell=True)
    
    print('✅ [VALENTINA]: Sistemas lanzados. Terminal LIBRE para Marcus.')
    print('🔗 Web activa en: http://localhost:3000')

if __name__ == '__main__':
    lanzar_imperio_background()
