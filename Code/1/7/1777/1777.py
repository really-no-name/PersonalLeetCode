#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1777.py
作者: Bolun Xu
创建日期: 2025/5/9
版本: 1.0
描述: 每家商店的产品价格。
"""
import pandas as pd


def products_price(products: pd.DataFrame) -> pd.DataFrame:
    return 1


if __name__ == '__main__':
    data = [['0', 'store1', '95'], ['0', 'store3', '105'], ['0', 'store2', '100'], ['1', 'store1', '70'],
            ['1', 'store3', '80']]
    products = pd.DataFrame(data, columns=['product_id', 'store', 'price']).astype(
        {'product_id': 'Int64', 'store': 'category', 'price': 'Int64'})
    print(products_price(products))