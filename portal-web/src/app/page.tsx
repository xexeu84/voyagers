
import React from 'react';

export default function Home() {
  return (
    <div style={{background:'#020617', color:'#f1f5f9', minHeight:'100vh', fontFamily:'sans-serif'}}>
      <nav style={{padding:'20px 50px', display:'flex', justifyContent:'space-between', alignItems:'center', background:'#0f172a', borderBottom:'1px solid #1e293b'}}>
        <h1 style={{color:'#38bdf8', fontWeight:'900', fontSize:'1.5rem'}}>VOYAGERS<span style={{color:'#fff'}}>.cloud</span></h1>
        <button style={{background:'#38bdf8', color:'#020617', padding:'10px 20px', borderRadius:'12px', fontWeight:'bold', border:'none', cursor:'pointer'}}>PUBLICAR VIAJE</button>
      </nav>
      <header style={{textAlign:'center', padding:'60px 20px'}}>
        <h2 style={{fontSize:'3rem', fontWeight:'900', marginBottom:'10px'}}>Logística Descentralizada.</h2>
        <p style={{color:'#94a3b8'}}>Tu maleta es el motor de la red. Seguro. Directo. Sin Deudas.</p>
      </header>
      <div style={{maxWidth:'1000px', margin:'0 auto', display:'grid', gridTemplateColumns:'repeat(auto-fit, minmax(300px, 1fr))', gap:'25px', padding:'20px'}}>
        {[1, 2].map(i => (
          <div key={i} style={{background:'#0f172a', padding:'25px', borderRadius:'20px', border:'1px solid #1e293b'}}>
            <div style={{display:'flex', justifyContent:'space-between', marginBottom:'15px'}}>
              <span style={{background:'#0ea5e9', color:'white', padding:'4px 12px', borderRadius:'15px', fontSize:'0.7rem', fontWeight:'bold'}}>VERIFICADO</span>
              <span style={{color:'#fbbf24'}}>★★★★★</span>
            </div>
            <h3 style={{fontSize:'1.4rem', margin:'5px 0'}}>Madrid → Londres</h3>
            <p style={{color:'#64748b', fontSize:'0.9rem'}}>Transportista: Alex G. • Maleta 10kg</p>
            <div style={{marginTop:'20px', display:'flex', justifyContent:'space-between', alignItems:'center'}}>
              <span style={{fontSize:'1.8rem', fontWeight:'900'}}>45€</span>
              <button style={{background:'#f8fafc', color:'#020617', padding:'10px 20px', borderRadius:'10px', fontWeight:'bold', border:'none'}}>RESERVAR</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
