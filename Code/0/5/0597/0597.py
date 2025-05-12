#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0597.py
作者: Bolun Xu
创建日期: 2025/5/12
版本: 1.0
描述: 好友申请 I：总体通过率。
"""
import pandas as pd


def acceptance_rate(friend_request: pd.DataFrame, request_accepted: pd.DataFrame) -> pd.DataFrame:
    friend_request = friend_request.drop_duplicates(subset=['sender_id', 'send_to_id'], keep='first')
    request_accepted = request_accepted.drop_duplicates(subset=['requester_id', 'accepter_id'], keep='first')
    request_cnt = friend_request.shape[0]
    accepted_cnt = request_accepted.shape[0]
    if request_cnt == 0:
        return pd.DataFrame({'accept_rate': [0]})
    else:
        df = pd.DataFrame({'accept_rate': [round(accepted_cnt / request_cnt, 2)]})
        return df


if __name__ == '__main__':
    data = [[1, 2, '2016/06/01'],
            [1, 3, '2016/06/01'],
            [1, 4, '2016/06/01'],
            [2, 3, '2016/06/02'],
            [3, 4, '2016/06/09']]
    friend_request = pd.DataFrame(data, columns=['sender_id', 'send_to_id', 'request_date']).astype(
        {'sender_id': 'Int64', 'send_to_id': 'Int64', 'request_date': 'datetime64[ns]'})
    data = [[1, 2, '2016/06/03'],
            [1, 3, '2016/06/08'],
            [2, 3, '2016/06/08'],
            [3, 4, '2016/06/09'],
            [3, 4, '2016/06/10']]
    request_accepted = pd.DataFrame(data, columns=['requester_id', 'accepter_id', 'accept_date']).astype(
        {'requester_id': 'Int64', 'accepter_id': 'Int64', 'accept_date': 'datetime64[ns]'})
    print(acceptance_rate(friend_request, request_accepted))