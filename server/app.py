from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)  


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(300), unique=False)
    description = db.Column(db.String(400), unique=False)
    price = db.Column(db.Int(10), unique=False)
    img = db.Column(db.String(500), unique=False)

    
    def __init__(self, product, description, price, img):
        self.product = product
        self.description = description
        self.price = price
        self.img = img
        

class ProductSchema(ma.Schema):
        class Meta: 
            fields = ('id', 'product', 'description', 'price', 'img')

  
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)   


if __name__=='__main__':
    app.run(debug=True)  

#Merge with @app.route Jacob