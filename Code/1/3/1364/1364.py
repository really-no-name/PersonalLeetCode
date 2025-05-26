#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1364.py
作者: Bolun Xu
创建日期: 2025/5/26
版本: 1.0
描述: 顾客的可信联系人数量。
"""
import pandas as pd


def count_trusted_contacts(customers: pd.DataFrame, contacts: pd.DataFrame, invoices: pd.DataFrame) -> pd.DataFrame:
    # 根据 invoice_id 查找 customer_name 和 price
    df_merge = invoices.merge(customers, left_on='user_id', right_on='customer_id', how='left')


    # 统计 联系人数量
    df_contacts = contacts.copy()
    df_contacts_grp = df_contacts.groupby('user_id')['contact_name'].count().reset_index(name='contacts_cnt')
    df_merge = df_merge.merge(df_contacts_grp, on='user_id', how='left').fillna(0)

    # 判断可信联系人
    df_contacts_filter = contacts[contacts['contact_name'].isin(customers['customer_name'])]
    df_contacts_grp2 = df_contacts_filter.groupby('user_id')['contact_name'].count().reset_index(name='trusted_contacts_cnt')
    df_merge = df_merge.merge(df_contacts_grp2, on='user_id', how='left').fillna(0)

    # 结果
    df_result = df_merge[['invoice_id', 'customer_name', 'price', 'contacts_cnt', 'trusted_contacts_cnt']]
    df_result = df_result.sort_values(by='invoice_id', ascending=True)
    return df_result


if __name__ == '__main__':
    data = [[1, 'Alice', 'alice@leetcode.com'], [2, 'Bob', 'bob@leetcode.com'], [13, 'John', 'john@leetcode.com'],
            [6, 'Alex', 'alex@leetcode.com']]
    customers = pd.DataFrame(data, columns=['customer_id', 'customer_name', 'email']).astype(
        {'customer_id': 'Int64', 'customer_name': 'object', 'email': 'object'})
    data = [[1, 'Bob', 'bob@leetcode.com'], [1, 'John', 'john@leetcode.com'], [1, 'Jal', 'jal@leetcode.com'],
            [2, 'Omar', 'omar@leetcode.com'], [2, 'Meir', 'meir@leetcode.com'], [6, 'Alice', 'alice@leetcode.com']]
    contacts = pd.DataFrame(data, columns=['user_id', 'contact_name', 'contact_email']).astype(
        {'user_id': 'Int64', 'contact_name': 'object', 'contact_email': 'object'})
    data = [[77, 100, 1], [88, 200, 1], [99, 300, 2], [66, 400, 2], [55, 500, 13], [44, 60, 6]]
    invoices = pd.DataFrame(data, columns=['invoice_id', 'price', 'user_id']).astype(
        {'invoice_id': 'Int64', 'price': 'Int64', 'user_id': 'Int64'})
    print(count_trusted_contacts(customers, contacts, invoices))