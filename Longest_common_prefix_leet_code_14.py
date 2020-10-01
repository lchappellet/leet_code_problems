#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 23:20:00 2020

@author: cyrilchappellet
"""
from typing import List

strs = ["flower","flow","flight"]
strs = ["abab","aba",""]
#strs = ["dog","racecar","car"]
#strs = ["a"]
equal_prefix = True
for index,pick_str in enumerate(strs):
        if index == 0:
            prev_str = pick_str
            continue
        if len(prev_str)< len(pick_str):
            continue
        else:
            prev_str = pick_str
print('pick_str:',prev_str)
for index, letter in enumerate(prev_str):
    for all_str in strs:
        print('strs:',strs)
        print('letter:',letter)
        if letter == all_str[index]:
            print('continue')
            continue
        else:
            equals = False
            if index == 0:
                index = 0
                print('break early:', '' )
            else:
                print('index minus one')
                index -= 1
                print('index to use:',index)
            break
    if not equal_prefix:
        print('str:',prev_str[:index])
#        return strs[:index]

#return strs[:index]
print('index_1:',index)
print('str_1:',prev_str[:index+1])

# quickest solution given for leet code. 
def longestCommonPrefix(strs: List[str]) -> str:
    if len(strs) == 0 :
        return ""
    min_str = min(strs , key=len)
    #7->6->5->...->1
    for i in reversed(range(1 , len(min_str)+1)) :
        search_str = min_str[0:i]
    for str in strs :
        if search_str not in str[0:len(search_str)] :
            break;
        else :
            return search_str
    else :
        return ""
strs = ["flower","flow","flight"]
answer = longestCommonPrefix(strs)
print('answer:',answer)
# HEre is the solution that worked for LEET code:
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # strs = ["flower","flow","flight"]
        equal_prefix = True
        prev_str = ''
        if len(strs) == 0:
            print('no length')
            return ''
        for index,pick_str in enumerate(strs):
                if index == 0:
                    prev_str = pick_str
                    continue
                if len(prev_str)< len(pick_str):
                    continue
                else:
                    prev_str = pick_str
        for index, letter in enumerate(prev_str):
            for all_str in strs:
                if letter == all_str[index]:
                    continue
                else:
                    equal_prefix = False
                    if index == 0:
                        index = 0
                        return ''
                    break
            if not equal_prefix:
                return prev_str[:index]

        return prev_str[:index+1]