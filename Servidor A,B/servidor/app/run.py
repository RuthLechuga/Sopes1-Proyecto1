from flask import Flask, request, jsonify
from flask_pymongo import  PyMongo

from bson.json_util import dumps

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
        oracion.save({"autor":autor, "nota": nota})
        return "Ingreso Exitoso"

@app.route('/datos_servidor',methods=['GET'])
def obtener():
     f = open("/proc/RAM", "r")
     datos = f.read()
     f.close()
     return datos
#    oracion = mongo.db.oracion
#    cantidad_datos = oracion.count()
#    return jsonify({"cantidad_datos":cantidad_datos})

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
