#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2985.py
作者: Bolun Xu
创建日期: 2025/3/19
版本: 1.0
描述: 计算订单平均商品数量。
"""
import pandas as pd


def compressed_mean(orders: pd.DataFrame) -> pd.DataFrame:
    # 计算总商品数
    total_items = (orders['item_count'] * orders['order_occurrences']).sum()

    # 计算总订单数
    total_orders = orders['order_occurrences'].sum()

    # 计算平均商品数量，保留两位小数
    average_items_per_order = round(total_items / total_orders, 2)

    # 将结果保存为 DataFrame
    result_df = pd.DataFrame({
        'average_items_per_order': [average_items_per_order]
    })

    return result_df


if __name__ == '__main__':
    # 假设 Orders 表已经加载到一个 DataFrame 中
    data = {
        'order_id': [10, 11, 12, 13],
        'item_count': [1, 2, 3, 4],
        'order_occurrences': [500, 1000, 800, 1000]
    }

    df = pd.DataFrame(data)
    print(compressed_mean(df))