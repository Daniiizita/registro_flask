from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'nomes_flask'

mysql = MySQL(app)

@app.route('/nomes', methods=['GET', 'POST'])
def nomes():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM nomes")
        nomes = cursor.fetchall()
        cursor.close()
        return jsonify(nomes)
    elif request.method == 'POST':
        nome = request.form['nome']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO nomes (nome) VALUES (%s)", (nome,))
        mysql.connection.commit()
        cursor.close()
        return jsonify({'message': 'Nome inserido com sucesso'})

@app.route('/nomes/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def nome(id):
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM nomes WHERE id = %s", (id,))
        nome = cursor.fetchone()
        cursor.close()
        if nome:
            return jsonify(nome)
        else:
            return jsonify({'message': 'Nome não encontrado'})
    elif request.method == 'PUT':
        nome = request.form['nome']
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE nomes SET nome = %s WHERE id = %s", (nome, id))
        mysql.connection.commit()
        cursor.close()
        return jsonify({'message': 'Nome atualizado com sucesso'})
    elif request.method == 'DELETE':
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM nomes WHERE id = %s", (id,))
        mysql.connection.commit()
        cursor.close()
        return jsonify({'message': 'Nome excluído com sucesso'})

if __name__ == '__main__':
    app.run()
