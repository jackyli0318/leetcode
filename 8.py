#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 18:30:29 2018

@author: jackylee
"""


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        str = str.strip()
        str_lst = str.split(" ")
        negative = False
        result = 0

        sub_str = str_lst[0]
        
        if "-+" in sub_str or "+-" in sub_str:
            return result
        
        if len(sub_str)>0 and "-" in sub_str[0]:
            negative = True
            sub_str = sub_str[1:]
        if len(sub_str)>0 and "+" in sub_str[0]:
            sub_str = sub_str[1:]
        
        result = ""
        for c in range(len(sub_str)):
            if sub_str[c].isdigit():
                result += sub_str[c]
            else:
                break
        
        if result.isdigit():
            result = int(result)
            if negative:
                result = -result
        if result == "":
            return 0
        if result < -2 ** 31:
            result = -2 ** 31
        if result > 2 ** 31 - 1:
            result = 2 ** 31 -1
        return result