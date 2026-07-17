from flask import Flask, render_template, request
import os
from rag.pipeline import RAGPipeline

app = Flask(__name__)

UPLOAD_FOLDER = "Documents"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

pipeline = RAGPipeline()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    
    if "pdf" not in request.files:
        return "No File Uploaded."
    
    file = request.files["pdf"]

    if file.filename == "":
        return "No File Selected."
    
    filepath = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    file.save(filepath)

    pipeline.build_index(filepath)

    return "PDF Indexed Successfully!!"


@app.route("/ask", methods=["POST"])
def ask():

    if pipeline.index is None:
        return render_template(
            "index.html",
            answer = "Please Upload A Pdf First!!!"
        )


    question = request.form["question"]

    answer = pipeline.ask(question)

    return render_template(
        "index.html",
        answer = answer
    )



if __name__ == "__main__":
    app.run(debug=True)

