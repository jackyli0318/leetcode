#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 00:48:51 2018

@author: jackylee
"""

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        HEAD_LST = ['I','X','C']
        
        roman_dict = {
            "I": 1,
            "IV": 4,
            "IX": 9,
            "V": 5,
            "X": 10,
            "XL": 40,
            "XC": 90,
            "L": 50,
            "C": 100,
            "CD": 400,
            "CM": 900,
            "D": 500,
            "M": 1000,
        }
        
        i = 0
        length = len(s)
        result = 0
        while(i<length):
            if s[i] in HEAD_LST and i+1 < length:
                if s[i]+s[i+1] in roman_dict:
                    result += roman_dict[s[i]+s[i+1]]
                    i += 2
                    continue
                
            result += roman_dict[s[i]]
            i += 1
        return result
            
            
            
            
            
            
            