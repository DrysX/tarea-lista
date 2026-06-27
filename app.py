import flask as fk
from flask import Flask

app = Flask(__name__)

tareas = []

@app.route("/", methods=["GET", "POST"])
def home():
    if fk.request.method == "POST":
        tarea = fk.request.form["tarea"].strip()

        if tarea:
            tareas.append(tarea)

    return fk.render_template(
        "index.html",
        tareas=tareas
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )