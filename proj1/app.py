from flask import Flask
from flask import request
from flask import url_for

app=Flask(__name__)

url_for('static', filename='style.css')

