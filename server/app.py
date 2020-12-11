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
    price = db.Column(db.Int(10), unique=False)
    img = db.Column(db.String(500), unique=False)

    
    def __init__(self, productName, description, price, img):
        self.productName = productName
        self.description = description
        self.price = price
        self.img = img
        

class ProductSchema(ma.Schema):
        class Meta: 
            fields = ('id', 'productName', 'description', 'price', 'img')

  
product_schema = ProductSchema()
products_schema = ProductSchema(many=True) 
@app.route('/product', methods=['POST'])
def add_product():
    product = request.form['productName']
    description = request.form['description']
    price = request.form['price']
    image = request.form['image']
    
    new_product = Product(id, productName, description, price, image)
    
    db.session.add(new_product)
    db.session.commit()
    
    product = Product.query.get(new_product.id)
    
    return product_schema.jsonify(product) 

# making the movie get all route 
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
    
    productName = request.form['productName']
    description = request.form['description']
    price = request.form['price']
    image = request.form['image']
    
    # changing and updating the movie titles 
    product.productName = productName
    product.description = description
    product.price = price
    product.image = image
    
    
    # commiting the session of updating to the database 
    db.session.commit()
    # returning the new updated schema
    return movie_schema.jsonify(product)

@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    
# deleting the movie
    db.session.delete(movie)
    db.session.commit()
    
    return 'It was deleted, thank you for using me for your services'


if __name__=='__main__':
    app.run(debug=True)  

#Merge with @app.route Jacob