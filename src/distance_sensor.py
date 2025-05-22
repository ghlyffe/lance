from sensor import Sensor,get_sensor

class DistanceSensor(Sensor):
    pass


def distance(port: int) -> int:
    """
    Retrieve the distance in millimetres captured by the Distance Sensor connected to port.
    If the Distance Sensor cannot read a valid distance it will return -1.
    """
    s = get_sensor(port, DistanceSensor)
    s.read()


# These methods don't matter to the simulation since they don't affect the behaviour in any way
# They just turn on the or off the headlights on the distance sensor
def clear(port: int) -> None:
    """
    Turns off all the lights in the Distance Sensor connected to port.
    """
    pass

def get_pixel(port: int, x: int, y: int) -> int:
    """
    Retrieve the intensity of a specific light on the Distance Sensor connected to port.
    """
    pass

def set_pixel(port: int, x: int, y: int, intensity: int) -> None:
    """
    Changes the intensity of a specific light on the Distance Sensor connected to port.
    """
    pass

def show(port: int, pixels: list[int]) -> None:
    """
    Change all the lights at the same time.
    """
    pass