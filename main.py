import configparser
import sys
import argparse
from flask import Flask, jsonify, request
from scipy.integrate import quad

app = Flask(__name__)
xt = 0
def f(x):
    return x**2-2**5

@app.route("/getRes", methods=["GET"])
def sh12354():
    global xt
    try:
        ans = {}
        res,error = quad(f, float(x), float(y))
        if xt == res:
            ans["name"] = config['DATA']['name']
            ans["lastname"] = config['DATA']['lastname']
            ans["rez"] = "OK, COOL"
        else:
            ans["name"] = config['DATA']['name']
            ans["lastname"] = config['DATA']['lastname']
            ans["rez"] = "NOT OK, TRY AGAI"
        return ans
    except Exception as e:
        return jsonify(message=f"NOT OK {e}"), 400

# @app.route("/getResInteg", methods=["GET"])
# def sh123():
#     try:
#         ans = {}
#         rez, error = quad(f, float(x), float(y))
# РЕЗУЛЬТАТ ИНТЕГРАЛА
#         ans["rez"] = rez
# ПОГРЕШНОСТЬ
#         ans["error"] = error
#         return ans
#     except Exception as e:
#         return jsonify(message=f"NOT OK {e}"), 400

@app.route("/postXT", methods=["POST"])
def sh12():
    global xt
    try:
        data = request.get_json()
        xt = data.get("rez")
        return jsonify(message=f"OK"), 400
    except Exception as e:
        return jsonify(message=f"NOT OK {e}"), 400

file_path = sys.argv[1]

try:
    config = configparser.ConfigParser()
    config.read(file_path)
    x = config['MATH']['x']
    y = config['MATH']['y']
    app.run(port=20000, debug=True)
except:
    print("Что-то не так с конфигурационным файлом")

    print("Something is wrong with the configuration file.")
