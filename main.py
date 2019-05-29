import calculate as cal
import arrow

month = '2018-01'

'''
while month != '2019-04':
	cal.investment_index_calculate('office_index.csv', 'office_sale.csv', 'office_rent.csv', 'index_new.csv', month)
	cal.save_table('office_index.csv', 'index_new.csv', month)
	month = arrow.get(month, 'YYYY-MM').shift(months=1).format('YYYY-MM')
'''

'''
while month != '2019-04':
	cal.investment_index_calculate('shop_index.csv', 'shop_sale.csv', 'shop_rent.csv', 'index_new.csv', month)
	cal.save_table('shop_index.csv', 'index_new.csv', month)
	month = arrow.get(month, 'YYYY-MM').shift(months=1).format('YYYY-MM')
'''

'''
while month != '2019-04':
	cal.sale_or_rent_index_calculate('office_sale_index.csv', 'office_sale.csv', 'index_new.csv', month)
	cal.save_table('office_sale_index.csv', 'index_new.csv', month)
	month = arrow.get(month, 'YYYY-MM').shift(months=1).format('YYYY-MM')
'''

'''
while month != '2019-04':
	cal.sale_or_rent_index_calculate('office_rent_index.csv', 'office_rent.csv', 'index_new.csv', month)
	cal.save_table('office_rent_index.csv', 'index_new.csv', month)
	month = arrow.get(month, 'YYYY-MM').shift(months=1).format('YYYY-MM')
'''

'''
while month != '2019-04':
	cal.sale_or_rent_index_calculate('shop_sale_index.csv', 'shop_sale.csv', 'index_new.csv', month)
	cal.save_table('shop_sale_index.csv', 'index_new.csv', month)
	month = arrow.get(month, 'YYYY-MM').shift(months=1).format('YYYY-MM')

while month != '2019-04':
	cal.sale_or_rent_index_calculate('shop_rent_index.csv', 'shop_rent.csv', 'index_new.csv', month)
	cal.save_table('shop_rent_index.csv', 'index_new.csv', month)
	month = arrow.get(month, 'YYYY-MM').shift(months=1).format('YYYY-MM')
'''