#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2299.py
作者: Bolun Xu
创建日期: 2025/4/16
版本: 1.0
描述: 。
时间复杂度：
空间复杂度：
"""
import re


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if (len(password) < 8 or
                not bool(re.search(r'[a-z]', password)) or
                not bool(re.search(r'[A-Z]', password)) or
                not bool(re.search(r'[0-9]', password)) or
                not bool(re.search(r'[!@#$%^&*()+-]', password))):
            return False
        for i in range(len(password) - 1):
            if password[i] == password[i + 1]:
                return False
        return True