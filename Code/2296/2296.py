#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2296.py
作者: Bolun Xu
创建日期: 2025/2/27
版本: 1.0
描述: 设计一个文本编辑器。
"""


class TextEditor:
    def __init__(self):
        self.left = []  # 用于存储光标左侧的字符
        self.right = []  # 用于存储光标右侧的字符

    def addText(self, text: str) -> None:
        """
        在光标左侧添加文本
        :param text: 要添加的文本
        """
        self.left.extend(text)  # 将文本中的字符逐个添加到光标左侧

    def deleteText(self, k: int) -> int:
        """
        删除光标左侧的k个字符
        :param k: 要删除的字符数
        :return: 实际删除的字符数
        """
        pre = len(self.left)  # 记录删除前的字符数
        del self.left[-k:]  # 删除光标左侧的k个字符
        return pre - len(self.left)  # 返回实际删除的字符数

    def text(self) -> str:
        """
        获取光标左侧至多10个字符
        :return: 光标左侧的字符串
        """
        return ''.join(self.left[-10:])  # 返回光标左侧最多10个字符组成的字符串

    def cursorLeft(self, k: int) -> str:
        """
        将光标向左移动k个字符
        :param k: 要移动的字符数
        :return: 光标左侧至多10个字符
        """
        while k and self.left:
            self.right.append(self.left.pop())  # 将光标左侧的字符移动到右侧
            k -= 1
        return self.text()  # 返回光标左侧至多10个字符

    def cursorRight(self, k: int) -> str:
        """
        将光标向右移动k个字符
        :param k: 要移动的字符数
        :return: 光标左侧至多10个字符
        """
        while k and self.right:
            self.left.append(self.right.pop())  # 将光标右侧的字符移动到左侧
            k -= 1
        return self.text()  # 返回光标左侧至多10个字符


# 主程序
if __name__ == "__main__":
    editor = TextEditor()  # 创建TextEditor实例

    # 添加文本
    editor.addText("Hello, World!")
    print("After adding text:", editor.text())  # 输出: Hello, Wor

    # 删除文本
    deleted = editor.deleteText(5)
    print(f"Deleted {deleted} characters:", editor.text())  # 输出: Hello

    # 光标左移
    editor.cursorLeft(3)
    print("After moving cursor left:", editor.text())  # 输出: Hel

    # 光标右移
    editor.cursorRight(2)
    print("After moving cursor right:", editor.text())  # 输出: Hello

    # 调试信息
    print("Left stack:", editor.left)  # 输出: ['H', 'e', 'l', 'l', 'o']
    print("Right stack:", editor.right)  # 输出: [' ', 'W', 'o', 'r', 'l', 'd', '!']
