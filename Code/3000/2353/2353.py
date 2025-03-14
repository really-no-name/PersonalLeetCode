#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2353.py
作者: Bolun Xu
创建日期: 2025/2/28
版本: 1.0
描述: 设计食物评分系统 -- 不符合leetcode要求？。
时间复杂度：
空间复杂度：
"""
from typing import List

import numpy
import pandas


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        """
        初始化系统。食物由 foods、cuisines 和 ratings 描述，长度均为 n 。
        :param foods: foods[i] 是第 i 种食物的名字。
        :param cuisines: cuisines[i] 是第 i 种食物的烹饪方式。
        :param ratings: ratings[i] 是第 i 种食物的最初评分。 1 <= ratings[i] <= 10^8
        """
        df = pandas.DataFrame([foods, cuisines, ratings])
        self.df = df.sort_values(by=0, axis=1)
        self.n = len(foods)
        # print(self.df)

    def changeRating(self, food: str, newRating: int) -> None:
        """
        修改名字为 food 的食物的评分
        :param food:
        :param newRating:
        :return:
        """
        i = numpy.where(self.df.iloc[0] == food)[0][0]
        self.df.iloc[2, i] = newRating
        # print(self.df)

    def highestRated(self, cuisine: str) -> str:
        """
        返回指定烹饪方式 cuisine 下评分最高的食物的名字。如果存在并列，返回 字典序较小 的名字。
        :param cuisine:
        :return:
        """
        max_rate = 0
        max_rate_food = ''
        for i in range(self.n):
            if self.df.iloc[1, i] == cuisine:
                if max_rate < self.df.iloc[2, i]:
                    max_rate = self.df.iloc[2, i]
                    max_rate_food = self.df.iloc[0, i]
        return max_rate_food


if __name__ == '__main__':
    # Your FoodRatings object will be instantiated and called as such:
    # obj = FoodRatings(foods, cuisines, ratings)
    # obj.changeRating(food,newRating)
    # param_2 = obj.highestRated(cuisine)
    foodRatings = FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
                              ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7])
    print(foodRatings.highestRated("korean"))  # 返回 "kimchi", "kimchi" 是分数最高的韩式料理，评分为 9 。
    print(foodRatings.highestRated("japanese"))  # 返回 "ramen", "ramen" 是分数最高的日式料理，评分为 14 。
    foodRatings.changeRating("sushi", 16)
    print(foodRatings.highestRated("japanese"))  # 返回 "sushi", "sushi" 是分数最高的日式料理，评分为 16 。
    foodRatings.changeRating("ramen", 16)
    print(foodRatings.highestRated("japanese"))  # 返回 "ramen", "sushi" 和 "ramen" 的评分都是 16 。但是，"ramen" 的字典序比 "sushi" 更小。
