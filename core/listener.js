const fs = require('fs');
const { execSync } = require('child_process');

// Aki lee las instrucciones que Marcus deja en el puente
const puente = JSON.parse(fs.readFileSync('./database/puente_mando.json', 'utf8'));

if (puente.instruccion_activa) {
    console.log(`[PUENTE]: Nueva instrucción de Marcus detectada: ${puente.comando}`);
    
    try {
        // Ejecución de la voluntad del Director
        const output = execSync(puente.comando).toString();
        
        // Reporte de éxito a Marcus
        puente.ultimo_log = output;
        puente.instruccion_activa = false; // Marcar como ejecutada
        fs.writeFileSync('./database/puente_mando.json', JSON.stringify(puente, null, 2));
        console.log("[PUENTE]: Ejecución completada y reportada.");
    } catch (error) {
        console.error("[ERROR]: Fallo en la ejecución autónoma:", error.message);
    }
}
