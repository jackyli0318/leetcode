#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 18:07:12 2018

@author: jackylee
"""

def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    zigzag_dict = dict()
    for i in range(numRows):
        zigzag_dict[i] = list()
    
    added = 0
    plus_flag = True
    for c in s:
        # increasing
        
        if plus_flag and added<numRows:
            zigzag_dict[added].append(c)
            added += 1
        elif plus_flag and added == numRows:
            plus_flag = False
            if numRows > 1:
                added -= 2
            else:
                added -= 1
        
        # decreasing
        if plus_flag == False and added > 0:
            zigzag_dict[added].append(c)
            added -= 1
        if plus_flag == False and added == 0:
            plus_flag = True
            if numRows <= 2:
                zigzag_dict[added].append(c)
                added += 1
    result = ""
    for i in range(numRows):
        for c in zigzag_dict[i]:
            if c:
                result += c
    return result


print(convert("ABCD",2))