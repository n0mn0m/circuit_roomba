import board
import busio
import digitalio
import time

start = b"\x80"
clean = b"\x87"
stop = b"\xAD"
power = b"\x85"
safe_mode = b"\x83"
full_mode = b"\x84"

start_codes = [start, safe_mode, clean]
stop_codes = [power, stop]

c = 0

def wake_up(brc):
    brc.value = False
    time.sleep(0.5)
    brc.value = True
    time.sleep(0.5)
    brc.value = False
    time.sleep(0.5)

brc = digitalio.DigitalInOut(board.A1)
brc.direction = digitalio.Direction.OUTPUT
uart = busio.UART(board.TX, board.RX, baudrate=19200)

for i in range(3):
    wake_up(brc)

while True:
    for code in start_codes:
        uart.write(code)
        print(code)

    time.sleep(2)

    for code in stop_codes:
        uart.write(code)
        print(code)


    c +=1

    print(brc)
    print(c)

    wake_up(brc)

    if c == 3:
        break
