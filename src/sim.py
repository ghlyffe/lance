class Simulator(object):
    def __init__(self):
        self.__inputs = None

    def load_model(self, filename):
        import config_load
        self.__model = config_load.load_config(filename)

    def get_time(self):
        """
        USed by simulation entities to get the current virtual time
        """
        return 0

    def stop(self):
        self.__model.stop()