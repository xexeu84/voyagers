const stripe = require('stripe')('TU_CLAVE_SECRETA_STRIPE');

async function crearIntentoDePago(monto, viajeId) {
    const paymentIntent = await stripe.paymentIntents.create({
        amount: monto * 100, // Stripe trabaja en céntimos
        currency: 'eur',
        metadata: { viaje_id: viajeId },
        automatic_payment_methods: { enabled: true },
    });
    console.log('Intento de pago creado: ' + paymentIntent.id);
    return paymentIntent.client_secret;
}
