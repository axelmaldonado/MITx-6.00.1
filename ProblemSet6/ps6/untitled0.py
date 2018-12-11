#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 14:49:02 2018

@author: axel
"""

import string

def get_country_codes(prices):
    # your code here
    for i in range(len(prices[0])):
        
        if prices[i+1] in string.ascii_lowercase:
            (print("hi"))


# don't include these tests in Vocareum
from test import testEqual

testEqual(get_country_codes("NZ$300, KR$1200, DK$5"), "NZ, KR, DK")
testEqual(get_country_codes("US$40, AU$89, JP$200"), "US, AU, JP")
testEqual(get_country_codes("AU$23, NG$900, MX$200, BG$790, ES$2"), "AU, NG, MX, BG, ES")
testEqual(get_country_codes("CA$40"), "CA")