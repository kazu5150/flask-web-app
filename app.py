from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route("/")
def index():
    fuga = 123
    return render_template("index.html", hoge=fuga)


@app.route("/upload", methods=["POST"])
def upload():
    img_file = request.files["img_file"]
    print(img_file.filename)
    img_file.save(os.path.join("static", img_file.filename))
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
