import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

# --- ⚙️ Configuration du port en tout premier ---
PORT = int(os.environ.get("PORT", 10000))  # Render donne automatiquement une variable d’environnement PORT
HOST = "0.0.0.0"

# --- 🚀 Initialisation de Flask ---
app = Flask(__name__)

# --- 📂 Configuration des uploads ---
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# --- 🌐 Routes principales ---

@app.route("/")
def login():
    """Page de connexion"""
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    """Page principale du tableau de bord"""
    return render_template("dashboard.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    """Upload d’un fichier et redirection"""
    if "file" not in request.files:
        return "Aucun fichier envoyé", 400

    file = request.files["file"]
    if file.filename == "":
        return "Nom de fichier vide", 400

    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)
        return render_template("upload_success.html", filename=filename)

    return redirect(url_for("dashboard"))

# --- 🚀 Lancement de l’app ---
if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)
