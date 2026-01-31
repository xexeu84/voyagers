const { execSync } = require('child_process');

async function runHighFrequency() {
    console.log("[AKI]: Iniciando Motor de Alta Frecuencia (15s)...");
    
    // El bot se mantiene vivo durante la ejecución del job
    for (let i = 0; i < 120; i++) { // Ejecuta durante ~30 minutos por sesión
        console.log(`[LATIDO]: Ciclo ${i+1} iniciado...`);
        
        try {
            // 1. Valentina busca actualizaciones de diseño
            // 2. KAI rastrea subvenciones y registros
            // 3. Lukas verifica seguridad y deudas
            execSync('node core/listener.js'); 
            
            console.log("[OK]: Tareas completadas. Durmiendo 15 segundos...");
        } catch (error) {
            console.error("[ERROR]: Fallo en ciclo, reintentando...");
        }

        // Pausa real de 15 segundos
        await new Promise(resolve => setTimeout(resolve, 15000));
    }
}
runHighFrequency();
