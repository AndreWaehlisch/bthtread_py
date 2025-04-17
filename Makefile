.PHONY: plot battery
.DEFAULT_GOAL := plot

plot: bthtscan.csv
	gnuplot bthtplot.gp

battery: bthtscan.csv
	gnuplot bthtplot_battery.gp
