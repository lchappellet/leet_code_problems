#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 12:29:41 2020

@author: cyrilchappellet
"""
# Leet coding problem:
#Given a 32-bit signed integer, reverse digits of an integer.
#
#Example 1:
#
#Input: 123
#Output: 321
#Example 2:
#
#Input: -123
#Output: -321
#Example 3:
#
#Input: 120
#Output: 21
#Note:
#Assume we are dealing with an environment which could only store integers
#  within the 32-bit signed integer range: [−231,  231 − 1].
#  For the purpose of this problem,
#  assume that your function returns 0 when the reversed integer overflows.



# Python program to reverse a number  
  
# Get the number from user manually 
# Here is what I found online for reversing a number.
num = int(input("Enter your favourite number: "))
 
# Initiate value to null
test_num = 0
 
# Check using while loop
 
while(num>0):
  #Logic
  remainder = num % 10
  test_num = (test_num * 10) + remainder
  num = num//10
 
# Display the result
print("The reverse number is : {}".format(test_num))


# My Code:
# Here is the code I wrote for reversing a number.
# Summary: The method used below is to convert the integer into a list of characters and then reverse the list of characters.


# here is my first solution:
# first take the input from the user 
string_num = int(input("enter your second favourite number:"))
# If there is a negative sign then I need to remove the negative from the integer and replace the negative sign later.
add_neg_to_num = False
# figure out if there is a negative number
if string_num < 0:
    add_neg_to_num = True
    string_num = -1*string_num
    
# insert each char to the beginning of the list because we go through the string
# from front to back then the first char will be at the end of the list because it is inserted first.
new_list = []
for char in str(string_num):
    print('char:',char)
    new_list.insert(0,char)
# add a neg number to a list if we found the number was negative earlier.
if add_neg_to_num:
    new_list.insert(0,'-')
print('new_numb_str_list',new_list)
# create a single string from the list
new_num_str = ''.join(new_list)
# generate a number instead of a string
new_num = int(new_num_str)
print("new_int_num:",new_num)


# here is what passed Leet coding
class Solution:
    def reverse(self, x: int) -> int:
        string_num = x
        if string_num < -2**31 or string_num > 2**31:
            print('returned zero')
            return 0
        add_neg_to_num = False
        if string_num < 0:
            add_neg_to_num = True
            string_num = -1*string_num
        new_list = []
        for char in str(string_num):
            print('char:',char)
            new_list.insert(0,char)
        if add_neg_to_num:
            new_list.insert(0,'-')
        print('new_numb_str_list',new_list)
        new_num_str = ''.join(new_list)
        new_num = int(new_num_str)
        print("new_int_num:",new_num)
        if new_num < -2**31 or new_num > 2**31:
            print('returned zero')
            return 0
        return new_num