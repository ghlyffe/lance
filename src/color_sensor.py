from sensor import Sensor,get_sensor
import color as cl

class ColourSensor(Sensor):
    def get_colour(self):
        data = self.read()
        #Do something
        return (0,0,0,0,0)

def color(port : int) -> int:
    """
    Returns the colour value of the detected colour. 
    Use the color module to map the colour value to a specific colour.
    """
    s = get_sensor(port,ColourSensor)
    raw = s.get_colour()
    #conver to color
    if raw[3] <= 100:
        return cl.BLACK
    elif raw[0:3] == (0,0,0):
        return cl.BLACK
    elif raw[0] >= raw[1]+100 and raw[0]>= raw[2]+100 and raw[3] >= 500:
        return cl.RED
    elif raw[1] >= raw[0]+100 and raw[1]>= raw[2]+100 and raw[3] >= 500:
        return cl.GREEN
    elif raw[2] >= raw[0]+100 and raw[2]>= raw[1]+100 and raw[3] >= 500:
        return cl.BLUE

def reflection(port : int) -> int:
    """
    Retrieves the intensity of the reflected light (0-100%).
    """
    pass

def rgbi(port: int) -> tuple[int,int,int,int]:
    """
    Retrieves the overall colour intensity and intensity of red, green and blue.
    Returns tuple[red: int, green: int, blue: int, intensity: int]
    """
    s = get_sensor(port,ColourSensor)
    return s.get_colour()[0:4]