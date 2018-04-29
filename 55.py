#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 21:26:41 2018

@author: jackylee
"""

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''
        last_index = length-1
        x < index+nums[index] 
        
        f[x]=False
        
        
        '''
        # 从后往前推
        last_index = len(nums) - 1
        
        can_lst = [last_index]
        
        for i in range(last_index-1, -1, -1):
            if nums[i]+i >= can_lst[len(can_lst)-1]:
                can_lst.append(i)
        if 0 in can_lst:
            return True
        else:
            return False
        
        # 从前往后推
#         last_index = len(nums) -1
#         f = list()
#         for i in range(len(nums)):
#             f.append(False)
#         f[0] = True
        
#         for i in range(len(nums)):
#             if f[i] == True:
#                 tmp_index = i
#                 jump_dis = nums[tmp_index]+1
                
#                 if tmp_index+jump_dis>last_index:
#                     return True
                
#                 for x in range(tmp_index+1, tmp_index+jump_dis):
#                     if x < last_index:
#                         f[x]=True
#                     elif x == last_index:
#                         return True
                        
#         return f[last_index]
                