#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 13:44:20 2018

@author: albertliu
"""

vowel = ['a', 'e', 'i', 'o', 'u'] # list of all vowels
print (vowel, '\n\n')
letter = {'a' : 0, 
          'e' : 0,
          'i' : 0,
          'o' : 0,
          'u' : 0}

print (letter, '\n\n')

name = 'my name is John and his is a bulldog'
print (name, '\n\n')   # the sentence

for c in name: 
    if c in vowel: 
        letter[c] += 1

sorted(letter)
print (letter)


