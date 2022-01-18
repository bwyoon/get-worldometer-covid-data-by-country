#!/usr/bin/python3

#####################################################################
# Original authour: Bokwon Yoon
# With these comments, you are free to copy, distribute, and modify.
#####################################################################

import os
import sys

Country = ['South-Africa', 'US', 'Japan', 'Cuba', 'South-Korea', 'Portugal', 'Singapore', 'UK', 'France', 'Israel', 'Germany', 'Italy', 'Ireland']
CountryKr = ['남아공', '미국', '일본', '쿠바', '한국', '포르투갈', '싱가포르', '영국', '프랑스', '이스라엘', '독일', '이탈리아', '아일랜드']

for c, ckr in zip(Country, CountryKr):
    cmd = './getworldometerscoviddata.py ' + c + ' ' + ckr
    print(cmd)
    os.system(cmd)
