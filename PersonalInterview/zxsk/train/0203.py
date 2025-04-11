#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0203.py
作者: Bolun Xu
创建日期: 2025/4/11
版本: 1.0
描述: 。
时间复杂度：
空间复杂度：
"""
"""
描述
小明是一个互联网公司的老板，需要招聘员工。现在有k个学校的学生前来应聘。

由于特殊原因，要求最后入职的员工学校的人数应该都不一样。

比如我们可以A大学录取5人，B大学录取4人。但是不允许A大学和B大学都录取5人。

请问最后最多录取多少人呢？

输入描述
第一行一个整数k，表示学校的数量。

第二行k个整数ai，表示这个学校有ai个人前来应聘。

满足 1<=k<=100000,1<=ai<=100000

输出描述
输出最多录取人数

示例
输   入：
3
3 3 2
返回值：
6
"""
def max_hires(k, a_list):
    a_list.sort(reverse=True)
    used = set()
    total = 0

    for num in a_list:
        # 从 num 开始往下找一个没有用过的人数
        while num > 0 and num in used:
            num -= 1
        if num > 0:
            used.add(num)
            total += num
    return total

# 主程序入口
if __name__ == '__main__':
    k = int(input())
    a_list = list(map(int, input().split()))
    print(max_hires(k, a_list))