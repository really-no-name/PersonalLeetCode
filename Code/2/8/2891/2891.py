#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2891.py
作者: Bolun Xu
创建日期: 2025/5/9
版本: 1.0
描述: 方法链。
"""
import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    df_filtered = animals[animals['weight'] > 100]
    df_sorted = df_filtered.sort_values(by=['weight'], ascending=False)
    return df_sorted[['name']]


if __name__ == '__main__':
    data = [['Tatiana', 'Snake', 98, 464],
            ['Khaled', 'Giraffe', 50 , 41 ],
            ['Alex', 'Leopard', 6  , 328],
            ['Jonathan', 'Monkey ', 45 , 463],
            ['Stefan', 'Bear   ', 100, 50 ],
            ['Tommy', 'Panda  ', 26 , 349]]
    animals = pd.DataFrame(data, columns=['name', 'species', 'age', 'weight']).astype({
        'name': object, 'species': object, 'age': int, 'weight': int
    })
    print(findHeavyAnimals(animals))