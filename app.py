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
    Login route
    Check if user exists in the database
    Check if password matches user input
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
            flash("You have entered incorrect Username and/or Password")
            return redirect(url_for('login'))

    # if the user is already in session
    if 'user' in session:
        return redirect(url_for('profile', username=session['user']))

    # Page Title
    title = 'Login'
    return render_template("login.html", title=title)


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Profile route
    Checks if the user is in session
    Query is sent to DB
    Display all the reviews created by user
    If the username = Admin, display all the reviews
    If user is not logged in, redirect to login page
    """
    # Page Title
    title = 'Profile'

    reviews = list(mongo.db.reviews.find())

    if 'user' in session:
        username = mongo.db.users.find_one(
            {"username": username})["username"].capitalize()

        if username == "Admin":
            reviews = list(mongo.db.reviews.find())
        else:
            reviews = list(mongo.db.reviews.find(
                           {"created_by": session["user"]}))
    else:
        flash('You must be logged in!')
        return redirect(url_for('login'))

    return render_template(
                "profile.html", username=username,
                reviews=reviews, title=title)


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("index"))


@app.route("/products")
def products():
    """
    Products route
    Displays all products in the DB
    Text index created to allow user to search DB
    by product_model or product_brand
    If a query is empty displays all products
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
    Sorting database by ascending or descending order
    to allow for filter function
    This code has been modified from
    https://stackoverflow.com/questions/65493525/sorting-in-flask-via-jinja-template-variable-issue-when-called
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
    View product by product id
    display reviews for the specific product
    If user is not in session redirect to login page
    """
    product = mongo.db.products.find_one({"_id": ObjectId(product_id)})
    reviews = list(mongo.db.reviews.find().sort("product_model", 1))

    if 'user' not in session:
        flash("You must be logged in to view this page!")
        return redirect(url_for("login"))

    # Page Title
    title = 'View Product'

    return render_template("view_product.html",
                           product=product, reviews=reviews, title=title)


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    """
    Add review route
    Creating a dictionary to be inserted in the DB
    Insert user review to the DB
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
    Updating product_reviews in product collection
    by incrementing total amount by 1
    each time a new review is added
    How to increment a value, source has been found
    in MongoDB documentation
    (https://docs.mongodb.com/manual/reference/operator/update/inc/)
    """
    mongo.db.products.update({"product_model": request.form.get
                             ("product_model")},
                             {'$inc': {"product_reviews": int(1)}})

    flash("Your Review Has Been Added")
    return redirect(url_for('profile', username=session['user']))


@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    """
    Add product to the database route
    If user is not logged in redirect to homepage
    If user is not Admin redirect to login page
    """
    if "user" not in session:
        return redirect(url_for("index"))

    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"].capitalize()

    if username != "Admin":
        flash("You do not have access to this page")
        return redirect(url_for("login"))

    """
    Adding product to the DB
    Creating a dictionary to add to the DB
    Insert a dictionary to the DB
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
    If user not logged in redirect to home page
    If the username is not "Admin"
    Redirect to login page
    """
    if 'user' not in session:
        return redirect(url_for("index"))

    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"].capitalize()

    if username != "Admin":
        flash("You do not have access to this page")
        return redirect(url_for("login"))

    """
    Editing existing product
    Create a dictionary
    getting the values from the form input fields
    Update product based on product id
    """

    product = mongo.db.products.find_one({"_id": ObjectId(product_id)})

    if request.method == "POST":
        edit_scooter = {
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
            "product_reviews": product['product_reviews']
        }
        mongo.db.products.update({"_id": ObjectId(product_id)}, edit_scooter)
        flash("Product Has Been Succesfully Edited")
        return redirect(url_for('products'))

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
    Find product_model name
    Update number of product_reviews
    by decreasing the total reviews amount by 1
    """

    product_reviewed = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    product_model = product_reviewed['product_model']

    mongo.db.products.update_one({"product_model": product_model},
                                 {'$inc': {"product_reviews": -1}})

    mongo.db.reviews.delete_one({"_id": ObjectId(review_id)})
    flash("Your review has been Deleted")

    return redirect(url_for('profile', username=session['user']))


# Edit Review
@app.route("/add_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    """
    Edit review route
    Update the user review based on review_id
    """
    if request.method == "POST":
        update_review = {
            "product_model": request.form.get("product_model"),
            "product_review": request.form.get("product_review"),
            "created_by": session["user"]
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, update_review)
        flash("Your Review Has Been Successfully Updated")
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
    return render_template("404.html", e=e), 404


@app.errorhandler(500)
def no_connection(e):
    """
    Custom 500 error page
    """
    return render_template("500.html", e=e), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
