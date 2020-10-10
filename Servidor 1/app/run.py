from flask import Flask, request, jsonify
from bson.json_util import dumps, loads
import requests

app = Flask(__name__)
pServidorA = 'http://34.123.224.145:5000/'
pServidorB = 'http://35.226.94.227:5000/'

@app.route('/postear',methods=['POST'])
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
