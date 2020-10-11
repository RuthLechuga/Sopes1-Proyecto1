from flask import Flask, request, jsonify
from bson.json_util import dumps, loads
import requests
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MONGO_DBNAME'] = 'oraciones'
app.config['MONGO_URI'] = 'mongodb://mongo:27017/oraciones'

pServidorA = 'http://34.123.224.145:5000/'
pServidorB = 'http://35.226.94.227:5000/'

@app.route('/postear',methods=['POST'])
@cross_origin()
def index():
    if request.method == 'POST':
        content = request.json
        autor = content['autor']
        nota = content['nota']
        datos = {'autor':autor, 'nota': nota}
        datosServidorA = loads(requests.get(pServidorA+ 'datos_servidor').content)
        datosServidorB = loads(requests.get(pServidorB+ 'datos_servidor').content)

        if datosServidorA['cantidadDatos'] < datosServidorB['cantidadDatos']:
            return requests.post(pServidorA, json = datos).content
        
        if datosServidorA['cantidadDatos'] > datosServidorB['cantidadDatos']:
            return requests.post(pServidorB, json = datos).content
        
        if datosServidorA['RAM'] < datosServidorB['RAM']:
            return requests.post(pServidorA, json = datos).content
        
        if datosServidorA['RAM'] > datosServidorB['RAM']:
            return requests.post(pServidorB, json = datos).content
        
        if datosServidorA['CPU'] < datosServidorB['CPU']:
            return requests.post(pServidorA, json = datos).content
        
        if datosServidorA['CPU'] > datosServidorB['CPU']:
            return requests.post(pServidorB, json = datos).content
        
        return requests.post(pServidorA, json = datos).content
        
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
