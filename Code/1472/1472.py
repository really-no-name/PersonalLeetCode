#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 设计浏览器历史记录。
"""


class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cur = 0  # 当前页面是 history[cur]

    def visit(self, url: str) -> None:
        """
        从当前页跳转访问 url 对应的页面。执行此操作会把浏览历史前进的记录全部删除。
        :param url:
        :return:
        """
        self.cur += 1
        del self.history[self.cur:]  # 把浏览历史前进的记录全部删除
        self.history.append(url)  # 从当前页跳转访问 url 对应的页面

    def back(self, steps: int) -> str:
        """
        在浏览历史中后退 steps 步。
        如果你只能在浏览历史中后退至多 x 步 且 steps > x ，那么你只后退 x 步。
        :param steps:
        :return: 返回后退至多 steps 步 以后的 url
        """
        self.cur = max(self.cur - steps, 0)  # 后退 steps 步
        return self.history[self.cur]

    def forward(self, steps: int) -> str:
        """
        在浏览历史中前进 steps 步。
        如果你只能在浏览历史中前进至多 x 步且 steps > x ，那么你只前进 x 步。
        :param steps:
        :return: 返回前进 至多 steps步以后的 url
        """
        self.cur = min(self.cur + steps, len(self.history) - 1)  # 前进 steps 步
        return self.history[self.cur]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


if __name__ == '__main__':
    obj = BrowserHistory("leetcode.com")

    print("1------------------------------------------")
    obj.visit("google.com")  # 你原本在浏览 "leetcode.com" 。访问 "google.com"

    print("2------------------------------------------")
    obj.visit("facebook.com")  # 你原本在浏览 "google.com" 。访问 "facebook.com"

    print("3------------------------------------------")
    obj.visit("youtube.com")  # 你原本在浏览 "facebook.com" 。访问 "youtube.com"

    print("4------------------------------------------")
    print(obj.back(1))  # 你原本在浏览 "youtube.com" ，后退到 "facebook.com" 并返回 "facebook.com"

    print("5------------------------------------------")
    print(obj.back(1))  # 你原本在浏览 "facebook.com" ，后退到 "google.com" 并返回 "google.com"

    print("6------------------------------------------")
    print(obj.forward(1))  # 你原本在浏览 "google.com" ，前进到 "facebook.com" 并返回 "facebook.com"

    print("7------------------------------------------")
    obj.visit("linkedin.com")  # 你原本在浏览 "facebook.com" 。 访问 "linkedin.com"

    print("8------------------------------------------")
    print(obj.forward(2))  # 你原本在浏览 "linkedin.com" ，你无法前进任何步数。

    print("9------------------------------------------")
    print(obj.back(2))  # 你原本在浏览 "linkedin.com" ，后退两步依次先到 "facebook.com" ，然后到 "google.com" ，并返回 "google.com"
