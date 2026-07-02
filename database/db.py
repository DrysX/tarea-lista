import sqlite3

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