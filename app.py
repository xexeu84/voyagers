from flask import Flask, jsonify
from core.routes import RouteManager

app = Flask(__name__)
manager = RouteManager()

@app.route('/')
def status():
    return jsonify({"status": "ONLINE", "project": "Voyagers", "cloud": "Active"})

if __name__ == "__main__":
    import os
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
