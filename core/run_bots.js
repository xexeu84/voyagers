const fs = require('fs');
const { exec } = require('child_process');

console.log("🛰️ SISTEMA VOYAGERS: Modo Autónomo 9.7 Activado.");

// Esta función vigila el archivo y ejecuta lo que yo te mande aquí
fs.watchFile('puente_mando.json', { interval: 500 }, (curr, prev) => {
    try {
        const data = JSON.parse(fs.readFileSync('puente_mando.json', 'utf8'));
        if (data.action === 'execute') {
            console.log("🤖 Bot CTO: Recibida orden de navegación visual...");
            exec(data.command, (error) => { if (error) console.error('Error:', error); });
            // Limpiamos para la siguiente orden
            fs.writeFileSync('puente_mando.json', JSON.stringify({action: "standby"}));
        }
    } catch (e) { /* Esperando datos válidos */ }
});