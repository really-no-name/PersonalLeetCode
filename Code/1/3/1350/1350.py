#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1350.py
作者: Bolun Xu
创建日期: 2025/4/29
版本: 1.0
描述: 院系无效的学生。
"""
import pandas as pd


def find_students(departments: pd.DataFrame, students: pd.DataFrame) -> pd.DataFrame:
    departments = departments.rename(columns={"id": "department_id", "name": "department_name"})
    merged_df = students.merge(departments, on='department_id', how='left')
    screen = merged_df[merged_df['department_name'].isna()]
    return screen[['id', 'name']]


if __name__ == '__main__':
    data = [[1, 'Electrical Engineering'], [7, 'Computer Engineering'], [13, 'Bussiness Administration']]
    departments = pd.DataFrame(data, columns=['id', 'name']).astype({'id': 'Int64', 'name': 'object'})
    data = [[23, 'Alice', 1], [1, 'Bob', 7], [5, 'Jennifer', 13], [2, 'John', 14], [4, 'Jasmine', 77], [3, 'Steve', 74],
            [6, 'Luis', 1], [8, 'Jonathan', 7], [7, 'Daiana', 33], [11, 'Madelynn', 1]]
    students = pd.DataFrame(data, columns=['id', 'name', 'department_id']).astype(
        {'id': 'Int64', 'name': 'object', 'department_id': 'Int64'})
    print(find_students(departments, students))