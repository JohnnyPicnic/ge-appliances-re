import os
import serial
import time

fd = serial.Serial('/dev/ttyUSB0', 19200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)

clear = lambda: os.system('clear')

wakeupCommand = serial.to_bytes([0xE2,0x03,0x08,0x00,0xC0,0x41,0x60,0xE3])
enterNativeMode = serial.to_bytes([0xE2,0x03,0x08,0xCB,0xC0,0x8B,0xCE,0xE3])

fd.write(wakeupCommand)
time.sleep(0.1)
fd.write(enterNativeMode)
time.sleep(0.1)

relay0On = serial.to_bytes([0xE2,0x03,0x0A,0xCB,0xC4,0x00,0x01,0x77,0x82,0xE3])
relay0Off = serial.to_bytes([0xE2,0x03,0x0A,0xCB,0xC4,0x00,0x00,0x67,0xA3,0xE3])
relay1On = serial.to_bytes([0xE2,0x03,0x0A,0xCB,0xC4,0x01,0x01,0x44,0xB3,0xE3])
relay1Off = serial.to_bytes([0xE2,0x03,0x0A,0xCB,0xC4,0x01,0x00,0x54,0x92,0xE3])
relay2On = serial.to_bytes([0xE2,0x03,0x0A,0xCB,0xC4,0x02,0x01,0x11,0xE0,0xE3])
relay2Off = serial.to_bytes([0xE2,0x03,0x0A,0xCB,0xC4,0x02,0x00,0x01,0xC1,0xE3])
relay3On = serial.to_bytes([0xE2,0x03,0x0A,0xCB,0xC4,0x03,0x01,0x22,0xD1,0xE3])
relay3Off = serial.to_bytes([0xE2,0x03,0x0A,0xCB,0xC4,0x03,0x00,0x32,0xF0,0xE3])
relay4On = serial.to_bytes([0xE2,0x03,0x0A,0xCB,0xC4,0x04,0x01,0xBB,0x46,0xE3])
relay4Off = serial.to_bytes([0xE2,0x03,0x0A,0xCB,0xC4,0x04,0x00,0xAB,0x67,0xE3])
relay5On = serial.to_bytes([0xE2,0x03,0x0A,0xCB,0xC4,0x05,0x01,0x88,0x77,0xE3])
relay5Off = serial.to_bytes([0xE2,0x03,0x0A,0xCB,0xC4,0x05,0x00,0x98,0x56,0xE3])
relay6On = serial.to_bytes([0xE2,0x03,0x0A,0xCB,0xC4,0x06,0x01,0xDD,0x24,0xE3])
relay6Off = serial.to_bytes([0xE2,0x03,0x0A,0xCB,0xC4,0x06,0x00,0xCD,0x05,0xE3])
relay7On = serial.to_bytes([0xE2,0x03,0x0A,0xCB,0xC4,0x07,0x01,0xEE,0x15,0xE3])
relay7Off = serial.to_bytes([0xE2,0x03,0x0A,0xCB,0xC4,0x07,0x00,0xFE,0x34,0xE3])
relay8On = serial.to_bytes([0xE2,0x03,0x0A,0xCB,0xC4,0x08,0x01,0xFE,0x2B,0xE3])
relay8Off = serial.to_bytes([0xE2,0x03,0x0A,0xCB,0xC4,0x08,0x00,0xEE,0x0A,0xE3])
relay9On = serial.to_bytes([0xE2,0x03,0x0A,0xCB,0xC4,0x09,0x01,0xCD,0x1A,0xE3])
relay9Off = serial.to_bytes([0xE2,0x03,0x0A,0xCB,0xC4,0x09,0x00,0xDD,0x3B,0xE3])

max = 9
delay = 0.2

while True:
	for relay in range(0, max):
		cmdOn = "relay" + str(relay) + "On"
		fd.write(vars()[cmdOn])
		print(relay, ": ON")
		time.sleep(delay)
	clear()
	time.sleep(0.5)
	for relay in range(0, max):
		cmdOff = "relay" + str(relay) + "Off"
		fd.write(vars()[cmdOff])
		print(relay, ": OFF")
		time.sleep(delay)
	time.sleep(0.2)
	fd.write(enterNativeMode)