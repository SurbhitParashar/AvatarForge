import os
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from avatar_logic import generate_avatar
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["OUTPUT_FOLDER"] = OUTPUT_FOLDER


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            if "file" not in request.files:
                return render_template("index.html", error="No file uploaded")

            file = request.files["file"]

            if file.filename == "":
                return render_template("index.html", error="No file selected")

            filename = secure_filename(file.filename)
            input_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)

            file.save(input_path)

            output_filename = "avatar_" + filename
            output_path = os.path.join(app.config["OUTPUT_FOLDER"], output_filename)

            # 🔥 Run your pipeline
            generate_avatar(input_path, output_path)

            return render_template("index.html", result=output_filename)

        except Exception as e:
            return render_template("index.html", error=str(e))

    return render_template("index.html")


@app.route("/download/<filename>")
def download_file(filename):
    path = os.path.join(app.config["OUTPUT_FOLDER"], filename)
    return send_file(path, as_attachment=True)

from flask import send_from_directory

@app.route('/outputs/<filename>')
def serve_output(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)