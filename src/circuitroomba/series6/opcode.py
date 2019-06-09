# circuitroomba opcodes
# https://www.irobotweb.com/-/media/MainSite/PDFs/About/STEM/Create/iRobot_Roomba_600_Open_Interface_Spec.pdf?la=en

START = "0x80"
RESET = "0x7"
BAUD = "0x81"
CONTROL = "0x82"
SAFE = "0x83"
FULL = "0x84"
POWER = "0x85"
SPOT = "0x86"
CLEAN = "0x87"
MAX_CLEAN = "0x88"
DRIVE = "0x89"
MOTORS = "0x8a"
PWM_MOTORS = "0x90"
DRIVE_PWM = "0x92"
LEDS = "0x8b"
SONG = "0x8c"
PLAY = "0x8d"
STREAM = "0x94"
QUERY_LIST = "0x95"
DO_STREAM = "0x96"
QUERY = "0x8e"
FORCE_SEEKING_DOCK = "0x8f"
SCHEDULING_LEDS = "0xa2"
DIGIT_LEDS_RAW = "0xa3"
DIGIT_LEDS_ASCII = "0xa4"
BUTTONS = "0xa5"
SCHEDULE = "0xa7"
SET_DAY_TIME = "0xa8"
STOP = "0xad"

baud_codes = {
    0: 300,
    1: 600,
    2: 1200,
    3: 2400,
    4: 4800,
    5: 9600,
    6: 14400,
    7: 19200,
    8: 28800,
    9: 38400,
    10: 57600,
    11: 115200,
}

valid_modes = ("off", "safe", "passive", "full")

mode_commands = {
    "passive": (START, RESET, STOP, BAUD),
    "safe": (START, RESET, STOP, BAUD),
    "full": (START, RESET, STOP, BAUD),
    "off": (START, RESET),
    None: (START),
}

commands = {
    "0x80": {
        "int_opcode": 128,
        "data_bytes": 0,
        "new_mode": "passive",
        "new_mode_hex_opcode": "",
    },
    "0x7": {
        "int_opcode": 7,
        "data_bytes": 0,
        "new_mode": "off",
        "new_mode_hex_opcode": "",
    },
    "0xad": {
        "int_opcode": 173,
        "data_bytes": 0,
        "new_mode": "off",
        "new_mode_hex_opcode": "",
    },
    "0x81": {
        "int_opcode": 129,
        "data_bytes": 1,
        "new_mode": "passive",  # research how to best handle noop
        "new_mode_hex_opcode": "",
    },
}
