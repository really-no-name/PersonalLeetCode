#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1440.py
作者: Bolun Xu
创建日期: 2025/5/26
版本: 1.0
描述: 计算布尔表达式的值。
"""
import pandas as pd


def eval_expression(variables: pd.DataFrame, expressions: pd.DataFrame) -> pd.DataFrame:
    df_expressions = expressions.copy()

    # 确保返回的 DataFrame 包含 'value' 列，即使 expressions 是空的
    if df_expressions.empty:
        df_expressions['value'] = []
        return df_expressions

    def check(row):
        left = variables.loc[variables["name"] == row['left_operand'], "value"].values[0]
        right = variables.loc[variables["name"] == row['right_operand'], "value"].values[0]
        if row['operator'] == '=':
            return 'true' if left == right else 'false'
        elif row['operator'] == '<':
            return 'true' if left < right else 'false'
        elif row['operator'] == '>':
            return 'true' if left > right else 'false'
        return None

    df_expressions['value'] = df_expressions.apply(check, axis=1)
    return df_expressions


if __name__ == '__main__':
    data = [['x', 66], ['y', 77]]
    variables = pd.DataFrame(data, columns=['name', 'value']).astype({'name': 'object', 'value': 'Int64'})
    data = [['x', '>', 'y'], ['x', '<', 'y'], ['x', '=', 'y'], ['y', '>', 'x'], ['y', '<', 'x'], ['x', '=', 'x']]
    expressions = pd.DataFrame(data, columns=['left_operand', 'operator', 'right_operand']).astype(
        {'left_operand': 'object', 'operator': 'object', 'right_operand': 'object'})
    print(eval_expression(variables, expressions))