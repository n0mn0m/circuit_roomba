rename:
	/usr/sbin/diskutil rename CIRCUITPY ROOMBAPY

check:
	ls /Volumes/ROOMBAPY

send:
	cp main.py /Volumes/ROOMBAPY

locate:
	@ls /dev/tty.usb*

connect:
	screen /dev/tty.usbmodem143101 115200
