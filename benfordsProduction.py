#I have a bad habit of importing all things I may or may not need :P
from flask import Flask, request, render_template, session, redirect, make_response, send_file
import pandas as pd 
#print('Pandas version', pd.__version__)
import matplotlib
import matplotlib.pylab as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

#variables for census data
census_2009 = pd.read_table('census_2009b')
census_2009.shape
census_2009['7_2009'].head()

## function for retrieving first digit
first_digit_list=[]
for this_amt in list(census_2009['7_2009']):
   first_digit_list.append(str(this_amt)[0])

len(first_digit_list)

print(census_2009.shape)
print(first_digit_list[0:5])

#variables for matplotlib graph
#labels = ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9']
#x = np.arange(len(labels))
#width = 0.35

#fig, ax = plt.subplots()
##rects1 = ax.bar(x - width/2, first_digit_list, width, label='Census Data')
#rects2 = ax.bar(x + width/2, benfords_list, width, label='Benford Prediction')

#some text for labels, title, and x-axis tick labels
# ax.set_ylabel("amount of leading digit occurence")
# ax.set_title("Benford's assertion within the census data")
# ax.set_xticks(x)
# ax.set_xticklabels(labels)
# ax.legend()

##graphing functions

first_digit_list.sort()
_=plt.hist(first_digit_list, bins=len(set(first_digit_list)))
_=plt.xlabel('leading digit')
_=plt.ylabel('count')

plt.show()