#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 17:13:21 2020

@author: cyrilchappellet
"""

#I             1
#V             5
#X             10
#L             50
#C             100
#D             500
#M             1000

roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}

roman_string = str(input('Please Input a string of roman numerals:')).upper()
#for value in roman_string:
#    if value in 'IVXLCDM':
#        continue
#    else:
#        print('You have input the wrong string value:')
#        roman_string = str(input('Please Input a string of roman numerals'))

#print('join two strings:', ''.join(list(['one','two'])))
previous_value_small = False
list_numbers = []
for index,value in enumerate(roman_string):
#    if index == 0:
#        list_numbers.append(roman_dict[value])
#        continue
    if previous_value_small:
        previous_value_small = False
        value = ''.join([roman_string[index-1],roman_string[index]])
        list_numbers.append(roman_dict[value])
        continue
    
    if roman_dict[roman_string[index]] < roman_dict[roman_string[index+1]]:
        previous_value_small = True
        continue
    if value in roman_dict:
        list_numbers.append(roman_dict[value])
 
print('LIST:',list_numbers)        
print('Sum of list:', sum(list_numbers))
         
        
        