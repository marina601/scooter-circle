import os
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sslify import SSLify
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
sslify = SSLify(app)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


"""
@app.before_request
def before_request():

    Forcing the url if run on http
    to redirect to https secure server
    help found on
    https://stackoverflow.com/questions/15116312/redirect-http-to-https-on-flaskheroku
    if 'DYNO' in os.environ:
        if request.url.startswith('http://'):
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)
"""


@app.route("/")
@app.route("/index")
def index():
    """
    Find Products from Mongo db collection
    """
    products = mongo.db.products.find()
    return render_template("index.html", products=products)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Checking if the user already exists,
    If not, then checking if username exists
    Checking if password_1 = password_2
    Creating a dictionary to insert user into db
    Insert the new user into db
    Put the user into 'session' cookie
    Redirect the user to their profile page
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username in use, try alternative")
            return redirect(url_for("register"))

        password_1 = request.form.get("password")
        password_2 = request.form.get("password_2")

        if password_1 != password_2:
            flash("Your passwords do not match")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("You have successfully Registered!")
        return redirect(url_for('profile', username=session["user"]))

    # Page Title
    title = 'Register'
    return render_template("register.html", title=title)


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Login function checks if the method is POST
    If user exists in the database
    If password matches user input
    Redirects user to profile page
    Otherwise error message displayed
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
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
    """
    Profile function grabs the session user's username
    from database and displays user's reviews
    If session user is Admin display all the reviews
    in the database
    """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"].capitalize()

    if username == "Admin":
        reviews = list(mongo.db.reviews.find())
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


@app.route("/products")
def products():
    """
    Getting input field values from the select element
    Search function checks allows users to search products
    by product_model or product_brand
    If query is empty displays all products from the database
    """

    price = request.args.get("product_price")
    range = request.args.get("product_max_range")
    charge = request.args.get("product_battery_charge")
    speed = request.args.get("product_max_speed")
    query = request.args.get("query")

    if query:
        products = mongo.db.products.find({"$text": {"$search": query}})
    else:
        products = mongo.db.products.find()

    """
    Sorting database by accessending or dissending order
    to allow filter function
    """

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

    # Checking if the user is in session
    if 'user' not in session:
        flash("You must be logged in to view this page!")
        return redirect(url_for("login"))

    return render_template("products.html",
                           products=list(products), title=title)


@app.route("/view_product/<product_id>", methods=["GET", "POST"])
def view_product(product_id):
    """
    View products by product id and
    display reviews for the specific product
    If user is not in session return the user to login page
    """
    product = mongo.db.products.find_one({"_id": ObjectId(product_id)})
    reviews = list(mongo.db.reviews.find().sort("product_model", 1))

    if 'user' not in session:
        return redirect(url_for("login"))

    return render_template("view_product.html",
                           product=product, reviews=reviews)


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    """
    Add review function checks if the method="POST"
    Creating a dictionary to be inserted in the database
    Insert user review to the database
    Redirect the user to their profile page
    """
    if request.method == "POST":
        review = {
            "product_model": request.form.get("product_model"),
            "product_review": request.form.get("product_review"),
            "created_by": session["user"]
        }
        mongo.db.reviews.insert_one(review)
    """
    Updating product amount of product reviews
    by incrementing the product_reviews amount by
    1 every time a new review is added
    """
    mongo.db.products.update({"product_model": request.form.get
                             ("product_model")},
                             {'$inc': {"product_reviews": int(1)}})

    flash("Your Review Has Been Added")
    return redirect(url_for('profile', username=session['user']))

    # if user is not in session return the user to login page
    if 'user' not in session:
        return redirect(url_for("login"))


@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    """
    Add product to the database by Admin user only
    Checking if the user is in session
    and if the username is "Admin"
    Otherwise redirect to login page
    """

    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"].capitalize()

    if 'user' not in session:
        flash("You must be logged in with Admin account to access this page!")
        return redirect(url_for("login"))
    if username != "Admin":
        flash("You do not have access to this page")
        return redirect(url_for("login"))

    """
    Adding product to the databae
    Creating a dictionary to add to the database
    Insert a dictionary to the database
    Redirect Admin user to the products.html
    """

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
            "product_description": request.form.get("product_description"),
            "product_reviews": int(0)
        }

        mongo.db.products.insert_one(product)

        flash("A New Product Has Been Succsefully Added")
        return redirect(url_for('products'))

    # Page Title
    title = 'Add-Product'
    return render_template("add_product.html", title=title)


@app.route("/edit_product/<product_id>", methods=["GET", "POST"])
def edit_product(product_id):
    """
    Checking if the user is in session
    and if the username is "Admin"
    Otherwise redirect to login page
    """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"].capitalize()

    if 'user' not in session:
        flash("You must be logged in with Admin account to access this page!")
        return redirect(url_for("login"))
    if username != "Admin":
        flash("You do not have access to this page")
        return redirect(url_for("login"))

    """
    Editing existing product if the method is post
    Create a dictionary getting the values from the form input fields
    Update product based on product id
    """

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
            "product_description": request.form.get("product_description"),
            "product_reviews": int(0)
        }
        mongo.db.products.update({"_id": ObjectId(product_id)}, edit_scooter)
        flash("Product Has Been Succsefully Edited")

    product = mongo.db.products.find_one({"_id": ObjectId(product_id)})

    # Page Title
    title = 'Edit-Product'
    return render_template("edit_product.html", product=product, title=title)


@app.route("/delete_product/<product_id>")
def delete_product(product_id):
    """
    Delete product from the database
    """
    mongo.db.products.remove({"_id": ObjectId(product_id)})
    flash("Product Has Been Deleted")
    return redirect(url_for('products'))


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    """
    Delete review from the database
    Find the review by the id
    Find the value of the product_model being deleted
    Updating amount of product reviews
    by decreasing the product_reviews amount by
    1 every time a review is deleted
    """

    product_reviewed = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    product_model = product_reviewed['product_model']

    mongo.db.products.update_one({"product_model": product_model},
                                 {'$inc': {"product_reviews": -1}})

    mongo.db.reviews.delete_one({"_id": ObjectId(review_id)})
    flash("You review has been Deleted")

    return redirect(url_for('profile', username=session['user']))


# Edit Review
@app.route("/add_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    """
    Edit review function checks if
    the reques method = "POST"
    creating a dictionary getting all the input values from
    the input field elements
    Update the user review based on review_id
    """
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


@app.route("/contact")
def contact():
    """
    Contact Page
    """
    title = 'Contact'
    return render_template("contact.html", title=title)


@app.errorhandler(404)
def page_not_found(e):
    """
    Custome 404 error page
    """
    return render_template('404.html', e=e), 404


@app.errorhandler(500)
def no_connection(e):
    """
    Custom 500 error page
    """
    return render_template("500.html", e=e), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
