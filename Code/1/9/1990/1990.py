#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1990.py
作者: Bolun Xu
创建日期: 2025/6/2
版本: 1.0
描述: 统计实验的数量。
"""
import pandas as pd


def count_experiments(experiments: pd.DataFrame) -> pd.DataFrame:
    # 获取所有平台和实验名称的唯一值
    platforms = ['Android', 'IOS', 'Web']
    experiment_names = ['Reading', 'Sports', 'Programming']

    # 创建所有可能的组合
    cross_product = pd.MultiIndex.from_product([platforms, experiment_names],
                                               names=['platform', 'experiment_name']).to_frame(index=False)

    # 统计
    df_experiments = experiments.groupby(['platform', 'experiment_name'])['experiment_id'].nunique().reset_index(name='num_experiments')

    # 合并
    df_result = cross_product.merge(df_experiments, how='left', on=['platform', 'experiment_name']).fillna(0)
    return df_result


if __name__ == '__main__':
    data = [[4, 'IOS', 'Programming'], [13, 'IOS', 'Sports'], [14, 'Android', 'Reading'], [8, 'Web', 'Reading'],
            [12, 'Web', 'Reading'], [18, 'Web', 'Programming']]
    experiments = pd.DataFrame(data, columns=['experiment_id', 'platform', 'experiment_name']).astype(
        {'experiment_id': 'Int64', 'platform': 'object', 'experiment_name': 'object'})
    print(count_experiments(experiments))