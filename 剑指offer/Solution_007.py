# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n <= 1:
            return n
        else :
            a = 0
            b = 1
            for i in range(2,n+1):
                b = a+b
                a = b-a
            return b