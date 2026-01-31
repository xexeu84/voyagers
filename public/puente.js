const { exec } = require('child_process');
const fs = require('fs');

console.log('?? PUENTE VOYAGERS: Escuchando órdenes de los bots...');

// Crear el archivo de órdenes si no existe
if (!fs.existsSync('ordenes.txt')) fs.writeFileSync('ordenes.txt', '');

fs.watchFile('ordenes.txt', (curr, prev) => {
    const orden = fs.readFileSync('ordenes.txt', 'utf8').trim();
    if (orden) {
        console.log('?? Ejecutando: ' + orden);
        exec(orden, (err, stdout, stderr) => {
            if (stdout) console.log(stdout);
            if (stderr) console.error(stderr);
            fs.writeFileSync('ordenes.txt', ''); // Limpiar tras ejecutar
        });
    }
});
