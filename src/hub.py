import motor
import sensor
import color_sensor
import distance_sensor

class port:
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5


class Hub(object):
    def stop(self):
        pass

class Spike(Hub):
    def __init__(self, conf):
        self.__ports_connected = conf["ports"].keys()
        self.__peripherals = {}
        self.__expect_input = False
        for p in self.__ports_connected:
            self.__make_peripheral(p,conf["ports"][p])

    def __string_to_port(self,port : str):
        if len(port) != 1:
            raise ValueError()
        val = ord(port)
        if (val < 65) or (val > 70):
            raise ValueError()
        return val - 65
    
    def __make_peripheral(self,p,conf):
        port = self.__string_to_port(p)
        t = conf["type"]
        s = conf["subtype"]
        if t == "motor":
            m = motor.Motor(s)
            self.__peripherals[port] = m
            motor.add_motor(port,m)
        elif t == "sensor":
            self.__expect_input = True
            sen = None
            if s == "colour":
                sen = color_sensor.ColourSensor()
            elif s == "distance":
                sen = distance_sensor.DistanceSensor()
            else:
                raise ValueError()
            self.__peripherals[port] = sen
            sensor.add_sensor(port, sen)
        else:
            raise ValueError()
        
    def stop(self):
        for p in self.__peripherals.keys():
            self.__peripherals[p].stop()
    

hubs_available = {"SPIKE": Spike}