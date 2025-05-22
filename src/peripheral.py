class Peripheral(object):
    def __init__(self):
        self.stopped = False

    def stop(self):
        self.stopped = True

    def access(self) -> None:
        if self.stopped:
            raise KeyboardInterrupt()