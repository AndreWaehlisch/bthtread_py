import pickle

with open("out.pickle", "rb") as file:
	bat, hum, temp, dt = pickle.load(file)

usePyQtGraph = False

def myform(x, pos):
	return f"{x:.1f} °C"

def update_view(*args):
	global ax2_view, win
	ax2_view.setGeometry(win.plotItem.vb.sceneBoundingRect())
	ax2_view.linkedViewChanged(win.plotItem.vb, ax2_view.XAxis)

if usePyQtGraph:
	import pyqtgraph as pg
	from pyqtgraph.graphicsItems.DateAxisItem import DateAxisItem
	win = pg.PlotWidget(axisItems={"bottom": DateAxisItem()})
	timestamps = [d.timestamp() for d in dt]
	win.plot(timestamps, temp, pen="r")
	ax2 = pg.AxisItem("right")
	win.plotItem.layout.addItem(ax2, 2, 3)
	ax2_view = pg.ViewBox()
	win.plotItem.scene().addItem(ax2_view)
	win.plotItem.getAxis("right").linkToView(ax2_view)
	ax2_view.setXLink(win.plotItem)
	ax2_view.addItem(pg.PlotDataItem(timestamps, hum, pen="b"))
	win.show()
else:
	from plot import plot
	import matplotlib.pyplot as plt
	from matplotlib.ticker import FuncFormatter

	with open("out.pickle", "rb") as file:
		bat, hum, temp, dt = pickle.load(file)
		plot(dt, temp, xtit="DateTime", ytit="Temperature", color="red", ytit_fontcolor="red", yax_color="red")
		ax = plt.gca()
		ax.yaxis.set_major_formatter(FuncFormatter(myform))
		plot(dt, hum, color="blue", ytit="Humidity", addYAxis=True, overplot=True, ytit_fontcolor="blue", yax_color="blue", percent=True)
