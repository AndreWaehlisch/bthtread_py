set term x11 size 1200,800 font "Times, 24"

unset key
set grid
set xdata time
set timefmt "%H:%M:%S-%d.%m.%Y"
set format x "%d.%m. %Hh"
set datafile separator ","

set ylabel "Temperature / deg C" tc "red"
set ytics nomirror autofreq tc "red"

set y2label "Humidity / %" tc "blue"
set y2tics nomirror autofreq tc "blue"

plot "bthtscan.csv" u 5:($4/10) w p lc "red" lw 2 axes x1y1, "bthtscan.csv" u 5:3 w p lc "blue" axes x1y2
pause mouse close
