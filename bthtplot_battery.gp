set term x11 size 1200,800 font "Times, 24"

unset key
set grid
set xdata time
set timefmt "%H:%M:%S-%d.%m.%Y"
set format x "%d.%m. %Hh"
set datafile separator ","

set ylabel "battery" tc "red"
set ytics nomirror autofreq tc "red"

plot "bthtscan.csv" u 5:2 w p lc "red" lw 2
pause mouse close
