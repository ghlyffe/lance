import motor
import motor_pair
from src.hub import port
import src.hub as hub
import runloop

async def main():
    motor_pair.pair(motor_pair.PAIR_1,port.A,port.E)
    motor_pair.move(motor_pair.PAIR_1, 0)
    motor_pair.unpair(motor_pair.PAIR_1)



def check():
    import sim
    assert(sim.location(spike) == [origin])
    runloop.run(main())
    assert(sim.location(spike) == [something])