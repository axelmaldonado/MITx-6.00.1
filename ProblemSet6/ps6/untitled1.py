#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 19:35:56 2018

@author: axel
"""
def ex1(string):
    listOfLetters = []
    for i in range(len(string)):
        if string[i].isalpha():
            listOfLetters.append(string[1])
    return listOfLetters

ex1("ThiS is a String with Upper and lower case Letters")