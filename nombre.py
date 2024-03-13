from flask import Flask 

app = Flask(__name__)

@app.route("/agua/<name>")
def hello_word(name):
   return f'<center><h1>Mi nombres : {name}</h1></center>'

if __name__ == "__main__":
   app.run(debug=True)