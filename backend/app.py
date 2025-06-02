
from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Produto

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    produtos = Produto.query.all()
    return jsonify([p.to_dict() for p in produtos])

@app.route('/produtos', methods=['POST'])
def adicionar_produto():
    data = request.json
    novo = Produto(
        nome=data['nome'],
        descricao=data['descricao'],
        preco=data['preco'],
        categoria=data['categoria'],
        estoque=data['estoque'],
        fornecedor=data['fornecedor']
    )
    db.session.add(novo)
    db.session.commit()
    return jsonify(novo.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
