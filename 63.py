#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 18:19:31 2018

@author: jackylee
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])
        
        f = list()
        for i in range(rows):
            f.append(list())
            for j in range(columns):
                f[i].append(-1)
                
        for i in range(rows):
            for j in range(columns):
                if obstacleGrid[i][j] == 0:
                    f[i][j] = 1
                else:
                    f[i][j] = 0
        
        for i in range(1, rows):
            if f[i][0] == 1:
                f[i][0] = f[i-1][0]
        for j in range(1, columns):
            if f[0][j] == 1:
                f[0][j] = f[0][j-1]
                
            
        for x in range(1, rows):
            for y in range(1, columns):
                if f[x][y] == 0:
                    continue
                f[x][y] = f[x-1][y]+f[x][y-1]
                
        return f[rows-1][columns-1]
        
        