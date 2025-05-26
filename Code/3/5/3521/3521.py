#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3521.py
作者: Bolun Xu
创建日期: 2025/5/26
版本: 1.0
描述: 查找推荐产品对。
"""
import pandas as pd


def find_product_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
    # 统计每种商品的购买者
    df_pp_grp = product_purchases.groupby('product_id')['user_id'].unique().reset_index()

    # 筛选 至少有 3 位不同的 客户同时购买了这两种产品
    df_pp_merge = pd.merge(df_pp_grp, df_pp_grp, how='cross')
    df_pp_merge = df_pp_merge[df_pp_merge['product_id_x'] < df_pp_merge['product_id_y']]
    df_pp_merge['customer_count'] = df_pp_merge.apply(
        lambda row: len(set(row['user_id_x']) & set(row['user_id_y'])),
        axis=1
        )
    df_pp_filter = df_pp_merge[df_pp_merge['customer_count'] >= 3]

    # 合并
    df_pp = df_pp_filter[['product_id_x', 'product_id_y', 'customer_count']] \
        .rename(columns={'product_id_x': 'product1_id', 'product_id_y': 'product2_id'})
    df_merge = df_pp.merge(product_info, how='left', left_on='product1_id', right_on='product_id')
    df_merge = df_merge.merge(product_info, how='left', left_on='product2_id', right_on='product_id')
    df_merge = df_merge.rename(columns={'category_x': 'product1_category', 'category_y': 'product2_category'})
    df_sort = df_merge.sort_values(['customer_count', 'product1_id', 'product2_id'], ascending=[False, True, True])
    df_result = df_sort[['product1_id', 'product2_id', 'product1_category', 'product2_category', 'customer_count']]
    return df_result


if __name__ == '__main__':
    data = [[1, 101, 2], [1, 102, 1], [1, 103, 3], [2, 101, 1], [2, 102, 5], [2, 104, 1], [3, 101, 2], [3, 103, 1],
            [3, 105, 4], [4, 101, 1], [4, 102, 1], [4, 103, 2], [4, 104, 3], [5, 102, 2], [5, 104, 1]]
    product_purchases = pd.DataFrame(data, columns=['user_id', 'product_id', 'quantity']).astype({
        'user_id': 'int64', 'product_id': 'int64', 'quantity': 'int64'
    })
    data = [[101, 'Electronics', 100], [102, 'Books', 20], [103, 'Clothing', 35], [104, 'Kitchen', 50],
            [105, 'Sports', 75]]
    product_info = pd.DataFrame(data, columns=['product_id', 'category', 'price']).astype({
        'product_id': 'int64', 'category': 'string', 'price': 'float64'
    })
    print(find_product_recommendation_pairs(product_purchases, product_info))
