#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1571.py
作者: Bolun Xu
创建日期: 2025/5/8
版本: 1.0
描述: 仓库经理。
"""
import pandas as pd


def warehouse_manager(warehouse: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    products['Volumetric'] = products['Width'] * products['Height'] * products['Length']
    df_merge = pd.merge(warehouse, products, how='left', on='product_id')
    df_merge['total_V'] = df_merge['Volumetric'] * df_merge['units']
    df_sum = df_merge.groupby(['name'])['total_V'].sum().reset_index()
    df_result = df_sum.rename(columns={'name': 'warehouse_name', 'total_V': 'volume'})
    return df_result


if __name__ == '__main__':
    data = [['LCHouse1', 1, 1],
            ['LCHouse1', 2, 10],
            ['LCHouse1', 3, 5],
            ['LCHouse2', 1, 2],
            ['LCHouse2', 2, 2],
            ['LCHouse3', 4, 1]]
    warehouse = pd.DataFrame(data, columns=['name', 'product_id', 'units']).astype(
        {'name': 'object', 'product_id': 'Int64', 'units': 'Int64'})
    data = [[1, 'LC-TV', 5, 50, 40],
            [2, 'LC-KeyChain', 5, 5, 5],
            [3, 'LC-Phone', 2, 10, 10],
            [4, 'LC-T-Shirt', 4, 10, 20]]
    products = pd.DataFrame(data, columns=['product_id', 'product_name', 'Width', 'Length', 'Height']).astype(
        {'product_id': 'Int64', 'product_name': 'object', 'Width': 'Int64', 'Length': 'Int64', 'Height': 'Int64'})

    print(warehouse_manager(warehouse, products))