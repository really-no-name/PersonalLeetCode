#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0608.py
作者: Bolun Xu
创建日期: 2025/5/19
版本: 1.0
描述: 树节点。
"""
import pandas as pd

def node_type(row, all_parent_ids):
    if pd.isna(row['p_id']):
        return 'Root'
    elif row['id'] in all_parent_ids:
        return 'Inner'
    else:
        return 'Leaf'

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    all_parent_ids = set(tree['p_id'].dropna().unique())
    tree['type'] = tree.apply(lambda row: node_type(row, all_parent_ids), axis=1)
    return tree[['id', 'type']]



if __name__ == '__main__':
    data = [[1, None], [2, 1], [3, 1], [4, 2], [5, 2]]
    tree = pd.DataFrame(data, columns=['id', 'p_id']).astype({'id': 'Int64', 'p_id': 'Int64'})
    print(tree_node(tree))