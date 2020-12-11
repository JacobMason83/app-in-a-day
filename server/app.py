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
    productName = db.Column(db.String(300), unique=False)
    description = db.Column(db.String(400), unique=False)
    price = db.Column(db.Integer, unique=False)
    image = db.Column(db.String(500), unique=False)

    def __init__(self, productName, description, price, image):
        
        self.productName = productName
        self.description = description
        self.price = price
        self.image = image

class ProductSchema(ma.Schema):
        class Meta: 
            fields = ('id', 'productName', 'description', 'price', 'image')
            
product_schema = ProductSchema()
products_schema = ProductSchema(many=True) 

class CreditCardInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cvc= db.Column(db.Integer, unique=False)
    ccinfo= db.Column(db.Integer, unique=False)
    cardholderName= db.Column(db.String(100), unique=False)

    def __init__(self, cvc, ccinfo, cardholderName):
        self.cvc = cvc
        self.ccinfo = ccinfo
        self.cardholderName = cardholderName

class CreditCardInfoSchema(ma.Schema):
        class Meta: 
            fields = ('id','cvc', 'ccinfo', 'cardholderName')
creditCardInfo_schema = CreditCardInfoSchema()
creditCardInfo_schema = CreditCardInfoSchema(many=True) 
#-----------------------------------------------------------------------------------
@app.route('/product', methods=['POST'])
def add_product():
    productName = request.json['productName']
    description = request.json['description']
    price = request.json['price']
    image = request.json['image']
    new_product = Product( productName, description, price, image)
    
    
    db.session.add(new_product)
    db.session.commit()

    product = Product.query.get(new_product.id)
    return product_schema.jsonify(product) 

# making the product get all route 
@app.route('/products', methods=['GET'])
def get_allProducts():
    all_products = Product.query.all()   # gets all the movies in the app
    results = products_schema.dump(all_products)
    return jsonify(results)

# making the get route 
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
  product = Product.query.get(id)
  return  product_schema.jsonify(product)
# update 

@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
    # getting the movie queried by id 
    product = Product.query.get(id)
    # requesting the fields from the database to be used for the changes 
    productName = request.json['productName']
    description = request.json['description']
    price = request.json['price']
    image = request.json['image']
    
    # changing and updating the products
    product.productName = productName
    product.description = description
    product.price = price
    product.image = image
    # commiting the session of updating to the database 
    db.session.commit()
    # returning the new updated schema
    return product_schema.jsonify(product)

@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
# deleting the  product 
    db.session.delete(product)
    db.session.commit()
    return 'It was deleted, thank you for using me for your services'

@app.route('/creditcardinfo', methods=['POST'])
def add_ccinfo():
    cvc = request.form['cvc']
    ccinfo = request.form['ccinfo']
    cardhholderName = request.form['cardholderName']
    new_creditCardInfo = CreditCardInfo(id, cvc, ccinfo, cardholderName)

    db.session.add(new_creditCardInfo)
    db.session.commit()
    creditCardInfo = CreditCardInfo.query.get(new_creditCardInfo.id)
    return creditCardInfo_schema.jsonify(creditCardInfo) 

    creditCardInfo = CreditCardInfo.query.get(new_creditCardInfo.id)
    return creditCardInfo_schema.jsonify(creditCardInfo) 

@app.route('/creditcardinfo/<id>', methods=['DELETE'])
def delete_creditCardInfo(id):
    creditCardInfo = CreditCardInfo.query.get(id)
    db.session.delete(creditCardInfo)
    db.session.commit()
    return "It was deleted"

if __name__=='__main__':
    app.run(port=7000, debug=True)  
#Merge with @app.route Jacob