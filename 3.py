#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 22:20:12 2018

@author: jackylee
"""

def lengthOfLongestSubstring(s):  
    """
    :type s: str
    :rtype: int
    """
    length = len(s)
    if length <= 1:
        return length
    
    if len(set(s)) == 1:
        return 1
    
    i = 0
    j = 1
    max_length = 1
    while(j<length):
        sub_string = s[i:j]
        cur_length = len(sub_string)
        try:
            pos = sub_string.index(s[j])
        except ValueError:
            j += 1
            continue
        
        if cur_length > max_length:
            max_length = cur_length
        i = i + pos + 1  # 因为是子序列，所以是i+pos+1才是s的位置
        j += 1
    
    sub_string = s[i:j]
    if len(set(sub_string)) == len(sub_string):
        cur_length = len(sub_string)
    if cur_length > max_length:
        max_length = cur_length
        
    print(max_length)
    return max_length


def solution2(s):  #超时
    length = len(s)
    maxi_sub = 1
    if length == 0:
        return 0
    for i in range(length-1):
        if s[i] == s[i+1]:
            continue
        for j in range(length, i, -1):
            if s[j-1] == s[j-2]:
                continue
                   
            # print(s[i:j])
            set_s = set(s[i:j])
            sub_length = j-i
            if sub_length == len(set_s):
                if sub_length > maxi_sub:
                    maxi_sub = sub_length
           
                   
    return maxi_sub
    

#a="aabcddeeffgiowefuauu"
###a="a abcd de ef fgiowe fua uu"
#lengthOfLongestSubstring(a)
##
a="abcde"
lengthOfLongestSubstring(a)
#
a="abcaabcbb"
lengthOfLongestSubstring(a)

a="dvdf"
lengthOfLongestSubstring(a)

