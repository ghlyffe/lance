import motor_pair
import port

import unittest

class test_motor_pair(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        motor_pair.reset()

    def assertNoExcept(self, callbale, *args, **kwargs):
        try:
            callable(*args,**kwargs)
        except:
            self.fail("Raised an unexpected exception")

    def test_pair(self):
        self.assertNoExcept(motor_pair.pair, motor_pair.PAIR_1, port.A, port.E)
        self.assertRaises(RuntimeError, motor_pair.pair, motor_pair.PAIR_1, port.B, port.C)
        self.assertRaises(ValueError, motor_pair.pair, motor_pair.PAIR_2, port.A, port.C)
        self.assertRaises(ValueError, motor_pair.pair, 7, port.B, port.C)
        self.assertRaises(ValueError, motor_pair.pair, motor_pair.PAIR_2, 7, port.D)

        motor_pair.unpair(motor_pair.PAIR_1)
        self.assertNoExcept(motor_pair.pair,motor_pair.PAIR_1, port.A, port.E)
        self.assertNoExcept(motor_pair.pair,motor_pair.PAIR_2, port.B, port.D)
        self.assertNoExcept(motor_pair.pair,motor_pair.PAIR_3, port.C, port.F)

    def test_unpair(self):
        motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)
        self.assertNoExcept(motor_pair.unpair, motor_pair.PAIR_1)
        self.assertRaises(RuntimeError, motor_pair.unpair, motor_pair.PAIR_1)
        self.assertRaises(RuntimeError, motor_pair.unpair, motor_pair.PAIR_2)
        self.assertRaises(ValueError, motor_pair.unpair, motor_pair.5)

    def test_move(self):
        pass