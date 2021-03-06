import pandas as pd
import numpy as np
import arrow

def save_table(old_file, new_file, this_month):
    
    df = pd.read_csv(old_file, index_col='city')
    df1 = pd.read_csv(new_file, index_col='city')
    
    df[this_month] = df1

    df.to_csv(old_file)


def investment_index_calculate(index_file, sale_file, rent_file, save_file, this_month):
    
    last_month = arrow.get(this_month,'YYYY-MM').shift(months=-1).format('YYYY-MM')

    df = pd.read_csv(index_file, usecols=['city', last_month])
    df2 = pd.read_csv(sale_file, usecols=['city', last_month, this_month])
    df2.rename(columns={this_month: "sale"+this_month, last_month: "sale"+last_month}, inplace=True)
    df3 = pd.read_csv(rent_file, usecols=['city', this_month])
    df3.rename(columns={this_month: "rent"}, inplace=True)

    # 合并
    merged = pd.merge(df, df2, on='city')
    merged = pd.merge(merged, df3, on='city')

    # 计算
    merged[this_month] = ((merged['sale'+this_month]+merged['rent'])/merged['sale'+last_month])*merged[last_month]
    merged[this_month] = merged[this_month].apply(lambda x: '{:.2f}'.format(x))

    # 保存
    merged.to_csv(save_file, columns=['city', this_month], index=False)


def sale_or_rent_index_calculate(index_file, sale_file, save_file, this_month):
    
    last_month = arrow.get(this_month,'YYYY-MM').shift(months=-1).format('YYYY-MM')

    df = pd.read_csv(index_file, usecols=['city', last_month])
    df2 = pd.read_csv(sale_file, usecols=['city', last_month, this_month])
    df2.rename(columns={this_month: "sale"+this_month, last_month: "sale"+last_month}, inplace=True)

    # 合并
    merged = pd.merge(df, df2, on='city')

    # 计算
    merged[this_month] = (merged['sale'+this_month]/merged['sale'+last_month])*merged[last_month]
    merged[this_month] = merged[this_month].apply(lambda x: '{:.2f}'.format(x))

    # 保存
    merged.to_csv(save_file, columns=['city', this_month], index=False)


def index_rate(index_file, save_file, this_month):

	one_year_ago = arrow.get(this_month, 'YYYY-MM').shift(years=-1).format('YYYY-MM')
	three_year_ago = arrow.get(this_month, 'YYYY-MM').shift(years=-3).format('YYYY-MM')
	five_year_ago = arrow.get(this_month, 'YYYY-MM').shift(years=-5).format('YYYY-MM')

	df = pd.read_csv(index_file, usecols=['city', this_month, one_year_ago, three_year_ago, five_year_ago])

	df['one_year_rate'] = df[this_month]/df[one_year_ago]-1
	df['three_year_rate'] = df[this_month]/df[three_year_ago]-1
	df['five_year_rate'] = df[this_month]/df[five_year_ago]-1

	df = df.dropna()

	df['one_year_rate'] = df['one_year_rate'].apply(lambda x: '{:.2%}'.format(x))
	df['three_year_rate'] = df['three_year_rate'].apply(lambda x: '{:.2%}'.format(x))
	df['five_year_rate'] = df['five_year_rate'].apply(lambda x: '{:.2%}'.format(x))
	
	df.to_csv(save_file, columns=['city', 'one_year_rate', 'three_year_rate', 'five_year_rate'], index=False)



