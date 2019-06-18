import pandas as pd
import numpy as np
import json 
import csv

def process_city_name(df):
	city = df.values
	for i in range(len(city)):
		if city[i][-1]=='市':
			city[i] = city[i][:-1]
	return city

# extract shop&&office rent&&sale history data.
def extract_origin_history_data(file_name):

	df = pd.read_csv(file_name, usecols=['city','date','value','type'])
	df[df.value==-10086] = np.nan

	df_office_sale = df[df.type=='office_sale']
	df_office_sale = pd.pivot_table(df_office_sale, values='value', index='city', columns='date')
	df_office_sale = df_office_sale.reset_index()
	df_office_sale.city = process_city_name(df_office_sale.city)
	df_office_sale.to_csv('office_sale.csv', index=False)

	df_office_rent = df[df.type=='office_rent']
	df_office_rent = pd.pivot_table(df_office_rent, values='value', index='city', columns='date')
	df_office_rent = df_office_rent.reset_index()
	df_office_rent.city = process_city_name(df_office_rent.city)
	df_office_rent.to_csv('office_rent.csv', index=False)

	df_shop_sale = df[df.type=='shop_sale']
	df_shop_sale = pd.pivot_table(df_shop_sale, values='value', index='city', columns='date')
	df_shop_sale = df_shop_sale.reset_index()
	df_shop_sale.city = process_city_name(df_shop_sale.city)
	df_shop_sale.to_csv('shop_sale.csv', index=False)

	df_shop_rent = df[df.type=='shop_rent']
	df_shop_rent = pd.pivot_table(df_shop_rent, values='value', index='city', columns='date')
	df_shop_rent = df_shop_rent.reset_index()
	df_shop_rent.city = process_city_name(df_shop_rent.city)
	df_shop_rent.to_csv('shop_rent.csv', index=False)


# extract shop&&office investment&&house&&rent index history data.
def extract_index_history_data(file_name):

	df = pd.read_csv('big_data_index.csv', usecols=
		['year_months','property_type','city_name','investment_income_index','house_price_index','rent_index'])

	df_office_index = df[df.property_type=='office']
	df_office_ivst_index = pd.pivot_table(df_office_index, values='investment_income_index', index='city_name', columns='year_months')
	df_office_ivst_index = df_office_ivst_index.reset_index()
	df_office_ivst_index.city_name = process_city_name(df_office_ivst_index.city_name)
	df_office_ivst_index.to_csv('office_index.csv', index=False)
	df_office_sale_index = pd.pivot_table(df_office_index, values='house_price_index', index='city_name', columns='year_months')
	df_office_sale_index = df_office_sale_index.reset_index()
	df_office_sale_index.city_name = process_city_name(df_office_sale_index.city_name)
	df_office_sale_index.to_csv('office_sale_index.csv', index=False)
	df_office_rent_index = pd.pivot_table(df_office_index, values='rent_index', index='city_name', columns='year_months')
	df_office_rent_index = df_office_rent_index.reset_index()
	df_office_rent_index.city_name = process_city_name(df_office_rent_index.city_name)
	df_office_rent_index.to_csv('office_rent_index.csv', index=False)

	df_shop_index = df[df.property_type=='business']
	df_shop_ivst_index = pd.pivot_table(df_shop_index, values='investment_income_index', index='city_name', columns='year_months')
	df_shop_ivst_index = df_shop_ivst_index.reset_index()
	df_shop_ivst_index.city_name = process_city_name(df_shop_ivst_index.city_name)
	df_shop_ivst_index.to_csv('shop_index.csv', index=False)
	df_shop_sale_index = pd.pivot_table(df_shop_index, values='house_price_index', index='city_name', columns='year_months')
	df_shop_sale_index = df_shop_sale_index.reset_index()
	df_shop_sale_index.city_name = process_city_name(df_shop_sale_index.city_name)
	df_shop_sale_index.to_csv('shop_sale_index.csv', index=False)
	df_shop_rent_index = pd.pivot_table(df_shop_index, values='rent_index', index='city_name', columns='year_months')
	df_shop_rent_index = df_shop_rent_index.reset_index()
	df_shop_rent_index.city_name = process_city_name(df_shop_rent_index.city_name)
	df_shop_rent_index.to_csv('shop_rent_index.csv', index=False)


# convert origin json file to csv file 
def json_to_csv(from_file, to_file, this_month):

	with open(from_file) as json_file:
		with open (to_file, 'w') as csv_file:
			
			fieldnames = ['url', 'city', 'new_num', 'rent']
			writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
			writer.writerow({'url':'url', 'city':'city', 'new_num':'num', 'rent':this_month})

			for line in json_file:
				# 按行将json数据转化为字典
				dic = json.loads(line)
				# 替换数字中间的逗号
				dic['new_num'] = dic['new_num'].replace(',', '')
				dic['rent'] = dic['rent'].replace(',', '') 
				if dic['new_num'] == '--':
					dic['new_num'] = ''
				if dic['rent'] == '--':
					dic['rent'] = ''
				# 写入csv文件
				writer.writerow(dic)

# 选列、nan
def preprocess(from_file, to_file, this_month):
	df = pd.read_csv(from_file, usecols = ['city', this_month], na_values = 'na')
	if from_file == 'mid_rent.csv':
		df = df.fillna(0)
	df.to_csv(to_file, index = False)


# file = 'out_data.csv'
# extract_origin_history_data(file)

# file = 'big_data_index.csv'
# extract_index_history_data(file)
