#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1070.py
作者: Bolun Xu
创建日期: 2025/5/20
版本: 1.0
描述: 产品销售分析 III。
"""
import pandas as pd


def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    """
    选出每个售出过的产品第一年销售的产品id、年份、数量和价格。
    """
    # 找到每个product_id的最小年份
    first_years = sales.groupby('product_id')['year'].min().reset_index()

    # 合并回原始数据获取完整记录
    result = pd.merge(sales, first_years, on=['product_id', 'year'])

    return result[['product_id', 'year', 'quantity', 'price']].rename(columns={'year': 'first_year'})


if __name__ == '__main__':
    data = [[1, 100, 2008, 10, 5000], [2, 100, 2009, 12, 5000], [7, 200, 2011, 15, 9000]]
    sales = pd.DataFrame(data, columns=['sale_id', 'product_id', 'year', 'quantity', 'price']).astype(
        {'sale_id': 'Int64', 'product_id': 'Int64', 'year': 'Int64', 'quantity': 'Int64', 'price': 'Int64'})
    data = [[100, 'Nokia'], [200, 'Apple'], [300, 'Samsung']]
    product = pd.DataFrame(data, columns=['product_id', 'product_name']).astype(
        {'product_id': 'Int64', 'product_name': 'object'})
    print(sales_analysis(sales, product))