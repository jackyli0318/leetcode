#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 18:17:55 2018

@author: jackylee
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        length = len(nums1)
        mid = int(length/2)
        if length%2 == 0:
            median = float(nums1[mid-1] + nums1[mid])/2
        else:
            median = nums1[mid]
        return median