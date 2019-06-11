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

clean:
	pip uninstall circuitroomba
	rm -rf .tox .eggs src/circuitroomba.egg-info

install:
	mkdir -p /Volumes/ROOMBAPY/lib/circuitroomba
	cp -r ./src/circuitroomba /Volumes/ROOMBAPY/lib/circuitroomba

