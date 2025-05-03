#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2084.py
作者: Bolun Xu
创建日期: 2025/4/29
版本: 1.0
描述: 为订单类型为 0 的客户删除类型为 1 的订单。
"""
import pandas as pd


def drop_specific_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # 步骤1：找出有类型0订单的客户
    customers_with_type0 = orders[orders['order_type'] == 0]['customer_id'].unique()

    # 步骤2：筛选数据
    # 条件1：订单类型为0
    # 条件2：或者客户不在有类型0订单的客户列表中（即只保留类型1订单）
    filtered_orders = orders[
        (orders['order_type'] == 0) |
        (~orders['customer_id'].isin(customers_with_type0))
        ]

    # 步骤3：按任意顺序输出结果（这里保持原顺序）
    result = filtered_orders[['order_id', 'customer_id', 'order_type']]
    return result


if __name__ == '__main__':
    data = [[1, 1, 0], [2, 1, 0], [11, 2, 0], [12, 2, 1], [21, 3, 1], [22, 3, 0], [31, 4, 1], [32, 4, 1]]
    orders = pd.DataFrame(data, columns=['order_id', 'customer_id', 'order_type']).astype(
        {'order_id': 'Int64', 'customer_id': 'Int64', 'order_type': 'Int64'})
    print(drop_specific_orders(orders))