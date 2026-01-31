const fetch = require('node-fetch');

async function verHistorial() {
  const proyectoID = "gen-lang-client-0559117850";
  // Consultamos la colección "analisis" ordenando por fecha de creación
  const urlDB = `https://firestore.googleapis.com/v1/projects/${proyectoID}/databases/(default)/documents/analisis?pageSize=5`;

  console.log("📂 Conectando con Voyagers Cloud...");

  try {
    const res = await fetch(urlDB);
    const data = await res.json();

    if (data.documents && data.documents.length > 0) {
      console.log("\n📋 ÚLTIMOS REPORTES ENCONTRADOS:");
      data.documents.forEach((doc, index) => {
        const f = doc.fields;
        console.log(`------------------------------`);
        console.log(`📌 ID: ${doc.name.split('/').pop()}`);
        console.log(`📦 Producto: ${f.producto?.stringValue || 'Sin datos'}`);
        console.log(`⚠️ Riesgo: ${f.riesgo?.stringValue || 'N/A'}`);
        console.log(`✅ Estado: ${f.estado?.stringValue || 'N/A'}`);
        console.log(`📅 Fecha: ${new Date(doc.createTime).toLocaleString()}`);
      });
    } else {
      console.log("📭 La base de datos está vacía o el proyecto aún se está reiniciando.");
    }
  } catch (error) {
    console.log("❌ Error de red:", error.message);
  }
}

verHistorial();
