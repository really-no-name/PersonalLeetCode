#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1507.py
作者: Bolun Xu
创建日期: 2025/3/20
版本: 1.0
描述: 转变日期格式。
时间复杂度： O(N)
空间复杂度： O(1)
"""


class Solution:
    def reformatDate(self, date: str) -> str:
        # 定义月份缩写到两位数字的映射字典
        month_mapping = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "Jun": "06",
            "Jul": "07",
            "Aug": "08",
            "Sep": "09",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12"
        }

        # 分割日期字符串
        parts = date.split()
        day = parts[0][:-2]  # 去掉日期后的 "th", "st", "nd", "rd"
        month = month_mapping[parts[1]]  # 获取月份的数字表示
        year = parts[2]  # 直接获取年份

        # 如果日期是一位数，前面补零
        if len(day) == 1:
            day = '0' + day

        # 返回格式化后的日期
        return f'{year}-{month}-{day}'


if __name__ == '__main__':
    sol = Solution()
    print(sol.reformatDate("20th Oct 2052"))