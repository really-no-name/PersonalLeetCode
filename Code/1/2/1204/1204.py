#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1204.py
作者: Bolun Xu
创建日期: 2025/5/21
版本: 1.0
描述: 最后一个能进入巴士的人。
"""
import pandas as pd


def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    df = queue.copy()
    # 根据上车顺序排序
    df_sort = df.sort_values(by=['turn'], ascending=True)
    # 累加
    df_sort['total-weight'] = df_sort['weight'].cumsum()
    # 排除(无法上巴士)
    df_filter = df_sort[df_sort['total-weight'] <= 1000]
    # 获取最后一个上车的人
    df_result = df_filter.tail(1)[['person_name']]
    return df_result


if __name__ == '__main__':
    data = [[5, 'Alice', 250, 1], [4, 'Bob', 175, 5], [3, 'Alex', 350, 2], [6, 'John Cena', 400, 3],
            [1, 'Winston', 500, 6], [2, 'Marie', 200, 4]]
    queue = pd.DataFrame(data, columns=['person_id', 'person_name', 'weight', 'turn']).astype(
        {'person_id': 'Int64', 'person_name': 'object', 'weight': 'Int64', 'turn': 'Int64'})
    print(last_passenger(queue))