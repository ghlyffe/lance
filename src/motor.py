from peripheral import Peripheral

READY = 1
RUNNING = 2
STALLED = -1
CANCELED = -2
ERROR = -3
DISCONNECTED = 0
COAST = 1
BRAKE = 2
HOLD = 3
CONTINUE = 0
SMART_COAST = 4
SMART_BRAKE = 5
CLOCKWISE = 0
COUNTERCLOCKWISE = 1
SHORTEST_PATH = 2
LONGEST_PATH = 3

sim_motors = {}

class Motor(Peripheral):
    def __init__(self, size):
        super().__init__()
        self.__size = 0
        if size == "sml":
            self.__size = 178
        elif size == "med":
            self.__size = 280
        elif size == "lrg":
            self.__size = 1000
        else:
            raise ValueError()
        
    def move(self,*args,**kwargs):
        self.access()

def add_motor(port, obj):
    global sim_motors
    sim_motors[port] = obj

def get_motor(port):
    if port in sim_motors.keys():
        return sim_motors[port]
    return None

def absolute_position(port: int) -> int:
    """
    Get the absolute position of a motor
    """
    pass

def get_duty_cycle(port:int) -> int:
    """
    Get the PWM of a motor
    """
    pass

def relative_position(port: int) -> int:
    """
    Get the relative position of a motor.
    """
    pass

def reset_relative_position(port: int, position: int) -> None:
    """
    Change the position used as the offset when using the run_to_relative_position function.
    """
    pass

def run(port: int, velocity: int, *, acceleration: int = 1000) -> None:
    """
    Start a motor at a constant speed
    """
    pass

def set_duty_cycle(port:int, pwm:int) -> None:
    """
    Start a motor with a specific PWM
    """
    pass

def stop(port: int, *, stop: int = BRAKE) -> None:
    """
    Stops a motor.
    """
    pass

def velocity(port: int) -> int:
    """
    Get the velocity (deg/sec) of a Motor
    """
    pass

async def run_for_degrees(port: int, degrees: int, velocity: int, *, 
                          stop: int = BRAKE, acceleration: int = 1000, deceleration: int = 1000):
    """
    Turn a motor for a specific number of degrees
    When awaited returns a status of the movement that corresponds to one of the following constants:

    motor.READY
    motor.RUNNING
    motor.STALLED
    motor.CANCELED
    motor.ERROR
    motor.DISCONNECTED
    """
    pass

async def run_for_time(port: int, duration: int, velocity: int, *, 
                       stop: int = BRAKE, acceleration: int = 1000, deceleration: int = 1000):
    """
    Run a motor for a limited amount of time
    When awaited returns a status of the movement that corresponds to one of the following constants:

    motor.READY
    motor.RUNNING
    motor.STALLED
    motor.ERROR
    motor.DISCONNECTED
    """
    pass

async def run_to_absolute_position(port: int, position: int, velocity: int, *, 
                                   direction: int, stop: int = BRAKE, 
                                   acceleration: int = 1000, deceleration: int = 1000):
    """
    Turn a motor to an absolute position.
    When awaited returns a status of the movement that corresponds to one of the following constants:

    motor.READY
    motor.RUNNING
    motor.STALLED
    motor.CANCELED
    motor.ERROR
    motor.DISCONNECTED
    """
    pass

async def run_to_relative_position(port: int, position: int, velocity: int, *, 
                                   stop: int = BRAKE, 
                                   acceleration: int = 1000, deceleration: int = 1000):
    """
    Turn a motor to a position relative to the current position.
    When awaited returns a status of the movement that corresponds to one of the following constants:

    motor.READY
    motor.RUNNING
    motor.STALLED
    motor.CANCELED
    motor.ERROR
    motor.DISCONNECTED
    """
    pass