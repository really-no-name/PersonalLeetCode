#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1484.py
作者: Bolun Xu
创建日期: 2025/4/22
版本: 1.0
描述: 按日期分组销售产品。
"""
import pandas as pd


def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    # 按 sell_date 分组
    grouped = activities.groupby('sell_date')

    # 计算每个日期的唯一产品数量
    num_sold = grouped['product'].nunique().reset_index()
    num_sold.columns = ['sell_date', 'num_sold']

    # 获取每个日期的产品列表（已排序并去重）
    products = grouped['product'].apply(lambda x: ','.join(sorted(set(x)))).reset_index()
    products.columns = ['sell_date', 'products']

    # 合并两个结果
    result = pd.merge(num_sold, products, on='sell_date')

    # 按 sell_date 排序
    result = result.sort_values('sell_date')

    return result


if __name__ == '__main__':
    data = [['2020-05-30', 'Headphone'], ['2020-06-01', 'Pencil'], ['2020-06-02', 'Mask'], ['2020-05-30', 'Basketball'],
            ['2020-06-01', 'Bible'], ['2020-06-02', 'Mask'], ['2020-05-30', 'T-Shirt']]
    activities = pd.DataFrame(data, columns=['sell_date', 'product']).astype(
        {'sell_date': 'datetime64[ns]', 'product': 'object'})
    print(categorize_products(activities))