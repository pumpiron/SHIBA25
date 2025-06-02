from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    estoque = db.Column(db.Integer, nullable=False)
    fornecedor = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "preco": self.preco,
            "categoria": self.categoria,
            "estoque": self.estoque,
            "fornecedor": self.fornecedor
        }