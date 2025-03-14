#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2353.py
作者: Bolun Xu
创建日期: 2025/2/28
版本: 2.0
描述: 设计食物评分系统。
时间复杂度：
空间复杂度：
"""
from typing import List

from collections import defaultdict
from sortedcontainers import SortedList  # 使用 sortedcontainers 库中的 SortedList 来维护有序列表


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        """
        初始化 FoodRatings 类。

        :param foods: 食物名称列表
        :param cuisines: 食物对应的菜系列表
        :param ratings: 食物对应的评分列表
        """
        self.food_map = {}  # 用于存储食物名称到其评分和菜系的映射
        self.cuisine_map = defaultdict(SortedList)  # 用于存储每个菜系对应的食物列表，按评分和名称排序

        # 遍历食物、菜系和评分列表，初始化 food_map 和 cuisine_map
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_map[food] = [rating, cuisine]  # 存储食物的评分和菜系
            # 将评分取负值，以便在 SortedList 中按评分从高到低排序，评分相同时按名称字典序排序
            self.cuisine_map[cuisine].add((-rating, food))

        # 调试信息：打印初始化后的 food_map 和 cuisine_map
        # print("Initialized food_map:", self.food_map)
        # print("Initialized cuisine_map:", self.cuisine_map)

    def changeRating(self, food: str, newRating: int) -> None:
        """
        更新食物的评分。

        :param food: 需要更新评分的食物名称
        :param newRating: 新的评分
        """
        if food not in self.food_map:
            # print(f"Error: Food '{food}' not found in food_map.")
            return

        # 获取食物的当前评分和菜系
        rating, cuisine = self.food_map[food]
        sl = self.cuisine_map[cuisine]  # 获取该菜系对应的 SortedList

        # 调试信息：打印更新前的 SortedList
        # print(f"Before changing rating for '{food}': {sl}")

        # 从 SortedList 中移除旧的评分和食物组合
        sl.discard((-rating, food))
        # 添加新的评分和食物组合
        sl.add((-newRating, food))
        # 更新 food_map 中的评分
        self.food_map[food][0] = newRating

        # 调试信息：打印更新后的 SortedList
        # print(f"After changing rating for '{food}': {sl}")

    def highestRated(self, cuisine: str) -> str:
        """
        返回指定菜系中评分最高的食物名称。

        :param cuisine: 菜系名称
        :return: 评分最高的食物名称
        """
        if cuisine not in self.cuisine_map:
            # print(f"Error: Cuisine '{cuisine}' not found in cuisine_map.")
            return ""

        # 获取该菜系对应的 SortedList 中的第一个元素（评分最高的食物）
        highest_rated_food = self.cuisine_map[cuisine][0][1]

        # 调试信息：打印查询结果
        # print(f"Highest rated food in '{cuisine}': {highest_rated_food}")

        return highest_rated_food


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
