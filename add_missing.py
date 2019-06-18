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


file_name = 'office_sale.csv'
df = pd.read_csv(file_name, index_col=['city']).T.loc['2018-01':]
print(file_name+' missing or abnormal values information:')
show_missing_val_information(df)
draw_plot(df['青岛'])

file_name = 'office_rent.csv'
df = pd.read_csv(file_name, index_col=['city']).T.loc['2018-01':]
print(file_name+' missing or abnormal values information:')
show_missing_val_information(df)
draw_plot(df['兰州'])
draw_plot(df['哈尔滨'])

file_name = 'shop_sale.csv'
df = pd.read_csv(file_name, index_col=['city']).T.loc['2018-01':]
print(file_name+' missing or abnormal values information:')
show_missing_val_information(df)

file_name = 'shop_rent.csv'
df = pd.read_csv(file_name, index_col=['city']).T.loc['2018-01':]
print(file_name+' missing or abnormal values information:')
show_missing_val_information(df)
draw_plot(df['重庆'])

