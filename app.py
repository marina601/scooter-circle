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
        return redirect(url_for('profile', username=session["user"]))

    # Page Title
    title = 'Register'
    return render_template("register.html", title=title)


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

    # Page Title
    title = 'Login'
    return render_template("login.html", title=title)


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"].capitalize()
    # if the user is Admin, display all the reviews
    if username == "Admin":
        reviews = list(mongo.db.reviews.find())
    # Display reviews only created by session user
    else:
        reviews = list(mongo.db.reviews.find({"created_by": session["user"]}))

    # Page Title
    title = 'Profile'

    # checking if the user exists
    if session["user"]:
        return render_template(
                "profile.html", username=username,
                reviews=reviews, title=title)

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
    # Getting input values from the select element to sort the db
    price = request.args.get("product_price")
    range = request.args.get("product_max_range")
    charge = request.args.get("product_battery_charge")
    speed = request.args.get("product_max_speed")
    query = request.args.get("query")

    if query:
        products = mongo.db.products.find({"$text": {"$search": query}})
    else:
        products = mongo.db.products.find()

    # Checking with conditional statement if the value is high or low
    # and sorting accordingly

    if range == "high":
        products = products.sort("product_max_range", -1)
    elif range == "low":
        products = products.sort("product_max_range", 1)
    elif speed == "fast":
        products = products.sort("product_max_speed", -1)
    elif speed == "slow":
        products = products.sort("product_max_speed", 1)
    elif charge == "slow":
        products = products.sort("product_battery_charge", -1)
    elif charge == "fast":
        products = products.sort("product_battery_charge", 1)
    elif price == "high":
        products = products.sort("product_price", -1)
    elif price == "low":
        products = products.sort("product_price", 1)

    # Page Title
    title = 'Products'
    return render_template("products.html",
                           products=list(products), title=title)


# view product by id and add review to the product
@app.route("/view_product/<product_id>", methods=["GET", "POST"])
def view_product(product_id):

    product = mongo.db.products.find_one({"_id": ObjectId(product_id)})
    reviews = list(mongo.db.reviews.find().sort("product_model", 1))

    if 'user' not in session:
        return redirect(url_for("login"))

    return render_template("view_product.html",
                           product=product, reviews=reviews)


# add review
@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        review = {
            "product_model": request.form.get("product_model"),
            "product_review": request.form.get("product_review"),
            "created_by": session["user"]
        }
        mongo.db.reviews.insert_one(review)
        flash("Your Review Has Been Added")
        return redirect(url_for('profile', username=session['user']))

    if 'user' not in session:
        return redirect(url_for("login"))


# add product to the db only by Admin user
@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        product = {
            "product_model": request.form.get("product_model"),
            "product_brand": request.form.get("product_brand"),
            "product_price": int(request.form.get("product_price")),
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

    # Page Title
    title = 'Add-Product'
    return render_template("add_product.html", title=title)


# edit product for admit user only
@app.route("/edit_product/<product_id>", methods=["GET", "POST"])
def edit_product(product_id):
    if request.method == "POST":
        edit_scooter = {
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
        mongo.db.products.update({"_id": ObjectId(product_id)}, edit_scooter)
        flash("Product Has Been Succsefully Edited")

    product = mongo.db.products.find_one({"_id": ObjectId(product_id)})
    # Page Title
    title = 'Edit-Product'
    return render_template("edit_product.html", product=product, title=title)


# Delete Product
@app.route("/delete_product/<product_id>")
def delete_product(product_id):
    mongo.db.products.remove({"_id": ObjectId(product_id)})
    flash("Product Has Been Deleted")
    return redirect(url_for('products'))


# Delete Review
@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("You review has been Deleted")
    return redirect(url_for('profile', username=session['user']))


# Edit Review
@app.route("/add_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == "POST":
        update_review = {
            "product_model": request.form.get("product_model"),
            "product_review": request.form.get("product_review"),
            "created_by": session["user"]
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, update_review)
        flash("Your Review Has Been Succsefully Updated")
        return redirect(url_for('profile', username=session["user"]))

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    # Page Title
    title = 'Edit-Review'
    return render_template("edit_review.html", review=review, title=title)


# Contact Page
@app.route("/contact")
def contact():
    # Page Title
    title = 'Contact'
    return render_template("contact.html", title=title)


# 404 Page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', e=e), 404


# 500 error Page
@app.errorhandler(500)
def no_connection(e):
    return render_template("500.html", e=e), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
