#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1393.py
作者: Bolun Xu
创建日期: 2025/4/29
版本: 1.0
描述: 股票的资本损益。
"""
import pandas as pd


def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    stocks['spend'] = stocks['price']  # 先默认 spend = price
    stocks.loc[stocks['operation'] == 'Buy', 'spend'] = -stocks['price']  # 对 Buy 操作取负
    result = stocks.groupby('stock_name')['spend'].sum().reset_index()
    result = result.rename(columns={'spend': 'capital_gain_loss'})
    return result


if __name__ == '__main__':
    data = [['Leetcode', 'Buy', 1, 1000], ['Corona Masks', 'Buy', 2, 10], ['Leetcode', 'Sell', 5, 9000],
            ['Handbags', 'Buy', 17, 30000], ['Corona Masks', 'Sell', 3, 1010], ['Corona Masks', 'Buy', 4, 1000],
            ['Corona Masks', 'Sell', 5, 500], ['Corona Masks', 'Buy', 6, 1000], ['Handbags', 'Sell', 29, 7000],
            ['Corona Masks', 'Sell', 10, 10000]]
    stocks = pd.DataFrame(data, columns=['stock_name', 'operation', 'operation_day', 'price']).astype(
        {'stock_name': 'object', 'operation': 'object', 'operation_day': 'Int64', 'price': 'Int64'})
    print(capital_gainloss(stocks))