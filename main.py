import calculate as cal
import arrow

month = '2018-01'

# calculate office&&shop investment index from month to 2019-03
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

# calculate office sale&&rent index from month to 2019-03
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

# calculate shop sale&&rent index from month to 2019-03
'''
while month != '2019-04':
	cal.sale_or_rent_index_calculate('shop_sale_index.csv', 'shop_sale.csv', 'index_new.csv', month)
	cal.save_table('shop_sale_index.csv', 'index_new.csv', month)
	month = arrow.get(month, 'YYYY-MM').shift(months=1).format('YYYY-MM')
'''
'''
while month != '2019-04':
	cal.sale_or_rent_index_calculate('shop_rent_index.csv', 'shop_rent.csv', 'index_new.csv', month)
	cal.save_table('shop_rent_index.csv', 'index_new.csv', month)
	month = arrow.get(month, 'YYYY-MM').shift(months=1).format('YYYY-MM')
'''

# calculate investment index rate in month
'''
cal.index_rate('office_index.csv', 'office_index_rate_2018_03.csv', '2018-03')
cal.index_rate('office_index.csv', 'office_index_rate_2018_06.csv', '2018-06')
cal.index_rate('office_index.csv', 'office_index_rate_2018_09.csv', '2018-09')
cal.index_rate('office_index.csv', 'office_index_rate_2018_12.csv', '2018-12')
cal.index_rate('office_index.csv', 'office_index_rate_2019_03.csv', '2019-03')

cal.index_rate('shop_index.csv', 'shop_index_rate_2018_03.csv', '2018-03')
cal.index_rate('shop_index.csv', 'shop_index_rate_2018_06.csv', '2018-06')
cal.index_rate('shop_index.csv', 'shop_index_rate_2018_09.csv', '2018-09')
cal.index_rate('shop_index.csv', 'shop_index_rate_2018_12.csv', '2018-12')
cal.index_rate('shop_index.csv', 'shop_index_rate_2019_03.csv', '2019-03')
'''