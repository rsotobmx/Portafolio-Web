

import subprocess
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)


app.config.from_object(__name__)
CORS(app,resources={r"/*":{'origins':'*'}})
#CORS(app,
#    resources={r"/*":{'origins':'http://localhost:8080',
#                         "allow_headers":"Access-Control-Allow-Origin"}})

processes=[]


#Aqui es donde Se realiza La conexion con el frontend el cual se logra gracias al framework de python que se llama Flask

@app.route('/mensaje',methods=['GET','POST'])
def Estrategia():
    
    if request.method == "GET":
        p1 = subprocess.Popen(["python",'strategy.py'])
        #estrategia trabajando
        processes.append(p1)
        print("trabajando el bot")
        print(p1.pid)
        print(processes)
        
        
            
        return "Trabajando"
    else:
        print(processes[-1].terminate())
        print(processes[-1].pid)
        print("Se detuvo el bot")
        for process in processes:
            process.terminate()
        return "stop"
        

        
 

if __name__ == "__main__":
    app.run(debug=True)
    




