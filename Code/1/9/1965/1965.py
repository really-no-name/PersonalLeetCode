#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1965.py
作者: Bolun Xu
创建日期: 2025/5/11
版本: 1.0
描述: 丢失信息的雇员。
"""
import pandas as pd


def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    employee_loss = employees[~employees['employee_id'].isin(salaries['employee_id'])][['employee_id']]
    salary_loss = salaries[~salaries['employee_id'].isin(employees['employee_id'])][['employee_id']]
    df = pd.concat([employee_loss, salary_loss], axis=0).sort_values(by='employee_id')
    return df


if __name__ == '__main__':
    data = [[2, 'Crew'], [4, 'Haven'], [5, 'Kristian']]
    employees = pd.DataFrame(data, columns=['employee_id', 'name']).astype({'employee_id': 'Int64', 'name': 'object'})
    data = [[5, 76071], [1, 22517], [4, 63539]]
    salaries = pd.DataFrame(data, columns=['employee_id', 'salary']).astype({'employee_id': 'Int64', 'salary': 'Int64'})
    print(find_employees(employees, salaries))