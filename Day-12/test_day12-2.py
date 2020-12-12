from unittest import TestCase
import importlib
s = importlib.import_module("day12-2")


class Test(TestCase):
    def test_move_ship(self):
        self.assertEqual((-13, 11), s.move_ship(-3, -7, -5, 9, 2))

    def rotate_waypoint(self):
        self.assertEqual(())
