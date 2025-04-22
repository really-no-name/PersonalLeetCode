#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1251.py
作者: Bolun Xu
创建日期: 2025/4/22
版本: 1.0
描述: 平均售价。
"""
import pandas as pd


def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    # 合并
    # merge_df = pd.merge(prices, units_sold, how='cross')  # 笛卡尔积
    # # print(merge_df)
    # merge_df = merge_df[
    #     (merge_df['purchase_date'] >= merge_df['start_date']) &
    #     (merge_df['purchase_date'] <= merge_df['end_date']) &
    #     (merge_df['product_id_y'] == merge_df['product_id_x'])
    #     ]

    # del merge_df['product_id_y']
    # merge_df = merge_df.rename(columns={'product_id_x': 'product_id'})

    merge_df = pd.merge(prices, units_sold, how='left', on='product_id')
    print(merge_df)
    merge_df = merge_df[(merge_df['purchase_date'] >= merge_df['start_date']) & (merge_df['purchase_date'] <= merge_df['end_date'])]

    merge_df['total_price'] = merge_df['price'] * merge_df['units']
    total = merge_df.groupby('product_id')[['units', 'total_price']].sum().reset_index()  # 分组求和
    total['average_price'] = (total['total_price'] / total['units']).round(2)

    all_products = prices['product_id'].unique()
    res = pd.DataFrame(all_products, columns=['product_id'])
    result = res.merge(total, on='product_id', how='left').fillna(0)

    return result[['product_id', 'average_price']]

    # merge_df = prices.merge(units_sold, on='product_id', how='left')
    # merge_df = merge_df[
    #     (merge_df['purchase_date'] >= merge_df['start_date']) &
    #     (merge_df['purchase_date'] <= merge_df['end_date'])
    #     ]
    #
    # # 计算每个 product_id 的总销售额（units × price）
    # merge_df['total_sales'] = merge_df['units'] * merge_df['price']
    #
    # # 计算每个 product_id 的总 units 和总销售额
    # grouped = merge_df.groupby('product_id').agg(
    #     total_units=('units', 'sum'),
    #     total_sales=('total_sales', 'sum')
    # )
    #
    # # 计算平均售价
    # grouped['average_price'] = (grouped['total_sales'] / grouped['total_units']).round(2)
    #
    # # 重置索引并返回结果
    # result = grouped.reset_index()[['product_id', 'average_price']]
    #
    # all_products = prices['product_id'].unique()
    # res = pd.DataFrame(all_products, columns=['product_id'])
    # return res.merge(result, on='product_id', how='left').fillna(0)


if __name__ == '__main__':
    # data = [[1, '2019-02-17', '2019-02-28', 5], [1, '2019-03-01', '2019-03-22', 20],
    #         [2, '2019-02-01', '2019-02-20', 15], [2, '2019-02-21', '2019-03-31', 30]]
    # prices = pd.DataFrame(data, columns=['product_id', 'start_date', 'end_date', 'price']).astype(
    #     {'product_id': 'Int64', 'start_date': 'datetime64[ns]', 'end_date': 'datetime64[ns]', 'price': 'Int64'})
    # data = [[1, '2019-02-25', 100], [1, '2019-03-01', 15], [2, '2019-02-10', 200], [2, '2019-03-22', 30]]
    # units_sold = pd.DataFrame(data, columns=['product_id', 'purchase_date', 'units']).astype(
    #     {'product_id': 'Int64', 'purchase_date': 'datetime64[ns]', 'units': 'Int64'})
    # print(average_selling_price(prices, units_sold))


    data = [[1, '2023-01-01', '2023-01-31', 10], [2, '2023-01-01', '2023-01-31', 20]]
    prices = pd.DataFrame(data, columns=['product_id', 'start_date', 'end_date', 'price']).astype(
        {'product_id': 'Int64', 'start_date': 'datetime64[ns]', 'end_date': 'datetime64[ns]', 'price': 'Int64'})
    data = []
    units_sold = pd.DataFrame(data, columns=['product_id', 'purchase_date', 'units']).astype(
        {'product_id': 'Int64', 'purchase_date': 'datetime64[ns]', 'units': 'Int64'})
    print(average_selling_price(prices, units_sold))