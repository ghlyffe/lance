import motor

PAIR_1 = 0
PAIR_2 = 1
PAIR_3 = 2

pair_to_text = {PAIR_1:"PAIR_1",PAIR_2:"PAIR_2",PAIR_3:"PAIR_3"}

pairs = {}
paired_ports = set()

async def stop(pair: int, *, stop: int = motor.BRAKE) -> None:
    pass

async def pair(pair: int, left_motor: int, right_motor: int) -> None:
    global pairs
    global paired_ports
    # Bounds checks
    if pair in pairs.keys():
        raise Exception() # Have to unpair before pairing again
    elif left_motor in paired_ports:
        raise Exception() # Port already in use
    elif right_motor in paired_ports:
        raise Exception() # Port already in use
    
    # If we get here, pairing is valid
    pairs[pair] = (left_motor, right_motor)
    paired_ports.add(left_motor)
    paired_ports.add(right_motor)

async def unpair(pair: int) -> None:
    global pairs
    global paired_ports
    # Bounds checks
    if pair not in pairs:
        raise Exception() # Can't unpair something that was never paired
    
    ports = pairs[pair]
    del pairs[pair]
    for p in ports:
        paired_ports.remove(p)