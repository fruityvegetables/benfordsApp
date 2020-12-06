from flask import Flask, request, render_template, session, redirect
import numpy as np
import pandas as pd 

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, World! This is my first Flask app. I plan on using it to assert Benford's law."

