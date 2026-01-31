const { execSync } = require('child_process');
const fs = require('fs');

function vigilanciaProactiva() {
    try {
        // 1. Verificación de Batería
        const bat //= JSON.parse(execSync('termux-battery-status').toString());
        if (bat.percentage < 15 && bat.status !== "PLUGGED_AC") {
            execSync(`termux-notification -c "Batería Crítica (${bat.percentage}%). No inicies análisis pesados." -t "⚠️ Alerta de Energía" --priority high`);
        }

        // 2. Verificación de logs (Caja Negra)
        const rutaLog = '/sdcard/VoyagersProyect/logs_autonomia.json';
        if (fs.existsSync(rutaLog)) {
            const logs = JSON.parse(fs.readFileSync(rutaLog));
            if (logs.length > 0) {
                const ultimoError = logs[logs.length - 1].error;
                execSync(`termux-notification -c "Último error: ${ultimoError}" -t "📓 Reporte de Caja Negra" --priority low`);
            }
        }

        // 3. Limpieza automática silenciosa
        // (Aquí sigue tu lógica de purga de logs para ahorrar espacio)

    } catch (e) {
        // Silencioso para no interrumpir la terminal
    }
}

vigilanciaProactiva();
