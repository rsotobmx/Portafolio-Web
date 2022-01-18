import subprocess
from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import signal
app = Flask(__name__)

app.config.from_object(__name__)
CORS(app,resources={r"/*":{'origins':'*'}})
#CORS(app,
#    resources={r"/*":{'origins':'http://localhost:8080',
#                         "allow_headers":"Access-Control-Allow-Origin"}})

@app.route('/',methods=['GET'])
def greetings():
    return("Hello, robert")

@app.route('/mensaje',methods=['GET','POST'])
def mensaje():
    
    p1=None  
    if request.method == "GET":
        p1 = subprocess.Popen(["python",'strategy.py'])
        #estrategia trabajando
        print("trabajando")
        print(p1)
        #p1.terminate()
        print(p1)
        
        
        return "p1 "
    else:
        p1 = subprocess.Popen(["python",'strategy.py'])
        print(p1)
        p1.terminate()
        print("Stopp")
        return "stop"
        
    






if __name__ == "__main__":
    app.run(debug=True)
    




