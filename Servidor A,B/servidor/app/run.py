from flask import Flask, request, jsonify
from flask_pymongo import  PyMongo
from bson.json_util import dumps, loads

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'oraciones'
app.config['MONGO_URI'] = 'mongodb://mongo:27017/oraciones'

mongo = PyMongo(app)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        oracion = mongo.db.oracion
        resultados = oracion.find()
        return dumps(resultados)

    if request.method == 'POST':
        content = request.json
        autor = content['autor']
        nota = content['nota']
        oracion = mongo.db.oracion
        oracion.save({'autor':autor, 'nota': nota})
        return 'Ingreso Exitoso'

@app.route('/datos_servidor',methods=['GET'])
def obtenerDatos():
     f = open('/proc/RAM', 'r')
     datos = loads(f.read())
     porcentajeRAM = (datos['Free']/datos['Total'])*100
     f.close()
     oracion = mongo.db.oracion
     cantidad_datos = oracion.count()
     return jsonify({'cantidadDatos':cantidad_datos, 'RAM':porcentajeRAM, 'CPU': 90})

@app.route('/getPorcentajes',methods=['GET'])
def obtenerPorcentajes():
     f = open('/proc/RAM', 'r')
     datos = loads(f.read())
     porcentajeRAM = (datos['Free']/datos['Total'])*100
     f.close()
     return jsonify({'RAM':porcentajeRAM, 'CPU': 90})

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
