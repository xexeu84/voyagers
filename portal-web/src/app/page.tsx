import React, { useEffect, useState } from 'react';

export default function Home() {
  // Evitar errores de extensiones externas (MetaMask) en el lado del cliente
  useEffect(() => {
    if (typeof window !== 'undefined') {
      window.addEventListener('unhandledrejection', (event) => {
        if (event.reason && event.reason.message && event.reason.message.includes('MetaMask')) {
          event.preventDefault();
        }
      });
    }
  }, []);

  return (
    <div style={{background:'#020617', color:'#f1f5f9', minHeight:'100vh', fontFamily:'sans-serif'}}>
      <nav style={{padding:'15px 40px', display:'flex', justifyContent:'space-between', alignItems:'center', background:'#0f172a', borderBottom:'1px solid #1e293b'}}>
        <h1 style={{color:'#38bdf8', fontWeight:'900', fontSize:'1.6rem', letterSpacing:'-1px'}}>VOYAGERS</h1>
        <div style={{display:'flex', gap:'15px'}}>
          <button style={{color:'#94a3b8', background:'none', border:'none', fontWeight:'600'}}>Mis Viajes</button>
          <button style={{background:'#38bdf8', color:'#020617', padding:'10px 22px', borderRadius:'10px', fontWeight:'800', border:'none'}}>PUBLICAR ESPACIO</button>
        </div>
      </nav>

      <main style={{padding:'40px'}}>
        <div style={{background:'#1e293b', padding:'20px', borderRadius:'15px', display:'flex', gap:'10px', maxWidth:'900px', margin:'0 auto 40px auto', border:'1px solid #334155'}}>
          <input placeholder="Origen" style={{flex:1, background:'#0f172a', border:'1px solid #334155', padding:'12px', borderRadius:'8px', color:'white'}} />
          <input placeholder="Destino" style={{flex:1, background:'#0f172a', border:'1px solid #334155', padding:'12px', borderRadius:'8px', color:'white'}} />
          <button style={{background:'#38bdf8', color:'#020617', padding:'0 25px', borderRadius:'8px', fontWeight:'bold'}}>BUSCAR</button>
        </div>

        <div style={{display:'grid', gridTemplateColumns:'2fr 1fr', gap:'30px', maxWidth:'1200px', margin:'0 auto'}}>
          <div>
            <h2 style={{marginBottom:'20px'}}>Viajes Disponibles</h2>
            <div style={{background:'#0f172a', padding:'20px', borderRadius:'16px', marginBottom:'15px', border:'1px solid #1e293b'}}>
              <div style={{display:'flex', justifyContent:'space-between'}}>
                <div>
                  <h3 style={{fontSize:'1.3rem'}}>Madrid → París</h3>
                  <p style={{color:'#64748b'}}>Salida: 02 Feb • Equipaje: 10kg máx.</p>
                </div>
                <div style={{textAlign:'right'}}>
                  <span style={{fontSize:'1.5rem', fontWeight:'900', color:'#38bdf8'}}>28€</span>
                  <p style={{fontSize:'0.8rem', color:'#4ade80'}}>● Disponible</p>
                </div>
              </div>
              <button style={{marginTop:'15px', width:'100%', background:'#f8fafc', color:'#020617', padding:'10px', borderRadius:'8px', fontWeight:'bold', border:'none'}}>RESERVAR ESPACIO</button>
            </div>
          </div>

          <div style={{background:'#0f172a', borderRadius:'16px', border:'1px solid #1e293b', height:'400px', display:'flex', flexDirection:'column'}}>
            <div style={{padding:'15px', borderBottom:'1px solid #1e293b', fontWeight:'bold'}}>Chat de Negociación</div>
            <div style={{flex:1, padding:'15px', fontSize:'0.9rem', color:'#64748b', textAlign:'center', marginTop:'50px'}}>
              Selecciona un viaje para iniciar un chat seguro.
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
