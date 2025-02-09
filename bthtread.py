try:
	from PySide2.QtCore import QFile, QDataStream, QIODevice, QDateTime
except ModuleNotFoundError:
	try:
		from PyQt5.QtCore import QFile, QDataStream, QIODevice, QDateTime
	except ModuleNotFoundError:
		raise RuntimeError("No supported Qt version found!")

import sys, signal
import pickle

if __name__ == "__main__":
	print("Starting...")
	signal.signal(signal.SIGINT, signal.SIG_DFL)

	inputFile = QFile("test.output.lTSGec")
	if not inputFile.open(QIODevice.ReadOnly):
		raise RuntimeError("Could not read file...")

	dataStream = QDataStream(inputFile)
	dataStream.setVersion(QDataStream.Qt_5_15)

	arr_battery = []
	arr_humidity = []
	arr_temp = []
	arr_datetime = []

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
		arr_battery.append(battery)
		arr_humidity.append(humidity)
		arr_temp.append(temp * 0.1)
		arr_datetime.append(dateTimeStamp.toPython())
		n += 1

	inputFile.close()
	print(f"Number of entries read: {n}")

	with open("out.pickle", "wb") as file:
		pickle.dump((arr_battery, arr_humidity, arr_temp, arr_datetime), file)
		print("Output written to out.pickle")
