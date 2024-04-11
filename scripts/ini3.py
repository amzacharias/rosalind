#!/usr/bin/env python
# -*-coding: utf-8 -*-
"""
Description:
# This program is for rosalind.info/problems/ini3/
Given:  A string s of length at most 200 letters and four
integers a, b, c and d.
Return: The slice of this string from indices a through b and c through d
(with space in between), inclusively.
In other words, we should include elements s[b] and s[d] in our slice.
"""
__author__ = 'Amanda Zacharias'
__contact__ = '16amz1@queensu.ca'
__date__ = '2024/04/11'
__version__ = '1.0'
__status__ = 'initiated'
# Code -----------------------------------------------
demo_s = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesan" \
         "dalltheKingsmenCouldntputHumptyDumptyinhisplaceagain."
demo_a = 22
demo_b = 27
demo_c = 97
demo_d = 102

print(demo_s[demo_a:demo_b+1], demo_s[demo_c:demo_d+1])
# Note that the end position for slicing is excluded, which is why we do end_pos+1

s = "wzNRCWZ4fTrwdkL2AVTH3MEoX1iMS910GDTKYsxcEvjKaOsvt5umKyP8rChrysopeleamy" \
    "0MqZFwldz5W0ztwFRuFGWwzdAG5U9o1TjuHyLrUP3wuikFPs1XSxDvnsoloensiseRkwa6n" \
    "2M5I0sqcpTstwxDcGlR71ruQtbi2iqknwc973Mq9I5."
a = 57
b = 67
c = 125
d = 133

print(s[a:b+1], s[c:d+1])
