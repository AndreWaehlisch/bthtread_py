import pickle
from plot import plot
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def myform(x, pos):
	return f"{x:.0f} °C"

with open("out.pickle", "rb") as file:
	bat, hum, temp, dt = pickle.load(file)
	plot(dt, temp, xtit="DateTime", ytit="Temperature", color="red", ytit_fontcolor="red", yax_color="red")
	ax = plt.gca()
	ax.yaxis.set_major_formatter(FuncFormatter(myform))
	plot(dt, hum, color="blue", ytit="Humidity", addYAxis=True, overplot=True, ytit_fontcolor="blue", yax_color="blue", percent=True)
