const admin = require('firebase-admin');
// Este archivo conecta tu lógica local con los servidores de Google
admin.initializeApp({
  credential: admin.credential.applicationDefault(),
  databaseURL: 'https://voyagers-global-node.firebaseio.com'
});
const db = admin.firestore();
console.log('--- CONEXIÓN CLOUD VOYAGERS: ESTABLECIDA ---');
