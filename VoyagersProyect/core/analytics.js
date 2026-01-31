// Analytics de Rutas Voyagers
const estadisticasRutas = [
    { ruta: 'Madrid-Londres', volumen: '85%', tendencia: 'SUBIENDO', beneficio_estimado: '1.240€' },
    { ruta: 'Madrid-Barcelona', volumen: '92%', tendencia: 'ESTABLE', beneficio_estimado: '850€' },
    { ruta: 'Madrid-París', volumen: '40%', tendencia: 'BAJANDO', beneficio_estimado: '310€' }
];

function renderDashboard() {
    return estadisticasRutas.map(r => 
        `<div style='background:#444; margin:10px 0; padding:10px; border-left:5px solid ${r.volumen > "80%" ? "#00ff00" : "#ffcc00"}'>
            <b>${r.ruta}</b> - Tráfico: ${r.volumen} | ${r.tendencia} 📈<br>
            <small>Beneficio Nodo: ${r.beneficio_estimado}</small>
        </div>`
    ).join('');
}
