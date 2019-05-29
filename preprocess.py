import pandas as pd
import numpy as np

# extract shop&&office rent&&sale history data.

'''
df = pd.read_csv('out_data.csv', usecols=['city','date','value','type'])
df[df.value==-10086] = np.nan

df_office_sale = df[df.type=='office_sale']
df_office_sale = pd.pivot_table(df_office_sale, values='value', index='city', columns='date')
df_office_sale.to_csv('office_sale.csv')

df_office_rent = df[df.type=='office_rent']
df_office_rent = pd.pivot_table(df_office_rent, values='value', index='city', columns='date')
df_office_rent.to_csv('office_rent.csv')

df_shop_sale = df[df.type=='shop_sale']
df_shop_sale = pd.pivot_table(df_shop_sale, values='value', index='city', columns='date')
df_shop_sale.to_csv('shop_sale.csv')

df_shop_rent = df[df.type=='shop_rent']
df_shop_rent = pd.pivot_table(df_shop_rent, values='value', index='city', columns='date')
df_shop_rent.to_csv('shop_rent.csv')
'''

# extract shop&&office investment&&house&&rent index history data.

'''
df = pd.read_csv('big_data_index.csv', usecols=
	['year_months','property_type','city_name','investment_income_index','house_price_index','rent_index'])

df_office_index = df[df.property_type=='office']
df_office_ivst_index = pd.pivot_table(df_office_index, values='investment_income_index', index='city_name', columns='year_months')
df_office_ivst_index.to_csv('office_index.csv')
df_office_sale_index = pd.pivot_table(df_office_index, values='house_price_index', index='city_name', columns='year_months')
df_office_sale_index.to_csv('office_sale_index.csv')
df_office_rent_index = pd.pivot_table(df_office_index, values='rent_index', index='city_name', columns='year_months')
df_office_rent_index.to_csv('office_rent_index.csv')

df_shop_index = df[df.property_type=='business']
df_shop_ivst_index = pd.pivot_table(df_shop_index, values='investment_income_index', index='city_name', columns='year_months')
df_shop_ivst_index.to_csv('shop_index.csv')
df_shop_sale_index = pd.pivot_table(df_shop_index, values='house_price_index', index='city_name', columns='year_months')
df_shop_sale_index.to_csv('shop_sale_index.csv')
df_shop_rent_index = pd.pivot_table(df_shop_index, values='rent_index', index='city_name', columns='year_months')
df_shop_rent_index.to_csv('shop_rent_index.csv')
'''