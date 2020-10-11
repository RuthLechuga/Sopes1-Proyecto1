from flask import Flask, request, jsonify
from flask_pymongo import  PyMongo
from bson.json_util import dumps, loads
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MONGO_DBNAME'] = 'oraciones'
app.config['MONGO_URI'] = 'mongodb://mongo:27017/oraciones'

mongo = PyMongo(app)

@app.route('/',methods=['GET','POST'])
@cross_origin()
def index():
    if request.method == 'GET':
        oracion = mongo.db.oracion
        resultados = oracion.find()
        return dumps(resultados)

    if request.method == 'POST':
        print(request.json)
        content = json.loads(str(request.json))
        oracion = mongo.db.oracion
        oracion.save(content)
        return 'Ingreso Exitoso'

@app.route('/datos_servidor',methods=['GET'])
@cross_origin()
def obtenerDatos():
    f = open('/proc/RAM', 'r')
    datos = loads(f.read())
    porcentajeRAM = (datos['Free']/datos['Total'])*100
    f.close()
    
    f = open('/proc/CPU', 'r')
    porcentajeCPU = f.read()
    f.close()


    oracion = mongo.db.oracion
    cantidad_datos = oracion.count()
    return jsonify({'cantidadDatos':cantidad_datos, 'RAM':porcentajeRAM, 'CPU': porcentajeCPU})

@app.route('/getPorcentajes',methods=['GET'])
@cross_origin()
def obtenerPorcentajes():
    f = open('/proc/RAM', 'r')
    datos = loads(f.read())
    porcentajeRAM = (datos['Free']/datos['Total'])*100
    f.close()

    f = open('/proc/CPU', 'r')
    porcentajeCPU = f.read()
    f.close()
     
    return jsonify({'RAM':porcentajeRAM, 'CPU': porcentajeCPU})

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
