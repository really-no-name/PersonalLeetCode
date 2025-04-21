#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0577.py
作者: Bolun Xu
创建日期: 2025/4/21
版本: 1.0
描述: 员工奖金。
"""
import pandas as pd


def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    """
    告每个奖金 少于 1000 的员工的姓名和奖金数额
    :return: 以 任意顺序 返回结果表
    """
    # screen = employee[employee['supervisor'].notna()]
    total_emp = pd.merge(employee, bonus, how='left', on='empId')
    # print(total_emp)
    screen = total_emp[(total_emp['bonus'] < 1000) | (total_emp['bonus'].isna())]
    # print(screen)
    result = screen[['name', 'bonus']]
    return result


if __name__ == '__main__':
    data = [[3, 'Brad', None, 4000], [1, 'John', 3, 1000], [2, 'Dan', 3, 2000], [4, 'Thomas', 3, 4000]]
    employee = pd.DataFrame(data, columns=['empId', 'name', 'supervisor', 'salary']).astype(
        {'empId': 'Int64', 'name': 'object', 'supervisor': 'Int64', 'salary': 'Int64'})
    data = [[2, 500], [4, 2000]]
    bonus = pd.DataFrame(data, columns=['empId', 'bonus']).astype({'empId': 'Int64', 'bonus': 'Int64'})
    print(employee_bonus(employee, bonus))