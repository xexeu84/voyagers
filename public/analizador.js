const { execSync } = require('child_process');

function verificarRecursos() {
    try {
        // Leer estado de batería
        const bateriaRaw = execSync('termux-battery-status').toString();
        const bateria = JSON.parse(bateriaRaw);
        
        // Leer estado de red
        const redRaw = execSync('termux-telephony-deviceinfo').toString();
        const red = JSON.parse(redRaw);

        console.log(`🔋 Batería: ${bateria.percentage}% | ⚡ Estado: ${bateria.status}`);

        if (bateria.percentage < 15 && bateria.status !== "PLUGGED_AC") {
            console.log("⚠️ ALERTA: Batería baja. Modo de ahorro activado.");
            // Aquí podríamos limitar funciones pesadas
        }

        return { bateria: bateria.percentage, red: red.data_state };
    } catch (e) {
        console.log("📡 Sensores: Iniciando en modo estándar (API no detectada).");
        return null;
    }
}

// ... (Código previo de captura de datos)

try {
    const dataIA = await resIA.json();
    const textoRespuesta = dataIA.candidates[0].content.parts[0].text;
    
    // 🛡️ FILTRO DE INTEGRIDAD: Validamos si es un JSON válido
    let veredicto;
    try {
        veredicto = JSON.parse(textoRespuesta);
    } catch (e) {
        throw new Error("Respuesta de IA con formato inválido (No es JSON)");
    }

    // 🛡️ FILTRO DE CONTENIDO: Validamos campos críticos
    if (!veredicto.estado || !veredicto.riesgo || veredicto.estado === "N/A") {
        throw new Error("Datos incompletos: La IA no generó un veredicto válido");
    }

    // Si pasa los filtros, enviamos a Firestore
    const urlDB = `https://firestore.googleapis.com/v1/projects/gen-lang-client-0559117850/databases/(default)/documents/analisis`;
    // ... (Tu código de fetch a Firestore aquí)
    
    console.log("✅ Datos validados y sincronizados con éxito.");

} catch (error) {
    console.log(`⚠️ BLOQUEO DE SEGURIDAD: ${error.message}`);
    // Guardamos el fallo en la Caja Negra de forma autónoma
    guardarLog(error, "Filtro de Integridad / Envío Cloud");
}
