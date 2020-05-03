import os
from flask import Flask, render_template, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'myYummyDishes'
app.config["MONGO_URI"] = 'mongodb+srv://root:R00tUser@myfirstcluster-kwp3n.mongodb.net/myYummyDishes?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/display_recipes')
def display_recipes():
    return render_template('display-recipes.html', recipes=mongo.db.recipes.find())


@app.route('/add_recipe')
def add_recipe():
    return render_template('add-recipe.html')


@app.route('/edit_recipe')
def edit_recipe():
    return render_template('edit-recipe.html')


@app.route('/recipe')
def recipe():
    return render_template('recipe.html')


@app.route('/Categories')
def Categories():
    return render_template('category.html', Categories=mongo.db.Categories.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)