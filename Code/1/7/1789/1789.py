#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1789.py
作者: Bolun Xu
创建日期: 2025/4/22
版本: 1.0
描述: 员工的直属部门。
"""
import pandas as pd


def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    condition = ((employee['primary_flag'] == 'Y') |
                 (~employee['employee_id'].duplicated(keep=False))
                 )
    return employee[condition][['employee_id', 'department_id']]


if __name__ == '__main__':
    data = [['1', '1', 'N'], ['2', '1', 'Y'], ['2', '2', 'N'], ['3', '3', 'N'], ['4', '2', 'N'], ['4', '3', 'Y'],
            ['4', '4', 'N']]
    employee = pd.DataFrame(data, columns=['employee_id', 'department_id', 'primary_flag']).astype(
        {'employee_id': 'Int64', 'department_id': 'Int64', 'primary_flag': 'object'})
    print(find_primary_department(employee))