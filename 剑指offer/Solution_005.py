# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def push(self, node):
        self.s1.append(node)
        self.s2 = self.s1[::-1]
    def pop(self):
        self.s1 = self.s1[1:]
        return self.s2.pop()