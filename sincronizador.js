const fs = require('fs');
const fetch = require('node-fetch');

const PROYECTO_ID = "gen-lang-client-0559117850";
const RUTA_LOCAL = "/sdcard/VoyagersProyect/analizador.js";

async function sincronizar() {
    console.log("☁️ Conectando con el Servidor Maestro de Gemini...");
    const url = `https://firestore.googleapis.com/v1/projects/${PROYECTO_ID}/databases/(default)/documents/nucleo_ia/configuracion_maestra`;

    try {
        const res = await fetch(url);
        const data = await res.json();

        if (data.fields && data.fields.codigo_activo) {
            const codigoNube = data.fields.codigo_activo.stringValue;
            // Solo actualiza si hay contenido para evitar borrar el archivo local
            if (codigoNube.length > 10) {
                fs.writeFileSync(RUTA_LOCAL, codigoNube);
                console.log("✅ Código actualizado desde el servidor nube exitosamente.");
            }
        }
    } catch (e) {
        console.log("❌ Error de sincronización:", e.message);
    }
}
sincronizar();
console.log('🚀 PLAN MAESTRO ACTIVADO: Nodo Madrid-Oeste en línea');
