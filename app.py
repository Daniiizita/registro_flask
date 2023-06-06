from flask import Flask, redirect, render_template, request
from flaskext.mysql import MySQL

app = Flask(__name__)
nomes = []  # Lista para armazenar os nomes inseridos


# Configuração do MySQL
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'nomes_flask'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form.get('nome')
        nomes.append(nome)
    return render_template('index.html', nomes=nomes)

if __name__ == '__main__':
    app.run(debug=True)

""" CRUD LOGO ABAIXO """

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    if request.method == 'POST':
        nome = request.form.get('nome')
        nomes[index] = nome
        return redirect('/')
    nome = nomes[index]
    return render_template('edit.html', nome=nome, index=index)

@app.route('/delete/<int:index>')
def delete(index):
    del nomes[index]
    return redirect('/')
