from flask import Flask, request, render_template, session, redirect
import numpy as np
import pandas as pd 

# generates an HTML view for our complete census data file.
app = Flask(__name__)

df = pd.read_table("census_2009b")

# routes to the render template as HTML
@app.route('/', methods=("POST", "GET"))   
def html_table():
    return render_template('index.html', tables=[df.to_html(classes='data')], titles=df.columns.values)

# I know this is a risky thing to put in our code, but I am learning (o:
if __name__ == '__main__':
    app.run(host='0.0.0.0')