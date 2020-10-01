#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 22:02:09 2020

@author: cyrilchappellet
"""

# Valid Parenthesis
# problem guidlines below:
#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
#An input string is valid if:
#
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
# 
#
#Example 1:
#
#Input: s = "()"
#Output: true
#Example 2:
#
#Input: s = "()[]{}"
#Output: true
#Example 3:
#
#Input: s = "(]"
#Output: false
#Example 4:
#
#Input: s = "([)]"
#Output: false
#Example 5:
#
#Input: s = "{[]}"
#Output: true
# 
#
#Constraints:
#
#1 <= s.length <= 104
#s consists of parentheses only '()[]{}'.

# my solution
# main idea. The sequence must be a mirror image. If I have () or ({{[]}}) both are mirror images around a central point.

string_parenthesis = '({{}}){}{}'
def isValid(string_parenthesis):
    parenth_dict = {'(':')','{':'}','[':']'}
    oposit_parenth_dict = {')':'(','}':'{',']':'['}
    if string_parenthesis[0] in oposit_parenth_dict:
        print('false_0:')
        return False
    list_parenth =  [parenth_dict[string_parenthesis[0]]]
    print(list_parenth)
    
    for i in range(1,len(string_parenthesis)):
        if len(list_parenth) == 0:
            if string_parenthesis[i] in oposit_parenth_dict:
                print('false_0:')
                return False
            list_parenth.append(parenth_dict[string_parenthesis[i]])
            continue
        # check to see that the next value is in the parenth dict else it isn't in the correct order.
        if string_parenthesis[i] in parenth_dict:
            list_parenth.append(parenth_dict[string_parenthesis[i]])
            continue
        # compare the string parenthesis to its opposite and see if they are equal 
        print('list_parenth:',list_parenth)
        print('oposit:',oposit_parenth_dict[list_parenth[-1]])
        if string_parenthesis[i] == list_parenth[-1]:
            print('true_parenth:',string_parenthesis[i],'value:',list_parenth[-1])
            list_parenth = list_parenth[:-1]
            continue
        
        else:
            print('false_1:',string_parenthesis[i], 'i equals:',i)
            return False
    if len(list_parenth) == 0: 
        print('first True')
        return True
    else:
        print('list false_2:',list_parenth)
        return False

print('result:', isValid(string_parenthesis))


# Here is the valid solution to the leet code:

class Solution:
    def isValid(self, s: str) -> bool:
        parenth_dict = {'(':')','{':'}','[':']'}
        oposit_parenth_dict = {')':'(','}':'{',']':'['}
        print('s[0]:',s[0])
        if s[0] in oposit_parenth_dict:
            # print('false_0:')
            return False
        list_parenth =  list(parenth_dict[s[0]])
        # print(list_parenth)
        
        for i in range(1,len(s)):
            if len(list_parenth) == 0:
                if s[i] in oposit_parenth_dict:
                    # print('false_0:')
                    return False
                list_parenth.append(parenth_dict[s[i]])
                continue
            # check to see that the next value is in the parenth dict else it isn't in the correct order.
            if s[i] in parenth_dict:
                list_parenth.append(parenth_dict[s[i]])
                continue
            # compare the string parenthesis to its opposite and see if they are equal 
            # print('list_parenth:',list_parenth)
            # print('oposit:',oposit_parenth_dict[list_parenth[-1]])
            if s[i] == list_parenth[-1]:
                # print('true_parenth:',s[i],'value:',list_parenth[-1])
                list_parenth = list_parenth[:-1]
                continue

            else:
                # print('false_1:',s[i], 'i equals:',i)
                return False
        if len(list_parenth) == 0: 
            # print('first True')
            return True
        else:
            # print('list false_2:',list_parenth)
            return False
         