#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1173.py
作者: Bolun Xu
创建日期: 2025/5/9
版本: 1.0
描述: 即时食物配送 I。
"""
import pandas as pd


def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    cnt_ontime = delivery[delivery['order_date'] == delivery['customer_pref_delivery_date']].shape[0]
    cnt_total = delivery.shape[0]
    result = pd.DataFrame({'immediate_percentage': [round(cnt_ontime / cnt_total * 100, 2)]})
    return result


if __name__ == '__main__':
    data = [[1, 1, '2019-08-01', '2019-08-02'],
            [2, 5, '2019-08-02', '2019-08-02'],
            [3, 1, '2019-08-11', '2019-08-11'],
            [4, 3, '2019-08-24', '2019-08-26'],
            [5, 4, '2019-08-21', '2019-08-22'],
            [6, 2, '2019-08-11', '2019-08-13']]
    delivery = pd.DataFrame(data,
                            columns=['delivery_id', 'customer_id', 'order_date', 'customer_pref_delivery_date']).astype(
        {'delivery_id': 'Int64',
         'customer_id': 'Int64',
         'order_date': 'datetime64[ns]',
         'customer_pref_delivery_date': 'datetime64[ns]'})
    print(food_delivery(delivery))