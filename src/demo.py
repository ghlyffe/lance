import motor
import motor_pair
import color_sensor
import color
from hub import port
import hub
import runloop


async def main():
    import motor_pair
    motor_pair.pair(motor_pair.PAIR_1,port.A,port.E)
    motor_pair.move(motor_pair.PAIR_1, 0)

async def read_colours():
    while True:
        while color_sensor.color(port.B) != color.RED:
            continue
        print("Red detected")

runloop.run(main(),read_colours())