import pandas as pd
import numpy as np

def extract_month(season):
	num = int(season[-1])
	month = str(3*num)
	if len(month)==1:
		month = '0'+month
	year_month = season[0:5]+month
	return year_month

def merge(property_type, season):
	month = extract_month(season)

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
	merged['year_months'] = season
	if property_type=='shop':
		property_type='business'
	merged['property_type'] = property_type

	return merged

'''
df_office_1 = merge('office', '2018-1')
df_office_2 = merge('office', '2018-2')
df_office_3 = merge('office', '2018-3')
df_office_4 = merge('office', '2018-4')
df_office_5 = merge('office', '2019-1')

df_shop_1 = merge('shop', '2018-1')
df_shop_2 = merge('shop', '2018-2')
df_shop_3 = merge('shop', '2018-3')
df_shop_4 = merge('shop', '2018-4')
df_shop_5 = merge('shop', '2019-1')

pieces = [df_office_1,df_office_2,df_office_3,df_office_4,df_office_5,df_shop_1,df_shop_2,df_shop_3,df_shop_4,df_shop_5]

df = pd.concat(pieces, ignore_index=True)

df.to_csv('submit.csv', index=False)
'''

