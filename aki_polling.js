
const axios = require("axios");
const fs = require("fs");
const token = "8300141763:AAGDOU2I31OtHUD0d-Sb5_eFGBIC3DmD-K0";
let lastUpdateId = 0;

async function saveToDatabase(lead) {
    const fileName = "leads.json";
    let database = [];
    if (fs.existsSync(fileName)) {
        database = JSON.parse(fs.readFileSync(fileName));
    }
    database.push({ date: new Date().toISOString(), ...lead });
    fs.writeFileSync(fileName, JSON.stringify(database, null, 2));
    console.log(">>> [BBDD] Oportunidad guardada en el registro de Voyagers.");
}

async function processIntelligence(chatId, text, origin) {
    const lowerText = text.toLowerCase();
    const keywords = ["maleta", "envío", "paquete", "viajo", "vuelo", "espacio", "kilos"];
    const found = keywords.filter(k => lowerText.includes(k));
    
    if (found.length > 0) {
        const lead = { origin, text, keywords: found };
        await saveToDatabase(lead);
        
        if (lowerText.includes("kai")) {
            await axios.post(`https://api.telegram.org/bot${token}/sendMessage`, {
                chat_id: chatId,
                text: "Entendido, Director. He registrado esta ruta en la base de datos de Voyagers. El equipo está analizando la rentabilidad."
            });
        }
    }
}

async function poll() {
    try {
        const res = await axios.get(`https://api.telegram.org/bot${token}/getUpdates?offset=${lastUpdateId + 1}`);
        for (const update of res.data.result) {
            lastUpdateId = update.update_id;
            const msg = update.message || update.channel_post;
            if (msg && msg.text) {
                await processIntelligence(msg.chat.id, msg.text, msg.chat.title || "Privado");
            }
        }
    } catch (e) { }
    setTimeout(poll, 1000);
}

console.log(">>> KAI AGENT V2: CONEXIÓN CON BBDD GITHUB ESTABLECIDA <<<");
poll();
