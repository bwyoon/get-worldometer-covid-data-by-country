#####################################################################
# Original authour: Bokwon Yoon
# With these comments, you are free to copy, distribute, and modify.
#####################################################################

set term pngcairo enhanced size 960,960 font "Arial, 25"
set output 'covid-country.png'

file1 = 'covid-country.csv'
set datafile separator ","

set xdata time
set timefmt "%Y-%m-%d"
xmin = "2021-09-01"
xmax = "2021-09-29"
ymin = 0
ymax = 2.5

PX1 = 0.130
PX2 = 0.950
PY1 = 0.150
PY2 = 0.930

set multiplot

unset key
#set grid
#set style line 100 lt 1 lc rgb "gray" lw 2
#set grid ls 100

lw0 = 2 
lw1 = 4
set border 15
set border lw lw1

set lmargin at screen PX1
set rmargin at screen PX2
set bmargin at screen PY1
set tmargin at screen PY2

set xlabel "날짜" offset 0,1.00
set format x "%b-%d"
set xrange[xmin:]
set xtics out offset 0, 0.5 rotate by 270
#set xtics ("2021-09-01","2021-09-15", "2021-10-01", "2021-10-15", "2021-11-01", "2021-11-15",  "2021-12-01", "2021-12-15", "2022-01-01", "2022-01-15", "2022-02-01", "2022-02-15")
set xtics ("2021-09-01","2021-09-08", "2021-09-15", "2021-09-22", "2021-09-29", "2021-10-06",  "2021-10-13", "2021-10-20", "2021-10-27", "2021-11-03", "2021-11-10", "2021-11-17", "2021-11-24", "2021-12-01", "2021-12-08", "2021-12-15", "2021-12-22", "2021-12-29", "2022-01-05", "2022-01-12", "2022-01-19", "2022-01-26")
set mxtics 7
#set xtics 1, 1, 16 out offset 0, 0.25

set ylabel "단기 확진자 치명률 (%)" offset 1.75, 0
set format y "%.1f"
set yrange[ymin:ymax]
set ytics 0, 0.5, ymax out offset 0.5, 0 
set mytics 5

set object 1 rectangle from screen -0.1,-0.1 to screen 1.1,1.1 fillcolor rgb"#fffff0" behind
set label "Country 단기 확진자 치명률" center at screen 0.5, 0.975

# file1 every ::1 u 1:8 w filledcurve x1 lw 0 fc rgb "#88ccff", \

plot \
file1 every ::1 u 1:8 w filledcurve x1 lw 0 fc rgb "#aaeeff", \
file1 every ::1 u 1:7 w filledcurve x1 lw 0 fc rgb "#fffff0", \
file1 every ::1 u 1:6 w l lw 4 lc rgb "#0000ff", \
