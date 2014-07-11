#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 10, 2014

@author: anroco

How to find a string inside a python str?

¿Como encontrar un string dentro de un str python?
'''

#create a str
s = 'red lorry, yellow lorry, red lorry, yellow lorry'
print(s)

#use the in statement, return True or False
print('red' in s)

#define the segment of the string to perform the search
print('lorry' in s[6:30])

#the find(value) method return the first index in the string where the
#substring (value) is found, return -1 if substring is not found.
index = s.find('yellow')
print(index)

#define the segment of the string to perform the search
index = s.find('lorry', 6, 30)
print(index)
