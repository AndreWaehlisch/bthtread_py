import numpy as np
import sys, signal
import pickle

try:
	from PySide2.QtCore import QFile, QDataStream, QIODevice, QDateTime
except ModuleNotFoundError:
	try:
		from PyQt5.QtCore import QFile, QDataStream, QIODevice, QDateTime
	except ModuleNotFoundError:
		raise RuntimeError("No supported Qt version found!")

if __name__ == "__main__":
	print("Reading data...")
	signal.signal(signal.SIGINT, signal.SIG_DFL)

	inputFile = QFile("test.output")
	if not inputFile.open(QIODevice.ReadOnly):
		raise RuntimeError("Could not read file...")

	dataStream = QDataStream(inputFile)
	dataStream.setVersion(QDataStream.Qt_5_15)

	arr_packetID = []
	arr_battery = []
	arr_humidity = []
	arr_temp = []
	arr_datetime = []
	arr_ut = []

	n = 0
	while not inputFile.atEnd():
		length = dataStream.readUInt32()
		rawData = dataStream.readRawData(length)
		packetID = dataStream.readUInt8()
		battery = dataStream.readUInt8()
		humidity = dataStream.readUInt8()
		temp = dataStream.readInt16()
		dateTimeStamp = QDateTime()
		dataStream >> dateTimeStamp
		if dateTimeStamp.date().year() < 2025:
			continue
		arr_packetID.append(packetID)
		arr_battery.append(battery)
		arr_humidity.append(humidity)
		arr_temp.append(temp)
		arr_datetime.append(dateTimeStamp.toPython())
		arr_ut.append(dateTimeStamp.toString("hh:mm:ss-dd.MM.yyyy"))
		n += 1

	inputFile.close()
	print(f"Number of entries read: {n}")

	np.savetxt("out.csv", np.transpose((arr_packetID, arr_battery, arr_humidity, arr_temp, arr_ut)), fmt="%s", delimiter=",")
	print("Temp and humiditiy data output written to out.csv")

#	with open("out.pickle", "wb") as file:
#		pickle.dump((arr_battery, arr_humidity, arr_temp, arr_datetime), file)
#		print("Output written to out.pickle")
