#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1193.py
作者: Bolun Xu
创建日期: 2025/5/21
版本: 1.0
描述: 每月交易 I。
"""
import pandas as pd


# def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
#     df = transactions.copy()
#     # 改为月份
#     df['month'] = df['trans_date'].dt.strftime('%Y-%m')
#     # 计算trans_count
#     df_grp1 = df.groupby(['month', 'country'], dropna=False)['id'].nunique().reset_index(name='trans_count')
#     df_grp2 = df.groupby(['month', 'country'], dropna=False)['amount'].sum().reset_index(name='trans_total_amount')
#     df_grp3 = df[df['state'] == 'approved'].groupby(['month', 'country'], dropna=False)['id'].nunique().reset_index(name='approved_count')
#     df_grp4 = df[df['state'] == 'approved'].groupby(['month', 'country'], dropna=False)['amount'].sum().reset_index(name='approved_total_amount')
#
#     # 链式合并
#     df_merge = df_grp1.merge(df_grp3, on=['month', 'country'], how='left')\
#         .merge(df_grp2, on=['month', 'country'], how='left') \
#         .merge(df_grp4, on=['month', 'country'], how='left').fillna(0)
#
#     return df_merge


# 由于测试用例存在'country'为空值
def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    # 首先将trans_date转换为年月格式
    transactions['month'] = transactions['trans_date'].dt.strftime('%Y-%m')

    # 确保country中的空值不会被groupby忽略
    transactions['country'] = transactions['country'].where(pd.notnull(transactions['country']), None)

    # 计算总交易数和总金额
    result = transactions.groupby(['month', 'country'], dropna=False).agg(
        trans_count=('id', 'count'),
        trans_total_amount=('amount', 'sum')
    ).reset_index()

    # 计算已批准的交易数和总金额
    approved = transactions[transactions['state'] == 'approved'].groupby(
        ['month', 'country'], dropna=False).agg(
        approved_count=('id', 'count'),
        approved_total_amount=('amount', 'sum')
    ).reset_index()

    # 合并结果
    result = result.merge(approved, on=['month', 'country'], how='left')

    # 处理NaN值（当某个月/国家没有approved交易时）
    result['approved_count'] = result['approved_count'].fillna(0).astype(int)
    result['approved_total_amount'] = result['approved_total_amount'].fillna(0).astype(int)

    # 确保country中的空值显示为NULL/None而不是NaN
    result['country'] = result['country'].where(pd.notnull(result['country']), None)

    # 按题目要求顺序返回列
    return result[['month', 'country', 'trans_count', 'approved_count',
                   'trans_total_amount', 'approved_total_amount']]


if __name__ == '__main__':
    data = [[121, 'US', 'approved', 1000, '2018-12-18'], [122, 'US', 'declined', 2000, '2018-12-19'],
            [123, 'US', 'approved', 2000, '2019-01-01'], [124, 'DE', 'approved', 2000, '2019-01-07']]
    transactions = pd.DataFrame(data, columns=['id', 'country', 'state', 'amount', 'trans_date']).astype(
        {'id': 'Int64', 'country': 'object', 'state': 'object', 'amount': 'Int64', 'trans_date': 'datetime64[ns]'})
    print(monthly_transactions(transactions))