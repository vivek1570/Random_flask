from flask import Flask 
from markupsafe import escape
app=Flask(__name__)

@app.route("/about/<name>")

def project(name):
  return f"ada mapale {escape(name)}"