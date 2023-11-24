from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Endpoint para obtener todos los propietarios
@app.route('/propietarios', methods=['GET'])
def obtener_propietarios():
    response = requests.get("https://baserestapi.onrender.com/propietario")
    return jsonify(response.json())

# Endpoint para obtener un propietario específico por ID
@app.route('/propietarios/<int:id>', methods=['GET'])
def obtener_propietario(id):
    response = requests.get(f"https://baserestapi.onrender.com/propietario/{id}")
    return jsonify(response.json())

# Endpoint para obtener todos los vehículos
@app.route('/vehiculos', methods=['GET'])
def obtener_vehiculos():
    response = requests.get("https://baserestapi.onrender.com/vehiculo")
    return jsonify(response.json())

# Endpoint para obtener un vehículo específico por ID
@app.route('/vehiculos/<int:id>', methods=['GET'])
def obtener_vehiculo(id):
    response = requests.get(f"https://baserestapi.onrender.com/vehiculo/{id}")
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
