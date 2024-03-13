from flask import Flask

app = Flask(__name__)

@app.route('/suma/<int:num1>,<int:num2>')
@app.route('/suma/<int:num1>,<int:num2>,<int:num3>')
def suma(num1, num2, num3=None):
    if num3 is None:
        resultado = num1 + num2
        return f'<center><h1>{num1} + {num2} = {resultado}</h1></center>'
    else:
        resultado = num1 + num2 + num3
        return f'<center><h1>{num1} + {num2} + {num3} = {resultado}</h1></center>'

@app.route('/resta/<int:num1>,<int:num2>')
@app.route('/resta/<int:num1>,<int:num2>,<int:num3>')
def resta(num1, num2, num3=None):
    if num3 is None:
        resultado = num1 - num2
        return f'<center><h1>{num1} - {num2} = {resultado}</h1></center>'
    else:
        resultado = num1 - num2 - num3
        return f'<center><h1>{num1} - {num2} - {num3} = {resultado}</h1></center>'

@app.route('/division/<int:num1>,<int:num2>')
def division(num1, num2):
    if num2 != 0:
        resultado = num1 / num2
        return f'<center><h1>{num1} / {num2} = {resultado}</h1></center>'
    else:
        return '<center><h1>Error: No se puede dividir entre cero.</h1></center>'

@app.route('/')
def saludo():
    return '<center><h1>Calculadora ._.    ;)</h1></center>'

if __name__ == '__main__':
    app.run(debug=True)
