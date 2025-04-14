from flask import Flask, render_template, redirect, url_for, request
from config import Config 
from flask_sqlalchemy import SQLAlchemy


app= Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

#importar las entidades
from models.ModelUsuario import ModelUsuario

@app.route('/about', methods = ['GET', 'POST'])
def about():
    if request.method == 'POST':
        print(request.form['floatingInput'])
        return render_template('layout.html')
    else: 
        usuario = ModelUsuario.consultarUsuario(db, "jcdd_el_mejor")
        return render_template('about.html', usuario_enviado = usuario)

@app.route("/")
def layout():
    return redirect(url_for('about'))

@app.route("/menu")
def menu():
    return render_template('menu.html')

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080)