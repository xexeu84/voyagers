// Motor de Demanda Voyagers v1.0
const rutasCalientes = [
    { origen: 'Madrid (Barajas)', destino: 'Londres (LHR)', pagoKilo: 15.50, demanda: 'ALTA' },
    { origen: 'Madrid (Atocha)', destino: 'Barcelona (Sants)', pagoKilo: 8.00, demanda: 'MUY ALTA' },
    { origen: 'Madrid (Méndez Álvaro)', destino: 'Lisboa', pagoKilo: 12.00, demanda: 'MEDIA' }
];

function obtenerRutaTop() {
    return rutasCalientes.sort((a, b) => b.pagoKilo - a.pagoKilo)[0];
}
