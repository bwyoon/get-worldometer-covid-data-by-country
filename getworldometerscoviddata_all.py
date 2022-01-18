#!/usr/bin/python3

#####################################################################
# Original authour: Bokwon Yoon
# With these comments, you are free to copy, distribute, and modify.
#####################################################################

import os
import sys

Country = [ ['South-Africa', '남아공'], ['US', '미국'], ['Japan', '일본'],
 ['Cuba', '쿠바'], ['South-Korea', '한국'], ['Portugal', '포르투갈'], 
 ['Singapore', '싱가포르'], ['UK','영국'], ['France', '프랑스'], 
 ['Israel', '이스라엘'], ['Germany', '독일'], ['Italy', '이탈리아'], 
 ['Ireland', '아일랜드'] ]

for c in Country:
    cmd = './getworldometerscoviddata.py ' + c[0] + ' ' + c[1]
    print(cmd)
    os.system(cmd)
