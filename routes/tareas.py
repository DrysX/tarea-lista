import flask as fk
from flask import Blueprint, render_template, redirect, url_for
from database.db import obtener_tareas, agregar_tarea, eliminar_tarea, completar_tarea

tareas_bp = Blueprint("tareas", __name__)

@tareas_bp.route("/", methods=["GET", "POST"])
def home():
    if fk.request.method == "POST":
        tarea = fk.request.form["tarea"].strip()

        if tarea:
            agregar_tarea(tarea)
        
        return redirect(url_for("tareas.home"))
    
    tareas = obtener_tareas()

    return render_template(
        "index.html",
        tareas=tareas
    )

@tareas_bp.route("/completar/<int:id_tarea>", methods=["POST"])
def completar(id_tarea):
    completar_tarea(id_tarea)

    return redirect(url_for("tareas.home"))

@tareas_bp.route("/eliminar/<int:id_tarea>", methods=["POST"])
def eliminar(id_tarea):
    eliminar_tarea(id_tarea)

    return redirect(url_for("tareas.home"))
