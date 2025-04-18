#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2329.py
作者: Bolun Xu
创建日期: 2025/4/18
版本: 1.0
描述: 产品销售分析Ⅴ。
"""
import pandas as pd


def product_sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    # print(sales)
    # print(product)
    frame_a = sales.set_index('product_id').join(product.set_index('product_id'), how='inner')  # 表格拼接
    frame_a['spending'] = frame_a['price'] * frame_a['quantity']

    result = frame_a.groupby('user_id')['spending'].sum().reset_index()  # 根据user_id分组并汇总spending值
    return result.sort_values(by='spending', ascending=False)  # 排序


if __name__ == '__main__':
    sales = pd.read_csv('sales.csv')
    product = pd.read_csv('product.csv')
    print(product_sales_analysis(sales, product))