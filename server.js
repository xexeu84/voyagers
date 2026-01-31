
const express = require("express");
const axios = require("axios");
const app = express();
app.use(express.json());
const token = "8300141763:AAGDOU2I31OtHUD0d-Sb5_eFGBIC3DmD-K0";

app.post("/apiTelegram", async (req, res) => {
    console.log(" Mensaje recibido de Telegram...");
    if (req.body.message) {
        const chatId = req.body.message.chat.id;
        try {
            await axios.post(`https://api.telegram.org/bot${token}/sendMessage`, {
                chat_id: chatId,
                text: "¡CONSOLA ACTIVA! Aki reportándose desde el núcleo local. Director Marcus, el bloqueo de Google ha sido superado."
            });
            console.log(" Respuesta enviada con éxito.");
        } catch (e) { console.log(" Error al responder."); }
    }
    res.send("OK");
});
app.listen(3000, () => console.log(">>> CONSOLA DE AKI OPERATIVA EN PUERTO 3000 <<<"));
