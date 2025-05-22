from peripheral import Peripheral

sim_sensors = {}

class Sensor(Peripheral):
    def __init__(self):
        super().__init__()
        
    def read(self):
        self.access()

def add_sensor(port, obj : Sensor):
    global sim_sensors
    sim_sensors[port] = obj

def get_sensor(port,type_check=None):
    if port in sim_sensors.keys():
        if (not type_check) or isinstance(sim_sensors[port],type_check):
            return sim_sensors[port]
    raise OSError("[Errno 19] ENODEV")
