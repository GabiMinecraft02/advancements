import os
from flask import Flask, render_template

# --- Configuration du port ---
port = int(os.environ.get("PORT", 10000))

app = Flask(__name__)

# --- Routes principales ---

@app.route("/")
def home():
    return "<h1>Bienvenue sur le site Advancements !</h1><p>Tout fonctionne 🎉</p>"

# --- Lancement de l'app ---
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)
