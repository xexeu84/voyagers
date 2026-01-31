const { execSync } = require('child_process');

function executeWithAutoSync(command) {
    try {
        console.log(`[EJECUTANDO]: ${command}`);
        execSync(command, { stdio: 'inherit' });
    } catch (error) {
        if (error.message.includes('rejected') || error.message.includes('failed to push')) {
            console.log("⚠️ [ALERTA LUKAS]: Conflicto detectado. Inyectando V-SYNC automáticamente...");
            try {
                // Protocolo V-SYNC forzado
                execSync('git pull origin main --rebase', { stdio: 'inherit' });
                execSync('git push origin main', { stdio: 'inherit' });
                console.log("✅ [LUKAS]: Sistema purgado y sincronizado.");
            } catch (syncError) {
                console.error("❌ [CRÍTICO]: Fallo en auto-sincronización. Reintentando en 15s...");
            }
        }
    }
}

// Bucle infinito de alta frecuencia
setInterval(() => {
    executeWithAutoSync('node core/listener.js');
}, 15000);
