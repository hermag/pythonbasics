from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1> Index Page </h1>"

@app.route('/hello')
def hello():
    return '<h2> Hello, World </h2>'
    
if __name__=="__main__":
    app.run(debug=True,port=8080)