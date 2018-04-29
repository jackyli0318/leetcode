#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 00:08:26 2018

@author: jackylee
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        positive = True
        maxi = 2 ** 31 -1
        mini = -2 ** 31 
        
        if x < 0:
            positive = False
            x = abs(x)
            print(str(x)[::-1])
        x = int(str(x)[::-1])
        if not positive:
            x = -x
        if x<mini or x>maxi:
            return 0
        return x