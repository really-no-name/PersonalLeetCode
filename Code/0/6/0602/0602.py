#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0602.py
作者: Bolun Xu
创建日期: 2025/5/18
版本: 1.0
描述: 好友申请 II ：谁有最多的好友。
"""
import pandas as pd


def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    df_grp1 = request_accepted.groupby('requester_id')['accepter_id'].nunique().reset_index()
    df_grp1 = df_grp1.rename(columns={'requester_id': 'id', 'accepter_id': 'accept'})
    df_grp2 = request_accepted.groupby('accepter_id')['requester_id'].nunique().reset_index()
    df_grp2 = df_grp2.rename(columns={'accepter_id': 'id', 'requester_id': 'request'})
    df_merge = pd.merge(df_grp1, df_grp2, on='id', how='outer').fillna(0)
    df_merge['num'] = df_merge['accept'] + df_merge['request']
    df_filter = df_merge[df_merge['num'] == df_merge['num'].max()]
    return df_filter[['id', 'num']]


if __name__ == '__main__':
    data = [[1, 2, '2016/06/03'], [1, 3, '2016/06/08'], [2, 3, '2016/06/08'], [3, 4, '2016/06/09']]
    request_accepted = pd.DataFrame(data, columns=['requester_id', 'accepter_id', 'accept_date']).astype(
        {'requester_id': 'Int64', 'accepter_id': 'Int64', 'accept_date': 'datetime64[ns]'})
    print(most_friends(request_accepted))