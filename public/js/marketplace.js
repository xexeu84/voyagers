const rutasActivas = [
    { origen: "Madrid", destino: "México DF", espacio: "12kg", precio: "45€", tipo: "Viajero" },
    { origen: "Barcelona", destino: "París", espacio: "2m3", precio: "120€", tipo: "Transportista" },
    { origen: "Buenos Aires", destino: "Madrid", espacio: "8kg", precio: "30€", tipo: "Viajero" }
];

function renderRutas() {
    const container = document.getElementById('market-grid');
    if (!container) return;
    container.innerHTML = ""; // Limpiar antes de cargar
    rutasActivas.forEach(ruta => {
        container.innerHTML += `
            <div style='border:1px solid #333; padding:15px; border-radius:10px; background:#111; margin:10px;'>
                <h4 style='color:#00ffff;'>${ruta.origen} ✈️ ${ruta.destino}</h4>
                <p style='color:#ccc;'>Espacio: ${ruta.espacio} | <b>Precio: ${ruta.precio}</b></p>
                <span style='font-size:10px; background:#333; padding:2px 5px;'>${ruta.tipo}</span>
                <button onclick='alert("Iniciando KYC...")' style='display:block; width:100%; margin-top:10px; background:#00ffff; color:#000; border:none; padding:5px; cursor:pointer;'>Reservar</button>
            </div>`;
    });
}
document.addEventListener('DOMContentLoaded', renderRutas);
