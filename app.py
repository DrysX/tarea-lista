from flask import Flask
from database.db import crear_base_datos
from routes.tareas import tareas_bp

app = Flask(__name__)
app.register_blueprint(tareas_bp)

crear_base_datos()


if __name__ == "__main__":
    app.run(debug=True)