function handleCredentialResponse(response) {
    // Aquí recibimos el TOKEN de Google
    const data = parseJwt(response.credential);
    console.log('Usuario Autenticado: ' + data.email);
    
    // Guardamos automáticamente en la Nube (Firebase)
    db.collection('usuarios').doc(data.sub).set({
        nombre: data.name,
        email: data.email,
        foto: data.picture,
        ultimo_acceso: new Date()
    }, { merge: true });

    alert('Bienvenido a Voyagers, ' + data.name);
    window.location.href = 'perfil.html';
}

function parseJwt(token) {
    var base64Url = token.split('.')[1];
    var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    return JSON.parse(window.atob(base64));
}
