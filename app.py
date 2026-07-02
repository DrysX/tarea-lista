import flask as fk
from flask import Flask,render_template, redirect, url_for

import sqlite3

app = Flask(__name__)

DATABASE = "instance/tareas.db"
def crear_base_datos():
    conexion = sqlite3.connect(DATABASE)
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            completada INTEGER NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()

def obtener_tareas():
    conexion = sqlite3.connect(DATABASE)

    conexion.row_factory = sqlite3.Row

    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tareas")
    tareas = cursor.fetchall()
    conexion.close()
    return tareas

def agregar_tarea(titulo):
    conexion = sqlite3.connect(DATABASE)
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO tareas (titulo, completada) VALUES (?, ?)", (titulo, 0))
    conexion.commit()
    conexion.close()

def eliminar_tarea(id_tarea):
    conexion = sqlite3.connect(DATABASE)
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM tareas WHERE id = ?", (id_tarea,))
    conexion.commit()
    conexion.close()

def completar_tarea(id_tarea):
    conexion = sqlite3.connect(DATABASE)
    cursor = conexion.cursor()
    cursor.execute("UPDATE tareas SET completada = NOT completada WHERE id = ?", (id_tarea,))
    conexion.commit()
    conexion.close()

@app.route("/", methods=["GET", "POST"])
def home():
    if fk.request.method == "POST":
        tarea = fk.request.form["tarea"].strip()

        if tarea:
            agregar_tarea(tarea)
        
        return redirect(url_for("home"))
    
    tareas = obtener_tareas()

    return render_template(
        "index.html",
        tareas=tareas
    )

@app.route("/completar/<int:id_tarea>", methods=["POST"])
def completar(id_tarea):
    completar_tarea(id_tarea)

    return redirect(url_for("home"))

@app.route("/eliminar/<int:id_tarea>", methods=["POST"])
def eliminar(id_tarea):
    eliminar_tarea(id_tarea)

    return redirect(url_for("home"))


crear_base_datos()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )