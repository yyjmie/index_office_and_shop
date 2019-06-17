import pandas as pd
import numpy as np

def season_to_month(season):
	year_season = season.split('-')
	year = year_season[0]
	season = year_season[1]
	month = str(int(season)*3)
	if len(month)==1:
		month = '0'+month
	year_month = year+'-'+month
	return year_month

def month_to_season(month):
	year_month = month.split('-')
	year = year_month[0]
	month = year_month[1]
	season = str(int(int(month)/3))
	year_season = year+'-'+season
	return year_season

def merge(property_type, month):

	df = pd.read_csv(property_type+'_index.csv', usecols=['city', month])
	df.rename(columns={month:'investment_income_index'}, inplace=True)

	df1 = pd.read_csv(property_type+'_sale_index.csv', usecols=['city', month])
	df1.rename(columns={month:'house_price_index'}, inplace=True)

	df2 = pd.read_csv(property_type+'_rent_index.csv', usecols=['city', month])
	df2.rename(columns={month:'rent_index'}, inplace=True)

	df3 = pd.read_csv(property_type+'_index_rate_'+month+'.csv')
	df3.rename(columns={'one_year_rate':'annual_rate','three_year_rate':'year3_annual_rate','five_year_rate':'year5_annual_rate'})

	merged = pd.merge(df, df1, on='city', how='outer')
	merged = pd.merge(merged, df2, on='city', how='outer')
	merged = pd.merge(merged, df3, on='city', how='outer')
	merged['year_months'] = month_to_season(month)
	if property_type=='shop':
		property_type='business'
	merged['property_type'] = property_type

	return merged


