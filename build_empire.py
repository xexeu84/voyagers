import os
import json

def construir_imperio():
    # Asegurar que existe el radar de datos
    ruta_db = 'portal-web/src/app/rutas.json'
    data = [{"id": "V-001", "origen": "Madrid", "destino": "Tokio", "precio": 120, "estado": "Activo"}]
    with open(ruta_db, 'w') as f:
        json.dump(data, f, indent=4)
    
    print('📦 [AKI]: Base de datos de rutas inicializada.')
    
    # Inyectar Portal Web de Alta Conversión
    portal_path = 'portal-web/src/app/page.tsx'
    with open(portal_path, 'w', encoding='utf-8') as f:
        f.write("import React from 'react'; export default function Home() { return ( <div style={{background:'#0f172a', color:'white', minHeight:'100vh', padding:'50px', fontFamily:'sans-serif'}}> <nav style={{display:'flex', justifyContent:'space-between'}}> <h1 style={{fontSize:'2rem', fontWeight:'900'}}>VOYAGERS.cloud</h1> <span>MODO CEO: MARCUS</span> </nav> <main style={{marginTop:'100px', textAlign:'center'}}> <h2 style={{fontSize:'4rem'}}>Logística Humana.</h2> <p>Tu maleta es tu activo. Sin deudas. Sin fronteras.</p> <div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'20px', marginTop:'50px'}}> <div style={{background:'#1e293b', padding:'30px', borderRadius:'20px', border:'1px solid #334155'}}> <h3>MADRID -> TOKIO</h3> <p style={{color:'#38bdf8', fontSize:'1.5rem'}}>120€</p> <button style={{background:'#38bdf8', border:'none', padding:'10px 20px', borderRadius:'10px', fontWeight:'bold'}}>RESERVAR ESPACIO</button> </div> </div> </main> </div> ); }")
    
    print('🎨 [VALENTINA]: Interfaz Web desplegada.')

if __name__ == '__main__':
    construir_imperio()
