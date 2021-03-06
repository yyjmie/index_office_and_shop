import calculate as cal
import merge as mg
import preprocess as pp
import arrow


# define global variables

start_month = '2019-05'
end_month = '2019-06'

start_season = '2018-1'
end_season = '2019-2'

# merge new sale and rent file to the big table

month = start_month
while month != end_month:

	pp.json_to_csv("office_sale_"+month+".json", "mid1.csv", month)
	pp.preprocess("mid1.csv", "mid2.csv", month)
	cal.save_table("office_sale.csv", "mid2.csv", month)

	pp.json_to_csv("office_rent_"+month+".json", "mid1.csv", month)
	pp.preprocess("mid1.csv", "mid2.csv", month)
	cal.save_table("office_rent.csv", "mid2.csv", month)

	pp.json_to_csv("shop_sale_"+month+".json", "mid1.csv", month)
	pp.preprocess("mid1.csv", "mid2.csv", month)
	cal.save_table("shop_sale.csv", "mid2.csv", month)

	pp.json_to_csv("shop_rent_"+month+".json", "mid1.csv", month)
	pp.preprocess("mid1.csv", "mid2.csv", month)
	cal.save_table("shop_rent.csv", "mid2.csv", month)

	month = arrow.get(month, 'YYYY-MM').shift(months=1).format('YYYY-MM')

'''
# calculate office and shop investment index from start_month to end_month

month = start_month
while month != end_month:

	# office index calculate and save
	cal.investment_index_calculate('office_index.csv', 'office_sale.csv', 'office_rent.csv', 'index_new.csv', month)
	cal.save_table('office_index.csv', 'index_new.csv', month)
	
	cal.sale_or_rent_index_calculate('office_sale_index.csv', 'office_sale.csv', 'index_new.csv', month)
	cal.save_table('office_sale_index.csv', 'index_new.csv', month)

	cal.sale_or_rent_index_calculate('office_rent_index.csv', 'office_rent.csv', 'index_new.csv', month)
	cal.save_table('office_rent_index.csv', 'index_new.csv', month)

	# shop index calculate and save
	cal.investment_index_calculate('shop_index.csv', 'shop_sale.csv', 'shop_rent.csv', 'index_new.csv', month)
	cal.save_table('shop_index.csv', 'index_new.csv', month)

	cal.sale_or_rent_index_calculate('shop_sale_index.csv', 'shop_sale.csv', 'index_new.csv', month)
	cal.save_table('shop_sale_index.csv', 'index_new.csv', month)

	cal.sale_or_rent_index_calculate('shop_rent_index.csv', 'shop_rent.csv', 'index_new.csv', month)
	cal.save_table('shop_rent_index.csv', 'index_new.csv', month)

	month = arrow.get(month, 'YYYY-MM').shift(months=1).format('YYYY-MM')


start_month = mg.season_to_month(start_season)
end_month = mg.season_to_month(end_season)

# calculate investment index rate and save

month = start_month
while month != end_month:

	cal.index_rate('office_index.csv', 'office_index_rate_'+month+'.csv', month)
	cal.index_rate('shop_index.csv', 'shop_index_rate_'+month+'.csv', month)

	month = arrow.get(month, 'YYYY-MM').shift(months=3).format('YYYY-MM')


# merge all csv files to  a submit file

pieces = []

month = start_month
while month != end_month:

	df_office = mg.merge('office', month)
	df_shop = mg.merge('shop', month)

	pieces.append(df_office)
	pieces.append(df_shop)

	month = arrow.get(month, 'YYYY-MM').shift(months=3).format('YYYY-MM')

df = pd.concat(pieces, ignore_index=True)
df.to_csv('submit.csv', index=False)
'''