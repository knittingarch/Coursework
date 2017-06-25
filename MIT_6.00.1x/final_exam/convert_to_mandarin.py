#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 12:43:42 2016

@author: sdawson
"""

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num

    0-10 = digit
    11-19 = ten digit
    20-99 = digit ten digit
    '''

    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san',
    	'4': 'si', '5':'wu', '6':'liu', '7':'qi',
    	'8':'ba', '9':'jiu', '10': 'shi'}

    ten = trans["10"]
    first = us_num // 10
    second = us_num % 10    
    
    if 0 < us_num < 11:
        return trans[str(us_num)]
    elif us_num < 20:
        if first == 1:
            new_number = "%s %s" % (ten, trans[str(second)])
        return new_number
    elif us_num < 100:
        if 1 < first <= 9:
            if second != 0:
                second = trans[str(second)]
                new_number = "%s %s %s" % (trans[str(first)], ten, second)
                return new_number
            else:                
                new_number = "%s %s" % (trans[str(first)], ten)
                return new_number