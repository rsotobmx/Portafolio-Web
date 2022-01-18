from ast import Global
import os
import signal
import subprocess
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Resource, Api
import time
app = Flask(__name__)


app.config.from_object(__name__)
CORS(app,resources={r"/*":{'origins':'*'}})
#CORS(app,
#    resources={r"/*":{'origins':'http://localhost:8080',
#                         "allow_headers":"Access-Control-Allow-Origin"}})

processes=[]




@app.route('/mensaje',methods=['GET','POST'])
def Estrategia():
    
    if request.method == "GET":
        p1 = subprocess.Popen(["python",'strategy.py'])
        #estrategia trabajando
        processes.append(p1)
        print("trabajando")
        print(p1.pid)
        print(processes)
        
        
            
        return "Trabajando"
    else:
        print(processes[-1].terminate())
        print(processes[-1].pid)
        print("stop a esa mierdaa")
        for process in processes:
            process.terminate()
        return "stop"
        

        
 

if __name__ == "__main__":
    app.run(debug=True)
    




