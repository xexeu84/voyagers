import os
import shutil

def limpieza_profunda():
    objetivos = [
        'voyagers_auto.py.txt', 
        'bridge_executor.py.txt', 
        'rutas_descargadas.txt.tmp',
        '__pycache__'
    ]
    
    print('🧹 [AKI]: Iniciando limpieza de archivos fantasma...')
    for obj in objetivos:
        if os.path.isfile(obj):
            os.remove(obj)
            print(f'[-] Archivo eliminado: {obj}')
        elif os.path.isdir(obj):
            shutil.rmtree(obj)
            print(f'[-] Carpeta eliminada: {obj}')
            
    print('✨ [LUKAS]: Entorno de trabajo optimizado y limpio.')

if __name__ == "__main__":
    limpieza_profunda()
