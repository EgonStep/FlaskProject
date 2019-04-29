#Classe Flask 
from flask import Flask,render_template

#Cria-se uma instância de Flask (O parâmetro é o nome do módulo de aplicação)
app = Flask(__name__)

#Route Decorator: Define qual URL que ativará a função desejada.
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)

@app.route('/serie/<name>')
def show_serie_name(name):
    return 'Serie: ' + name

@app.route('/serie/<name>/<int:season>')
def show_serie_info(name,season):
    return 'Name: ' + name + '\nSeason: {0}'.format(season)

@app.route('/path/<path:subpath>')
def show_path(subpath):
    return subpath

