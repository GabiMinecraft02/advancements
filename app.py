from flask import Flask, render_template
import os

app = Flask(__name__)

# Dossier où sont stockées les images et textes
UPLOAD_FOLDER = os.path.join("static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def advancements():
    # Liste des images
    images = [f for f in os.listdir(UPLOAD_FOLDER)
              if f.lower().endswith((".jpg", ".png", ".jpeg", ".gif"))]

    # Texte
    texts = []
    text_file = os.path.join(UPLOAD_FOLDER, "text.txt")
    if os.path.exists(text_file):
        with open(text_file, "r", encoding="utf-8") as f:
            texts = f.readlines()

    return render_template("advancements.html", images=images, texts=texts)

if __name__ == "__main__":
    app.run(debug=True, port=5002)  # port spécifique au 3ème site
