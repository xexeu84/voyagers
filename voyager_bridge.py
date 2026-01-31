import json, requests, os

class VoyagerBridge:
    def __init__(self):
        self.cloud_url = "https://voyagers-cloud-production.up.railway.app/api/status"
        self.repo_path = "routes_database.json"

    def comunicar_hallazgo(self, bot_name, data):
        print(f"[{bot_name}] Enviando datos al puente cloud...")
        # Los bots ahora se hablan a través de estados en el JSON compartido
        hallazgo = {"bot": bot_name, "data": data, "timestamp": "2026-01-31"}
        # Lukas se encarga de que esto llegue a la web
        return hallazgo
