#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1543.py
作者: Bolun Xu
创建日期: 2025/5/17
版本: 1.0
描述: 产品名称格式修复。
"""
import pandas as pd


def fix_name_format(sales: pd.DataFrame) -> pd.DataFrame:
    # product_name 是小写字母且不包含前后空格
    sales['product_name'] = sales['product_name'].str.lower().str.strip()
    # sale_date 格式为 ('YYYY-MM')
    sales['sale_date'] = sales['sale_date'].dt.strftime("%Y-%m")

    df_grp = sales.groupby(['product_name', 'sale_date'])['sale_id'].count().reset_index(name='total')
    df_sort = df_grp.sort_values(['product_name', 'sale_date'], ascending=[True, True])
    return df_sort


if __name__ == '__main__':
    data = [[1, ' LCPHONE', '2000-01-16'],
            [2, 'LCPhone', '2000-01-17'],
            [3, 'LcPhOnE', '2000-02-18'],
            [4, 'LCKeyCHAiN', '2000-02-19'],
            [5, 'LCKeyChain', '2000-02-28'],
            [6, 'Matryoshka', '2000-03-31']]
    sales = pd.DataFrame(data, columns=['sale_id', 'product_name', 'sale_date']).astype(
        {'sale_id': 'Int64', 'product_name': 'object', 'sale_date': 'datetime64[ns]'})
    print(fix_name_format(sales))