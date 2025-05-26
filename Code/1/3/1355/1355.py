#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1355.py
作者: Bolun Xu
创建日期: 2025/5/26
版本: 1.0
描述: 活动参与者。
"""
import pandas as pd


def activity_participants(friends: pd.DataFrame, activities: pd.DataFrame) -> pd.DataFrame:
    df_grp = friends.groupby('activity')['name'].count().reset_index()
    df_grp['rank'] = df_grp['name'].rank(method='dense', ascending=False)

    df_filter = df_grp[(df_grp['rank'] != 1) & (df_grp['rank'] != df_grp['rank'].max())]
    return df_filter[['activity']]


if __name__ == '__main__':
    # data = [[1, 'Jonathan D.', 'Eating'], [2, 'Jade W.', 'Singing'], [3, 'Victor J.', 'Singing'],
    #         [4, 'Elvis Q.', 'Eating'], [5, 'Daniel A.', 'Eating'], [6, 'Bob B.', 'Horse Riding']]
    # friends = pd.DataFrame(data, columns=['id', 'name', 'activity']).astype(
    #     {'id': 'Int64', 'name': 'object', 'activity': 'object'})
    # data = [[1, 'Eating'], [2, 'Singing'], [3, 'Horse Riding']]
    # activities = pd.DataFrame(data, columns=['id', 'name']).astype({'id': 'Int64', 'name': 'object'})
    # print(activity_participants(friends, activities))

    data = [[1, 'Maria C.', 'Dancing'],
            [2, 'Jade W.', 'Eating'],
            [3, 'Jonathan D.', 'Singing'],
            [4, 'Claire C.', 'Walking'],
            [5, 'Will W.', 'Horse Riding'],
            [6, 'Anna A.', 'Singing'],
            [7, 'Daniel D.', 'Horse Riding'],
            [8, 'Jonathan D.', 'Singing'],
            [9, 'Stella S.', 'Swimming'],
            [10, 'Winston W.', 'Walking'],
            [11, 'Elvis E.', 'Horse Riding'],
            [12, 'Timmy T.', 'Horse Riding'],
            [13, 'Rose R.', 'Reading'],
            [14, 'Monica M.', 'Playing'],
            [15, 'Selena G.', 'Swimming'],
            [16, 'Nicola T.', 'Singing'],
            [17, 'Albert E.', 'Singing'],
            [18, 'Isaac N.', 'Swimming']]
    friends = pd.DataFrame(data, columns=['id', 'name', 'activity']).astype(
        {'id': 'Int64', 'name': 'object', 'activity': 'object'})
    data = [[1, 'Eating'],
            [2, 'Singing'],
            [3, 'Horse Riding'],
            [4, 'Dancing'],
            [5, 'Reading'],
            [6, 'Playing'],
            [7, 'Swimming'],
            [8, 'Walking']]
    activities = pd.DataFrame(data, columns=['id', 'name']).astype({'id': 'Int64', 'name': 'object'})
    print(activity_participants(friends, activities))