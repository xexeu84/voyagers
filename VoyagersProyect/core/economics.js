// Sistema Contable Voyagers v1.0
let billetera = {
    saldoPendiente: 0.00,
    saldoDisponible: 0.00,
    historial: []
};

function abonarPago(monto) {
    billetera.saldoPendiente += monto;
    console.log('Pago en custodia: ' + monto + '€');
}

function liberarPago(monto) {
    if(billetera.saldoPendiente >= monto) {
        billetera.saldoPendiente -= monto;
        billetera.saldoDisponible += monto;
        billetera.historial.push({fecha: new Date(), monto: monto, tipo: 'CRÉDITO'});
    }
}
