GPIO0 = 0#7
GPIO1 = 1#6


DATA_PIN = GPIO0
CLK_PIN = GPIO1

OUTPUT = True
INPUT = False

HIGH = True
LOW = False

# Globals:
gain = 1


def hx711_begin():
    setPinDir(CLK_PIN, OUTPUT)
    writePin(CLK_PIN, LOW)
    setPinDir(DATA_PIN, INPUT)


def hx711_set_gain(new_gain):
    global gain
    if new_gain == 128:   # channel A, gain factor 128
        gain = 1
    elif new_gain == 64:  # channel A, gain factor 64
        gain = 3
    elif new_gain == 32:  # channel B, gain factor 32
        gain = 2
    else:
        return "Invalid gain value"

    hx711_read()
    return gain


def hx711_read():
    #TODO: wait until ready:
    if not hx711_is_ready():
        return "Not ready"

    i = 0
    high_byte = 0
    low_byte = 0

    byte3 = None  # MSB
    byte2 = None
    byte1 = None
    byte0 = None  # LSB

    current_byte = 0
    while i<8:
        pulsePin(CLK_PIN, -1, HIGH)
        #writePin(CLK_PIN, HIGH)
        current_byte = (current_byte << 1) + int(readPin(DATA_PIN))
        #writePin(CLK_PIN, LOW)
        i += 1
    byte2 = current_byte

    current_byte = 0
    while i<16:
        pulsePin(CLK_PIN, -1, HIGH)
        #writePin(CLK_PIN, HIGH)
        current_byte = (current_byte << 1) + int(readPin(DATA_PIN))
        #writePin(CLK_PIN, LOW)
        i += 1
    byte1 = current_byte

    current_byte = 0
    while i<24:
        pulsePin(CLK_PIN, -1, HIGH)
        #writePin(CLK_PIN, HIGH)
        current_byte = (current_byte << 1) + int(readPin(DATA_PIN))
        #writePin(CLK_PIN, LOW)
        i += 1
    byte0 = current_byte

    i = 0
    while i < gain:
        pulsePin(CLK_PIN, -1, HIGH)
        #writePin(CLK_PIN, HIGH)
        #writePin(CLK_PIN, LOW)
        i += 1

    # Pad up byte3 with the most significant bit of byte2:
    if byte2 & 0b10000000:
        byte3 = 0b11111111
    else:
        byte3 = 0b00000000

    return str((byte3<<8)|byte2) + " " + str((byte1<<8)|byte0)


def hx711_is_ready():
    return readPin(DATA_PIN) == LOW


def hx711_tare():
    global offset
