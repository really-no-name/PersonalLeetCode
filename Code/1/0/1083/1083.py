#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1083.py
作者: Bolun Xu
创建日期: 2025/5/12
版本: 1.0
描述: 销售分析 II。
"""
import pandas as pd


def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    # 将 Product 和 Sales 数据框合并，并按照 buyer_id 分组
    merged_data = pd.merge(product, sales, left_on='product_id', right_on='product_id')
    grouped_data = merged_data.groupby('buyer_id')

    # 计算每个买家购买 'S8' 的总数和 'iphone' 的总数
    product_counts = grouped_data['product_name'].value_counts().unstack(fill_value=0)

    # 筛选出购买 'S8' 但没有购买 'iphone' 的买家
    result = product_counts[(product_counts['S8'] > 0) & (product_counts['iPhone'] == 0)].reset_index()

    return result[['buyer_id']]


if __name__ == '__main__':
    data = [[1, 'S8', 1000],
            [2, 'G4', 800],
            [3, 'iPhone', 1400]]
    product = pd.DataFrame(data, columns=['product_id', 'product_name', 'unit_price']).astype(
        {'product_id': 'Int64', 'product_name': 'object', 'unit_price': 'Int64'})
    data = [[1, 1, 1, '2019-01-21', 2, 2000],
            [1, 2, 2, '2019-02-17', 1, 800],
            [2, 1, 3, '2019-06-02', 1, 800],
            [3, 3, 3, '2019-05-13', 2, 2800]]
    sales = pd.DataFrame(data,
                         columns=['seller_id', 'product_id', 'buyer_id', 'sale_date', 'quantity', 'price']).astype(
        {'seller_id': 'Int64', 'product_id': 'Int64', 'buyer_id': 'Int64', 'sale_date': 'datetime64[ns]',
         'quantity': 'Int64', 'price': 'Int64'})
    print(sales_analysis(product, sales))