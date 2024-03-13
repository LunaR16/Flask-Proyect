from flask import flask 

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<center><h1>EL QUE ESTA LEYENDO ES UN MAMA GRANO</h1></center>'

@app.route("/home/<name>") # inicio
def home(name):
    return f'Estos es solo el principio {name}'

@app.route("/pg3")
def pg3():
        return "<center><h1> fuego, chispa, candela</h1></center>"

if __name__ == '__main__':
    app.run("Ports 5550, debug = True")

