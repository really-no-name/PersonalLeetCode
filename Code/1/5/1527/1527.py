#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1527.py
作者: Bolun Xu
创建日期: 2025/5/12
版本: 1.0
描述: 患某种疾病的患者。
"""
import pandas as pd


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    pattern = r'(^|\s)DIAB1'
    df_filt = patients[patients['conditions'].str.contains(pattern, regex=True, na=False)]
    return df_filt


if __name__ == '__main__':
    data = [[1, 'Daniel', 'YFEV COUGH'],
            [2, 'Alice', ''],
            [3, 'Bob', 'DIAB100 MYOP'],
            [4, 'George', 'ACNE DIAB100'],
            [5, 'Alain', 'DIAB201']]
    patients = pd.DataFrame(data, columns=['patient_id', 'patient_name', 'conditions']).astype(
        {'patient_id': 'int64', 'patient_name': 'object', 'conditions': 'object'})
    print(find_patients(patients))