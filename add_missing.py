import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def draw_plot(df):
	
	df.index = pd.to_datetime(df.index)

	fig,ax = plt.subplots()
	ax.plot(df.index.values, df.values)

	ax.xaxis.set_major_locator(mdates.YearLocator())
	ax.xaxis.set_minor_locator(mdates.MonthLocator())
	ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
	ax.xaxis.set_minor_formatter(mdates.DateFormatter('%m'))

	datemin = df.index[0]
	datemax = df.index[-1]
	ax.set_xlim(datemin, datemax)

	ax.grid(True)
	fig.autofmt_xdate()

	plt.show()


def show_missing_val_information(df):
	# missing
	missing_val_count_by_column = (df.isnull().sum())
	print(missing_val_count_by_column[missing_val_count_by_column>0])
	# abnormal
	min_val = df.min()
	print(min_val[min_val<=0])

file_list = ['office_sale.csv', 'office_rent.csv', 'shop_sale.csv', 'shop_rent.csv']

# show missing values information
for file in file_list:
	df = pd.read_csv(file, index_col=['city']).T
	print(file+' missing or abnormal values information:')
	show_missing_val_information(df)	

# fill in the missing values using interpolate method
for file in file_list:
	df = pd.read_csv(file, index_col=['city'])
	df = df.interpolate(axis=1)
	df.to_csv(file)

