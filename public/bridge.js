const fs = require('fs');
const fetch = require('node-fetch');

const CONFIG = {
    proyectoID: "gen-lang-client-0559117850",
    ruta: "/sdcard/VoyagersProyect/"
};

async function auditoriaAutonoma() {
    console.log("🔍 Iniciando Auditoría de Estado Voyagers...");
    
    try {
        const archivos = fs.readdirSync(CONFIG.ruta);
        const reporteArchivos = archivos.map(nombre => {
            const stats = fs.statSync(CONFIG.ruta + nombre);
            return {
                archivo: nombre,
                peso: (stats.size / 1024).toFixed(2) + " KB",
                modificado: stats.mtime.toLocaleString()
            };
        });

        console.table(reporteArchivos);

        // Verificación de salud de la base de datos
        const res = await fetch(`https://firestore.googleapis.com/v1/projects/${CONFIG.proyectoID}/databases/(default)/documents/analisis?pageSize=1`);
        console.log(res.ok ? "✅ Nube: Sincronizada" : "❌ Nube: Error de Autenticación");

    } catch (e) {
        console.log("⚠️ Error en auditoría:", e.message);
    }
}

async function auditoriaAutonoma() {
    // ... (mantiene la lógica de tabla de archivos anterior)

    // NUEVO: Lectura de Caja Negra
    console.log("\n📓 REVISANDO CAJA NEGRA (LOGS)...");
    const rutaLog = '/sdcard/VoyagersProyect/logs_autonomia.json';
    if (fs.existsSync(rutaLog)) {
        const logs = JSON.parse(fs.readFileSync(rutaLog));
        if (logs.length > 0) {
            console.table(logs);
        } else {
            console.log("✅ Sistema limpio: No hay errores registrados.");
        }
    }
}

