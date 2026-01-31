import os
import sys

def auto_write_module(filename, content):
    """Aki escribe el código directamente en el sistema de archivos"""
    try:
        path = os.path.join(os.getcwd(), filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f">>> [AKI] Archivo '{filename}' actualizado con éxito.")
        return True
    except Exception as e:
        print(f">>> [LUKAS] Error de escritura: {e}")
        return False

if __name__ == "__main__":
    # Este módulo será llamado por el Core cuando detecte código nuevo
    if len(sys.argv) > 2:
        auto_write_module(sys.argv[1], sys.argv[2])