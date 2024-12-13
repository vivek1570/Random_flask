import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect,session
from werkzeug.exceptions import abort
from werkzeug.security import generate_password_hash,check_password_hash
from functools import wraps

app=Flask(__name__)

app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def index():
  return "hello world"

# Decorator to require login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:  # Check if user is logged in
            return redirect("/login")  # Redirect to login if not authenticated
        return f(*args, **kwargs)
    return decorated_function




def get_db_connection():
  conn=sqlite3.connect('database.db')
  conn.row_factory=sqlite3.Row
  return conn


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Validate form data
        username = request.form.get("username")
        passw = request.form.get("password")
        email = request.form.get("email")

        if not (username and passw and email):
            return render_template("register.html", message="All fields are required.")

        # Hash the passw
        hashed_password = generate_password_hash(passw)

        # Store user data in the database
        # Your database insertion code goes here
        conn=get_db_connection()
        conn.execute('INSERT INTO login_table (username,passw,email) VALUES(?,?,?)',
        (username,hashed_password,email))
        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        passw = request.form.get("password")

        # Retrieve user data from the database
        # Your database query code goes here

        conn=get_db_connection()
        # user=conn.execute('SELECT username,passw,email FROM login_table WHERE username=?',(username,)).fetchone()
        user = conn.execute('SELECT id, username, passw, email FROM login_table WHERE username=?', (username,)).fetchone()
        # Check if username exists and passw is correct
        if user and check_password_hash(user["passw"], passw):
            session["user_id"] = user["id"]
            return redirect("/userhome")
        else:
            return render_template("login.html", message="Invalid username or passw.")

    return render_template("login.html")


@app.route("/userhome")
@login_required
def userhome():
    return "welcome to home page"