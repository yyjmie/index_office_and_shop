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


