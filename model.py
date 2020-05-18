from app import db


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(500), nullable=False, comment='路径')
    name = db.Column(db.String(100), nullable=False, comment='名称')
