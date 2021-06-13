import os
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    products = mongo.db.products.find()
    return render_template("index.html", products=products)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if the user exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        password_1 = request.form.get("password")
        password_2 = request.form.get("password_2")

        # check if the username already exists
        if existing_user:
            flash("Username in use, try alternative")
            return redirect(url_for("register"))

        # check if the password_1 matches to password_2
        if password_1 != password_2:
            flash("Your passwords do not match")
            return redirect(url_for("register"))

        # create a dictionary to be inserted in the db
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("You have successfully Registered!")
        return redirect(url_for('profile', username=session["username"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if the user already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check if the hashed password matches the user input
            if check_password_hash(existing_user
                                   ["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}"
                      .format(request.form.get("username").capitalize()))
                return redirect(url_for(
                    'profile', username=session["user"]))

            else:
                # invalid password match
                flash("You have enetered incorrect Username and/or Password")
                return redirect(url_for('login'))

        else:
            # invalid username match
            flash("You have enetered incorrect Username and/or Password")
            return redirect(url_for('login'))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"].capitalize()
    # checking if the user exists
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for('login'))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# all products
@app.route("/products")
def products():
    products = mongo.db.products.find()
    return render_template("products.html", products=products)


# view product by id and add review to the product
@app.route("/view_product/<product_id>", methods=["GET", "POST"])
def view_product(product_id):
    product = mongo.db.products.find_one({"_id": ObjectId(product_id)})
    if request.method == "POST":
        review = {
            "prduct_model": request.form.get("product_model"),
            "product_review": request.form.get("product_review"),
            "created_by": session["user"]
        }
        mongo.db.reviews.insert_one(review)
        flash("Your Review Has Been Added")
        return redirect(url_for('products'))

    reviews = mongo.db.reviews.find().sort("product_review", 1)

    if 'user' not in session:
        return redirect(url_for("login"))

    return render_template("view_product.html",
                           product=product, reviews=reviews)


# add product to the db only by Admin user
@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        product = {
            "product_model": request.form.get("product_model"),
            "product_brand": request.form.get("product_brand"),
            "product_price": request.form.get("product_price"),
            "product_max_range": request.form.get("product_max_range"),
            "product_max_speed": request.form.get("product_max_speed"),
            "product_motor_power": request.form.get("product_motor_power"),
            "product_load": request.form.get("product_load"),
            "product_wheel_size": request.form.get("product_wheel_size"),
            "product_battery_charge":
                request.form.get("product_battery_charge"),
            "product_water_resistant":
                request.form.get("product_water_resistant"),
            "product_weight": request.form.get("product_weight"),
            "product_affiliate_link":
                request.form.get("product_affiliate_link"),
            "product_image": request.form.get("product_image"),
            "product_description": request.form.get("product_description")
        }
        mongo.db.products.insert_one(product)
        flash("A New Product Has Been Succsefully Added")
        return redirect(url_for('products'))

    return render_template("add_product.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
