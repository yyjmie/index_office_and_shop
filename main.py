import calculate as cal

this_month = '2018-01'

cal.investment_index_calculate('office_index.csv', 'office_sale.csv', 'office_rent.csv', 'index_new.csv', this_month)
cal.save_table('office_index.csv', 'index_new.csv', this_month)