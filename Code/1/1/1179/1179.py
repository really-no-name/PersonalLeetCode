#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1179.py
作者: Bolun Xu
创建日期: 2025/4/22
版本: 1.0
描述: 重新格式化部门表。
"""
import pandas as pd


def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    # 使用pivot将月份转换为列
    result = department.pivot(
        index='id',  # 保持id作为行标识
        columns='month',  # 月份值转换为列名
        values='revenue'  # 将收入值填充到对应的单元格中
    )  # 重组

    # 添加所有月份列（确保即使某些月份没有数据也包含该列）
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for month in months:
        if month not in result.columns:
            result[month] = None

    # 重命名列，添加_Revenue后缀
    result.columns = [f"{col}_Revenue" for col in result.columns]

    # 重置索引并将id作为列
    result = result.reset_index()

    # 重新排序列，确保顺序正确
    result = result[['id'] + [f"{month}_Revenue" for month in months]]

    return result


if __name__ == '__main__':
    data = [[1, 8000, 'Jan'], [2, 9000, 'Jan'], [3, 10000, 'Feb'], [1, 7000, 'Feb'], [1, 6000, 'Mar']]
    department = pd.DataFrame(data, columns=['id', 'revenue', 'month']).astype(
        {'id': 'Int64', 'revenue': 'Int64', 'month': 'object'})
    print(reformat_table(department))
