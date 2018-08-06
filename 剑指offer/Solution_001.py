# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array)==0 or len(array[0])==0 or target < array[0][0] or target > array[-1][-1]:
        	return False
        i,j = len(array)-1,0
        while i>=0 and j< len(array[0]):
        	if array[i][j] == target:
        		return True
        	elif array[i][j] < target:
        		j = j+1
        	else:
        		i = i-1
        return False