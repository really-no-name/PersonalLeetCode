#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3564.py
作者: Bolun Xu
创建日期: 2025/5/26
版本: 1.0
描述: Seasonal Sales Analysis。
"""
import pandas as pd


def seasonal_sales_analysis(products: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df_merge = sales.merge(products, how='left', on='product_id')
    # 判断季节
    def get_season(date):
        month = date.month
        if 3 <= month <= 5:
            return 'Spring'
        elif 6 <= month <= 8:
            return 'Summer'
        elif 9 <= month <= 11:
            return 'Fall'
        else:
            return 'Winter'

    df_merge['season'] = df_merge['sale_date'].apply(get_season)

    # 计算类别销量
    df_merge['total_revenue'] = df_merge['quantity'] * df_merge['price']
    df_grp = df_merge.groupby(['season', 'category']) \
        .agg({'quantity': 'sum',
              'total_revenue': 'sum'}).reset_index()

    # 按季节分组，然后在每个季节内按销量和收入排序
    df_sort = df_grp.sort_values(['season', 'quantity', 'total_revenue'], ascending=[True, False, False])

    # 保留每个季节销量最高的类别
    df_result = df_sort.drop_duplicates(subset=['season'], keep='first')
    df_result = df_result.rename(columns={'quantity': 'total_quantity'})
    return df_result


if __name__ == '__main__':
    data = [[1, 1, '2023-01-15', 5, 10.0], [2, 2, '2023-01-20', 4, 15.0], [3, 3, '2023-03-10', 3, 18.0],
            [4, 4, '2023-04-05', 1, 20.0], [5, 1, '2023-05-20', 2, 10.0], [6, 2, '2023-06-12', 4, 15.0],
            [7, 5, '2023-06-15', 5, 12.0], [8, 3, '2023-07-24', 2, 18.0], [9, 4, '2023-08-01', 5, 20.0],
            [10, 5, '2023-09-03', 3, 12.0], [11, 1, '2023-09-25', 6, 10.0], [12, 2, '2023-11-10', 4, 15.0],
            [13, 3, '2023-12-05', 6, 18.0], [14, 4, '2023-12-22', 3, 20.0], [15, 5, '2024-02-14', 2, 12.0]]
    sales = pd.DataFrame(data, columns=['sale_id', 'product_id', 'sale_date', 'quantity', 'price']).astype(
        {'sale_id': 'int64', 'product_id': 'int64', 'sale_date': 'datetime64[ns]', 'quantity': 'int64',
         'price': 'float64'})

    data = [[1, 'Warm Jacket', 'Apparel'], [2, 'Designer Jeans', 'Apparel'], [3, 'Cutting Board', 'Kitchen'],
            [4, 'Smart Speaker', 'Tech'], [5, 'Yoga Mat', 'Fitness']]
    products = pd.DataFrame(data, columns=['product_id', 'product_name', 'category']).astype(
        {'product_id': 'int64', 'product_name': 'string', 'category': 'string'})
    print(seasonal_sales_analysis(products, sales))