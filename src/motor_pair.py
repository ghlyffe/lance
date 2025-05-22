import motor

PAIR_1 = 0
PAIR_2 = 1
PAIR_3 = 2

pair_to_text = {PAIR_1:"PAIR_1",PAIR_2:"PAIR_2",PAIR_3:"PAIR_3"}

pairs = {}
paired_ports = set()

def reset():
    global pairs
    global paired_ports
    pairs = {}
    paired_ports = set()


def stop(pair: int, *, stop: int = motor.BRAKE) -> None:
    """
    Stops a Motor Pair.
    """
    pass

def pair(pair: int, left_motor: int, right_motor: int) -> None:
    """
    pair two motors (left_motor & right_motor) and store the paired motors in pair.
    Use pair in all subsequent motor_pair related function calls.
    """
    global pairs
    global paired_ports
    # Bounds checks
    if (pair < 0) or (pair > 2): # The "stop using your own values" block
        raise ValueError()
    elif (left_motor < 0) or (left_motor > 5):
        raise ValueError()
    elif (right_motor < 0) or (right_motor > 5):
        raise ValueError()
    # Now the "These aren't motors" block
    elif not motor.get_motor(left_motor):
        raise OSError("[Errno 19] ENODEV")
    elif not motor.get_motor(right_motor):
        raise OSError("[Errno 19] ENODEV")
    # And lastly, the "Reusing is bad actually" block
    elif pair in pairs.keys():
        raise RuntimeError() # Have to unpair before pairing again
    elif left_motor in paired_ports:
        raise ValueError() # Port already in use
    elif right_motor in paired_ports:
        raise ValueError() # Port already in use
    
    # If we get here, pairing is valid
    pairs[pair] = (left_motor, right_motor)
    paired_ports.add(left_motor)
    paired_ports.add(right_motor)

def unpair(pair: int) -> None:
    """
    Unpair a Motor Pair.
    """
    global pairs
    global paired_ports
    # Bounds checks
    if pair not in pairs.keys():
        raise ValueError() # Can't unpair something that was never paired
    
    ports = pairs[pair]
    del pairs[pair]
    for p in ports:
        paired_ports.remove(p)

def move(pair: int, steering: int, *, velocity: int = 360, acceleration: int = 1000) -> None:
    """
    Move a Motor Pair at a constant speed until a new command is given.
    """
    if pair not in pairs.keys():
        raise ValueError()
    
    left,right = pairs[pair]
    l = motor.get_motor(left)
    r = motor.get_motor(right)
    #TODO: Work out steering
    l.move(velocity, acceleration)
    r.move(velocity, acceleration)

def move_tank(pair: int, left_velocity: int, right_velocity: int, *, acceleration: int = 1000) -> None:
    """
    Perform a tank move on a Motor Pair at a constant speed until a new command is given.
    """
    pass

async def move_for_degrees(pair: int, degrees: int, steering: int, *, 
                           velocity: int = 360, stop: int = motor.BRAKE, 
                           acceleration: int = 1000, deceleration: int = 1000):
    """
    Move a Motor Pair at a constant speed for a specific number of degrees.
    When awaited returns a status of the movement that corresponds to one of the following constants from the motor module:

    motor.READY
    motor.RUNNING
    motor.STALLED
    motor.CANCELED
    motor.ERROR
    motor.DISCONNECTED
    """
    pass

async def move_for_time(pair: int, duration: int, steering: int, *, 
                        velocity: int = 360, stop: int = motor.BRAKE, 
                        acceleration: int = 1000, deceleration: int = 1000):
    """
    Move a Motor Pair at a constant speed for a specific duration.
    When awaited returns a status of the movement that corresponds to one of the following constants from the motor module:

    motor.READY
    motor.RUNNING
    motor.STALLED
    motor.CANCELED
    motor.ERROR
    motor.DISCONNECTED
    """
    pass

async def move_tank_for_degrees(pair: int, degrees: int, left_velocity: int, right_velocity: int, *, 
                                stop: int = motor.BRAKE, acceleration: int = 1000, 
                                deceleration: int = 1000):
    """
    Perform a tank move on a Motor Pair at a constant speed until a new command is given.
    When awaited returns a status of the movement that corresponds to one of the following constants from the motor module:

    motor.READY
    motor.RUNNING
    motor.STALLED
    motor.CANCELED
    motor.ERROR
    motor.DISCONNECTED
    """
    pass

async def move_tank_for_time(pair: int, left_velocity: int, right_velocity: int, duration: int, *, 
                             stop: int = motor.BRAKE, acceleration: int = 1000, 
                             deceleration: int = 1000):
    """
    Perform a tank move on a Motor Pair at a constant speed for a specific amount of time.
    When awaited returns a status of the movement that corresponds to one of the following constants from the motor module:

    motor.READY
    motor.RUNNING
    motor.STALLED
    motor.CANCELLED
    motor.ERROR
    motor.DISCONNECTED
    """
    pass