import asyncio
import threading
import time

import sim

def run(*entry):
    # Do setup
    simulator = sim.Simulator()
    simulator.load_model("test/resource/spike_three_motor_two_colour_distance.json")

    runner_threads = [threading.Thread(target = asyncio.run, args = [e], name = "asyncio runner") for e in entry]
    for t in runner_threads:
        t.start()

    try:
        while(True):
            time.sleep(1)
    except:
        pass

    simulator.stop()

    for t in runner_threads:
        t.join()