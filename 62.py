#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 17:45:26 2018

@author: jackylee
"""

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int column
        :type n: int row
        :rtype: int
        """
        f = list()
        for i in range(n):
            f.append(list())
            for j in range(m):
                f[i].append(1)
        
        for x in range(1, n):
            for y in range(1, m):
                f[x][y] = f[x-1][y]+f[x][y-1]
        return f[n-1][m-1]