# this is my file to test rendering matplotlib inside of flask
import base64
from io import BytesIO

from flask import Flask
import matplotlib.pylab as plt
from matplotlib.figure import Figure
import pandas as pd 

app = Flask(__name__)


@app.route("/")
def hello():

    #variables for census data
    census_2009 = pd.read_table('census_2009b')
    census_2009.shape
    census_2009['7_2009'].head()

    ## function for retrieving first digit
    first_digit_list=[]
    for this_amt in list(census_2009['7_2009']):
        first_digit_list.append(str(this_amt)[0])

    len(first_digit_list)

    first_digit_list.sort()
    _=plt.hist(first_digit_list, bins=len(set(first_digit_list)))
    _=plt.xlabel('leading digit')
    _=plt.ylabel('count')

    plt.show()
    # Generate the figure
    fig = Figure()
    ax = fig.subplots()
    ax.plot([500, 6000])
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"
    