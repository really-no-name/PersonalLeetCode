#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1407.py
作者: Bolun Xu
创建日期: 2025/3/18
版本: 1.0
描述: 排名靠前的旅行者。
时间复杂度：
空间复杂度：
"""
import pandas as pd


def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    # 左连接 Users 和 Rides 表
    merged_df = pd.merge(users, rides, left_on='id', right_on='user_id', how='left')
    # 当使用 pd.merge 时，如果两个表中有相同的列名（例如 id），默认情况下，merge 会为这些列添加后缀（_x 和 _y）。
    # 检查合并后的列名
    # print("合并后的列名:", merged_df.columns.tolist())

    # 确保使用正确的列名进行分组
    # 如果 'id' 列被重命名为 'id_x'，则需要使用 'id_x'
    groupby_columns = ['id_x', 'name'] if 'id_x' in merged_df.columns else ['id', 'name']

    # 计算每个用户的总旅行距离
    travelled_distance = merged_df.groupby(groupby_columns, as_index=False)['distance'].sum()

    # 将没有行程的用户的距离设置为 0
    travelled_distance['distance'] = travelled_distance['distance'].fillna(0)

    # 重命名列
    travelled_distance.rename(columns={'distance': 'travelled_distance'}, inplace=True)

    # 按照 travelled_distance 降序排列，如果距离相同，则按照 name 升序排列
    result = travelled_distance.sort_values(by=['travelled_distance', 'name'], ascending=[False, True])

    # 选择需要的列
    result = result[['name', 'travelled_distance']]
    return result


if __name__ == '__main__':
    # 示例数据
    users = {
        'id': [1, 2, 3, 4, 7, 13, 19],
        'name': ['Alice', 'Bob', 'Alex', 'Donald', 'Lee', 'Jonathan', 'Elvis']
    }

    rides = {
        'id': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'user_id': [1, 2, 3, 7, 13, 19, 7, 19, 7],
        'distance': [120, 317, 222, 100, 312, 50, 120, 400, 230]
    }
    result = top_travellers(pd.DataFrame(users), pd.DataFrame(rides))
    print(result)
