#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1445.py
作者: Bolun Xu
创建日期: 2025/4/29
版本: 1.0
描述: 苹果和桔子。
"""
import pandas as pd


def apples_oranges(sales: pd.DataFrame) -> pd.DataFrame:
    apple_df = sales[sales['fruit'] == 'apples'].rename(columns={'fruit': 'type_apple'})
    orange_df = sales[sales['fruit'] == 'oranges'].rename(columns={'fruit': 'type_orange'})
    total_df = pd.merge(apple_df, orange_df, how='left', on='sale_date')
    total_df['diff'] = total_df['sold_num_x'] - total_df['sold_num_y']
    return total_df[['sale_date', 'diff']]


if __name__ == '__main__':
    data = [['2020-05-01', 'apples', 10], ['2020-05-01', 'oranges', 8], ['2020-05-02', 'apples', 15],
            ['2020-05-02', 'oranges', 15], ['2020-05-03', 'apples', 20], ['2020-05-03', 'oranges', 0],
            ['2020-05-04', 'apples', 15], ['2020-05-04', 'oranges', 16]]
    sales = pd.DataFrame(data, columns=['sale_date', 'fruit', 'sold_num']).astype(
        {'sale_date': 'datetime64[ns]', 'fruit': 'object', 'sold_num': 'Int64'})
    print(apples_oranges(sales))