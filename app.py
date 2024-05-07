from flask import Flask, request
import json

from src import Core, PrBaseException


app = Flask(__name__)
core = Core()

@app.route("/register/set", methods=["POST"])
def set_register():
    data:dict[str,str] = json.loads(request.data)
    try:
        core.registers.set(data)
        response = "OK"
    
    except PrBaseException as e:
        response = e.message, e.status

    return response


@app.route("/register/read", methods=["GET"])
def read_register():
    data = core.registers.read
    return data



@app.route("/memory/set", methods=["POST"])
def set_memory():
    data = json.loads(request.data)
    try:
        core.memory.set(data["data"])
        response = "OK"
    except PrBaseException as e:
        response = e.message , e.status

    return response


@app.route("/memory/read", methods=["GET"])
def read_memory():
    data = core.memory.read
    res = {"data": data}
    return res


@app.route("/core/instruction", methods=["POST"])
def execute_instruction():  
    data: dict[str, list[str]] = json.loads(request.data) 
    core.execute_instruction(data["instructions"])
    return "OK"




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
