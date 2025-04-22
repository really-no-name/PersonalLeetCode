#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1084.py
作者: Bolun Xu
创建日期: 2025/4/22
版本: 1.0
描述: 销售分析 III。
时间复杂度：
空间复杂度：
"""
import pandas as pd


def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    # 转换日期格式
    sales['sale_date'] = pd.to_datetime(sales['sale_date'])

    # 春季销售的产品
    spring = sales[
        (sales['sale_date'] >= '2019-01-01') &
        (sales['sale_date'] <= '2019-03-31')
        ]['product_id'].unique()

    # 非春季销售的产品
    non_spring = sales[
        (sales['sale_date'] < '2019-01-01') |
        (sales['sale_date'] > '2019-03-31')
        ]['product_id'].unique()

    # 仅在春季销售的产品
    exclusive_spring = set(spring) - set(non_spring)

    # 获取产品信息
    result = product[product['product_id'].isin(exclusive_spring)]

    return result[['product_id', 'product_name']]


if __name__ == '__main__':
    data = [[1, 'S8', 1000], [2, 'G4', 800], [3, 'iPhone', 1400]]
    product = pd.DataFrame(data, columns=['product_id', 'product_name', 'unit_price']).astype(
        {'product_id': 'Int64', 'product_name': 'object', 'unit_price': 'Int64'})
    data = [[1, 1, 1, '2019-01-21', 2, 2000], [1, 2, 2, '2019-02-17', 1, 800], [2, 2, 3, '2019-06-02', 1, 800],
            [3, 3, 4, '2019-05-13', 2, 2800]]
    sales = pd.DataFrame(data,
                         columns=['seller_id', 'product_id', 'buyer_id', 'sale_date', 'quantity', 'price']).astype(
        {'seller_id': 'Int64', 'product_id': 'Int64', 'buyer_id': 'Int64', 'sale_date': 'datetime64[ns]',
         'quantity': 'Int64', 'price': 'Int64'})
    print(sales_analysis(product, sales))