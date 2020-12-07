import pandas as pd 
#print('Pandas version', pd.__version__)
import matplotlib.pylab as plt

pd.options.display.max_rows = 999

census_2009 = pd.read_table('census_2009b')
census_2009.shape
census_2009['7_2009'].head()

first_digit_list=[]
for this_amt in list(census_2009['7_2009']):
   first_digit_list.append(str(this_amt)[0])

len(first_digit_list)

print(census_2009.shape)
print(first_digit_list[0:5])