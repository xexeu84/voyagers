self.addEventListener('install', (e) => { console.log('Voyagers PWA Instalada'); });
self.addEventListener('fetch', (e) => { e.respondWith(fetch(e.request)); });
