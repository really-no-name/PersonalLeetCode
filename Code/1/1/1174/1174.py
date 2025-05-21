#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1174.py
作者: Bolun Xu
创建日期: 2025/5/21
版本: 1.0
描述: 即时食物配送 II。
"""
import pandas as pd


def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    df = delivery.copy()
    # 分类即时和计划
    df['time_type'] = df.apply(
        lambda row: 'immediate' if row['order_date'] == row['customer_pref_delivery_date'] else 'scheduled',
        axis=1)

    # 筛选首次订单
    df_sort = df.sort_values('order_date', ascending=True)
    df_filter = df_sort.drop_duplicates(subset=['customer_id'], keep='first')

    # 计算
    first_cnt = df_filter.shape[0]
    immediate_cnt = df_filter[df_filter['time_type'] == 'immediate'].shape[0]
    return pd.DataFrame({'immediate_percentage': [round(immediate_cnt / first_cnt * 100, 2)]})


if __name__ == '__main__':
    data = [[1, 1, '2019-08-01', '2019-08-02'], [2, 2, '2019-08-02', '2019-08-02'], [3, 1, '2019-08-11', '2019-08-12'],
            [4, 3, '2019-08-24', '2019-08-24'], [5, 3, '2019-08-21', '2019-08-22'], [6, 2, '2019-08-11', '2019-08-13'],
            [7, 4, '2019-08-09', '2019-08-09']]
    delivery = pd.DataFrame(data,
                            columns=['delivery_id', 'customer_id', 'order_date', 'customer_pref_delivery_date']).astype(
        {'delivery_id': 'Int64', 'customer_id': 'Int64', 'order_date': 'datetime64[ns]',
         'customer_pref_delivery_date': 'datetime64[ns]'})
    print(immediate_food_delivery(delivery))