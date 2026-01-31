import subprocess
import os
def ejecutar_comando_autonomo(comando):
    try:
        proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = proceso.communicate()
        return stdout, stderr
    except Exception as e:
        return None, str(e)
if __name__ == "__main__":
    print('🚀 [PUENTE INSTALADO]')
