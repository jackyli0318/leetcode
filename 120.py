#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 17:36:46 2018

@author: jackylee
"""

class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        f = list()
        rows = len(triangle)
        
        # init
        for i in range(len(triangle)):
            f.append(list())
            for j in range(len(triangle[i])):
                f[i].append(0)
        # init f[i][0] and f[i][i]
        f[0][0]=triangle[0][0]
        for i in range(1, len(triangle)):
            f[i][0] = triangle[i][0]+f[i-1][0]
            f[i][i] = triangle[i][i]+f[i-1][i-1]
        
        
        for x in range(1, len(triangle)):
            for y in range(1, len(triangle[x])-1):
               f[x][y] = triangle[x][y]+min(f[x-1][y-1], f[x-1][y])
        
        
        
        i = rows-1
        
        result = f[i][0]
        for j in range(len(f[i])):
            if f[i][j] < result:
                result = f[i][j]
        return result