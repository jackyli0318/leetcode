#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 20:08:53 2018

@author: jackylee
"""

#def isMatch(s, p):
#    """
#    :type s: str
#    :type p: str
#    :rtype: bool
#    """
##    one = 0
##    snd = 0
##    sub = ""
##    pat = ""
##    adding = True
##    if s == p:
##        return True
##    
##    while(one<len(s)):
##        if snd==len(p):
##            return False
##            
##        if p[snd] == "*":
##            adding = False
##            
##            pat_len = len(pat)
##            i = 0
##            repeat = False
##            
##            
##            while (one<len(s) and s[one]==pat[i]):
##                one += 1
##                i += 1
##                if i == pat_len:
##                    repeat = True
##                    i = 0
##            # i==0时，符合pat
##            if repeat == False and i>0:
##                return False
##            
##            pat = ""
##            if one==len(s) and i>0:
##                return False
##            else:
##                return True
##            
##            sub = s[one]
##            adding = True
##            continue
##            
##        if p[snd] == ".":
##            if snd+1<len(p) and p[snd+1] == "*":
##                return True
##                
##            pat = ""
##            sub = ""
##            continue
##        
##        sub += s[one]
##        if adding:
##            pat += p[snd]
##        
##        one += 1
##        snd += 1
##        
##    return True
#    
#    one = 0
#    snd = 0
#    pat = ""
#    
#    if s == p:
#        return True
#    
#    while(one<len(s)):
#        if snd>=len(p):
#            return False
#        
#        if s[one] == p[snd]:
#            pat = p[snd]
#            one += 1
#            snd += 1
#            
#            continue
#        
#        
#        if p[snd] == ".":
#            if snd+1<len(p) and p[snd+1] == "*":
#                if snd+2>=len(p):
#                    return True
#                
#                
#            pat = ""
#            one += 1
#            snd += 1
#            continue
#        
#        if p[snd] == "*":
#            while(one<len(s) and s[one]==pat):
#                one += 1
#            snd += 1
#            if snd>=len(p) and s[one-1]!=pat:
#                return False
#            elif snd>=len(p) and s[one-1]==pat:
#                return True
#            if one>=len(s) and s[-1]==p[snd]:
#                return True
#            if one>=len(s):
#                return False
#            
#            if p[snd]==".":
#                pat = ""
#                one += 1
#                snd += 1
#                continue
#            
#            if s[one] != p[snd]:
#                return False
#            
#            continue
#        
#        if s[one] != p[snd]:
#            if snd+1<len(p) and p[snd+1] != "*":
#                return False
#            else:
#                snd += 2
#    
#    if one>=len(s) and snd<len(p):
#        return False
#    return True

def isMatch(s, p):
    s = s[::-1]
    p = p[::-1]
    
    one = 0
    snd = 0
    pat = ""
    
    if s == p:
        return True
    
    while(one<len(s)):
        if snd>=len(p):
            return False
        
        if s[one] == p[snd]:
            one += 1
            snd += 1
            continue
        
        
        if p[snd] == ".":
            pat = ""
            one += 1
            snd += 1
            continue
        
        if p[snd] == "*":
            snd += 1
            pat = p[snd]
            
            if p[snd]==".":
                pat = s[one]
            
            one += 1
            while( one<len(s) and s[one]==pat ):
                one += 1
            if one<len(s) and s[one]!=pat:
                snd += 1
                continue
            # one>len(s)
            if snd>=len(p):
                return True
            else:
                if p[snd:].count("*") == len(p[snd:])/2:
                    return True
                else:
                    return False
                
        
        if s[one] != p[snd]:
            return False
    
    if one>=len(s):
        if snd<len(p) and p[snd:].count("*") == len(p[snd:])/2:
            return True
        return False
        
    return True


s="aaa"
p="ab*a*c*a"

print(isMatch(s, p))