import flask as fk
from flask import Flask,render_template, redirect, url_for

app = Flask(__name__)

tareas = []

@app.route("/", methods=["GET", "POST"])
def home():
    if fk.request.method == "POST":
        tarea = fk.request.form["tarea"].strip()

        if tarea:
            tareas.append(
                {
                    "titulo": tarea,
                    "completada": False
                }
            )
        
        return redirect(url_for("home"))

    return render_template(
        "index.html",
        tareas=tareas
    )

@app.route("/completar/<int:id_tarea>", methods=["POST"])
def completar(id_tarea):
    if 0 <= id_tarea < len(tareas):
        tareas[id_tarea]["completada"] = not tareas[id_tarea]["completada"]
    return redirect(url_for("home"))

@app.route("/eliminar/<int:id_tarea>", methods=["POST"])
def eliminar(id_tarea):
    if 0 <= id_tarea < len(tareas):
        tareas.pop(id_tarea)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )