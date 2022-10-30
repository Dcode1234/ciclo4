from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import pymongo
import certifi

ca = certifi.where()

client = pymongo.MongoClient("mongodb+srv://bdregistraduria:abcd123456789@cluster0.qfgmf.mongodb.net/bdregistraduria?retryWrites=true&w=majority",tlsCAFile=ca)

db = client.test
print(db)


from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorPartido import ControladorPartido

miControladorMesa=ControladorMesa()
miControladorPartido=ControladorPartido()


app=Flask(__name__)
cors = CORS(app)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)


#rutas mesas

@app.route("/mesas",methods=['GET'])
def getMesas():
    json=miControladorMesa.index()
    return jsonify(json)

@app.route("/mesas",methods=['POST'])
def crearMesa():
    data = request.get_json()
    json=miControladorMesa.create(data)
    return jsonify(json)

@app.route("/mesas/<string:mesa>",methods=['GET'])
def getMesa(mesa):
    json=miControladorMesa.show(mesa)
    return jsonify(json)

@app.route("/mesas/<string:mesa>",methods=['PUT'])
def modificarMesa(mesa):
    data = request.get_json()
    json=miControladorMesa.update(mesa,data)
    return jsonify(json)

@app.route("/mesas/<string:mesa>",methods=['DELETE'])
def eliminarEstudiante(mesa):
    json=miControladorMesa.delete(mesa)
    return jsonify(json)


#rutas partido

@app.route("/partidos",methods=['GET'])
def getPartidos():
    json=miControladorPartido.index()
    return jsonify(json)

@app.route("/partidos",methods=['POST'])
def crearPartido():
    data = request.get_json()
    json=miControladorPartido.create(data)
    return jsonify(json)

@app.route("/partidos/<string:id>",methods=['GET'])
def getPartido(id):
    json=miControladorPartido.show(id)
    return jsonify(json)

@app.route("/partidos/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json=miControladorPartido.update(id,data)
    return jsonify(json)

@app.route("/partidos/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)





if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])