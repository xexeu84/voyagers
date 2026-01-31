// Base de Datos de Inventario - Nodo Madrid-Oeste
const inventarioLocal = [
    { id: 'PKG-001', contenido: 'Documentos urgentes', peso: '0.5kg', destino: 'Londres', estado: 'En Almacén' },
    { id: 'PKG-002', contenido: 'Repuestos electrónicos', peso: '2.1kg', destino: 'Barcelona', estado: 'Pendiente Recogida' },
    { id: 'PKG-003', contenido: 'Libros texto', peso: '4.0kg', destino: 'París', estado: 'En Tránsito' }
];

function listarInventario() {
    return inventarioLocal.map(item => 
        `<div style='border-bottom:1px solid #555; padding:10px;'>
            <span style='color:#00d1b2;'>[${item.id}]</span> ${item.contenido} - <b>${item.peso}</b><br>
            <small>Destino: ${item.destino} | Estado: ${item.estado}</small>
        </div>`
    ).join('');
}
