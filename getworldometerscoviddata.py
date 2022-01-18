#!/usr/bin/python3

#####################################################################
# Original authour: Bokwon Yoon
# With these comments, you are free to copy, distribute, and modify.
##################################################################### 

import datetime
import sys
import os

if len(sys.argv) < 3:
    print('USAGE: {} Country 국가'.format(sys.argv[0]))
    exit(1)

Country = sys.argv[1]
country = Country.lower()
CountryKr = sys.argv[2].rstrip()
outfile1 = 'covid-' + country + '-org.dat'
outfile2 = 'covid-' + country + '.csv'

url = r'https://www.worldometers.info/coronavirus/country/' + country + '/'

# Extract daily confirmed cases (dcases) and daily new deaths (ddeaths)
# 신규확진자수와 신규사망자수 추출
cmd  = f'curl -s "{url}"'
cmd += r" | sed -n -e '/text:/p' -e '/categories:/p' -e '/data:/p'"
cmd += r" | sed -n -e '/Daily New Cases/ {n;n;p;n;n;p}'  -e '/Daily Deaths/ {n;n;n;n;p}'"
cmd += r" | sed -e 's/categories://' -e 's/data://' -e 's/\[//' -e 's/\]//g' -e 's/\},//g'"
cmd += r" | sed -r -e 's/null/0/g' -e 's/([a-zA-Z]{3,3}) ([0-9]{1,2}), (.{4,4})/\1-\2-\3/g' -e 's/ //g' > " + outfile1
# print(cmd)
os.system(cmd)

# Create arrays of date, dcases, and ddeaths
# 날짜, 신규확진자, 신규사망자 배열 생성
lines = open(outfile1, 'r').readlines()
v = lines[0].rstrip().split(',')
date = list(map(lambda x: datetime.datetime.strptime(x, '"%b-%d-%Y"').strftime('%Y-%m-%d'), v))
dcases = list(map(lambda x: float(x), lines[1].rstrip().split(',')))
ddeaths = list(map(lambda x: float(x), lines[2].rstrip().split(',')))

# Calculate 7-day moving averages of date, dcases, and ddeaths
# 신규확진자와 신규사망자의 7일 이동평균 계산
dcases7 = []
ddeaths7 = []
for n in range(len(date)):
    sumlen = 7 if n > 5 else n+1
    sum1, sum2 = 0.0, 0.0
    for m in range(sumlen):
        sum1 += dcases[n-m]
        sum2 += ddeaths[n-m]
    dcases7.append(sum1/float(sumlen))
    ddeaths7.append(sum2/float(sumlen))

# Calculate case fatality rate (CFR) using 7-day moving averages of dcases and 
# ddeaths. 
# 14 days and 21 days are selected as the time lapses between date of case 
# confirmation date and death confirmation date. 
# The main CFR is the average between CFRs using 14 and 21-day time lapses.
# 신규확진자와 신규사망자의 7일 이동평균으로 확진자 치명률 계산
# 확진과 사망 사이의 시차는 14일과 21일로 정함.
# 메인 확진자 치명률은 이들 시차로 계산한 확진자 치명률의 평균으로 계산
with open(outfile2, 'w') as f:
    f.write('date dcases ddeaths dcases7 ddeath7 cfatal cfatalmin cfatalmax\n')
    for n in range(22, len(date)):
        cfatal14 = 0.0 if dcases7[n-14] == 0.0 else ddeaths7[n]/dcases7[n-14]
        cfatal21 = 0.0 if dcases7[n-21] == 0.0 else ddeaths7[n]/dcases7[n-21]
        str = '{},{:.0f},{:.0f},{:.5f},{:.5f},{:.5f},{:.5f},{:.5f}\n'.format(
              date[n], dcases[n], ddeaths[n], dcases7[n], ddeaths7[n], 
              0.5*(cfatal14+cfatal21)*100.0, 
              (cfatal14 if cfatal14 < cfatal21 else cfatal21)*100.0, 
              (cfatal14 if cfatal14 > cfatal21 else cfatal21)*100.0) 
        f.write(str)

# Create a graph
# 그래프 생성
newgpfile = f'covid-{country}.gp'
newpngfile = f'covid-{country}.png'
cmd = f'cp covid-country.gp {newgpfile}'
# print(cmd)
os.system(cmd)

cmd  = r'sed -e "s/country/' + country + r'/g" '
cmd += r'-e "s/Country/' + CountryKr + r'/g" -i ' + newgpfile
# print(cmd)
os.system(cmd)

cmd = f'gnuplot {newgpfile}'
# print(cmd)
os.system(cmd)

cmd = f'rm {newgpfile} {outfile1}'
# print(cmd)
os.system(cmd)

