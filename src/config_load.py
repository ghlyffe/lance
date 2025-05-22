import motor
from hub import Hub,hubs_available

class Model(object):
    def __init__(self, conf):
        self.__hubs = []
        self.__setup(conf)

    def __setup(self, conf):
        for h in conf:
            if h["hub_type"] not in hubs_available:
                raise Exception()
            
            hub = hubs_available[h["hub_type"]](h["description"])
            self.add_hub(hub)

    def add_hub(self, hub : Hub):
        self.__hubs.append(hub)


    def stop(self):
        for h in self.__hubs:
            h.stop()

def load_config(file):
    import json
    conf = json.load(open(file,"r"))
    model = Model(conf["model"])
    return model