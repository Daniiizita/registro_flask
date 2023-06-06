from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'nomes_flask'

mysql = MySQL(app)

api = Api(app)

class NomesResource(Resource):
    def get(self):
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT * FROM nomes")
        result = cursor.fetchall()
        return jsonify(result)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nome', type=str, help='Nome deve ser fornecido')
        args = parser.parse_args()
        nome = args['nome']

        cursor = mysql.connect().cursor()
        cursor.execute(f"INSERT INTO nomes (nome) VALUES ('{nome}')")
        mysql.connect().commit()

        return {'message': 'Nome inserido com sucesso'}, 201

api.add_resource(NomesResource, '/nomes')
