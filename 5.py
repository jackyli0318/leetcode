#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 13:10:30 2018

@author: jackylee
"""

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    length = len(s)
    if length < 1:
        return s
    i = 0
    j = length
    max_len = 0
    max_sub = ""
    
    sub_str = s[i:j]
    cur_len = len(sub_str)
    j = sub_str[::-1].index(s[i])
    j = cur_len - j + i
        
    while(i<length):
        sub_str = s[i:j]
#        print(sub_str)
        if isPalindrome(sub_str):
            if len(sub_str)>max_len:
                max_len = len(sub_str)
                max_sub = sub_str
        else:
            if s[i] in s[i+1:j-1]:
                sub_str = s[i:j-1]
                cur_len = len(sub_str)
                j = sub_str[::-1].index(s[i])
                j = cur_len - j + i
                continue
        
        i += 1
        j = length
    
    return max_sub
    

def isPalindrome(s):
    if s == s[::-1]:
        return True
    return False



s="ababbbccccc"
a = longestPalindrome(s)
print(a)