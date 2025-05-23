#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1164.py
作者: Bolun Xu
创建日期: 2025/5/21
版本: 1.0
描述: 指定日期的产品价格。
"""
import pandas as pd


def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    df_total_id = products[['product_id']].drop_duplicates(keep='first')

    # 筛选至'2019-08-16'
    df_filter = products[products['change_date'] <= '2019-08-16']

    # 获取最后的价格
    df_sort = df_filter.sort_values(by=['product_id', 'change_date'], ascending=[True, False])
    df_drop = df_sort.drop_duplicates(subset=['product_id'], keep='first')

    # 合并，无更改默认初始值10
    df_merge = df_total_id.merge(df_drop, on='product_id', how='left').fillna(10)
    df_merge = df_merge.rename(columns={'new_price': 'price'})
    return df_merge[['product_id', 'price']]


if __name__ == '__main__':
    data = [[1, 20, '2019-08-14'], [2, 50, '2019-08-14'], [1, 30, '2019-08-15'], [1, 35, '2019-08-16'],
            [2, 65, '2019-08-17'], [3, 20, '2019-08-18']]
    products = pd.DataFrame(data, columns=['product_id', 'new_price', 'change_date']).astype(
        {'product_id': 'Int64', 'new_price': 'Int64', 'change_date': 'datetime64[ns]'})
    products = price_at_given_date(products)