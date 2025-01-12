from original_code import Runner
import unittest
from random import randint

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        human_1 = Runner(f'name_{randint(1, 10)}')
        for i in range(10):
            human_1.walk()
        self.assertEqual(human_1.distance, 50)
    def test_run(self):
        human_1 = Runner(f'name_{randint(1, 10)}')
        for i in range(10):
            human_1.run()
        self.assertEqual(human_1.distance, 100)

    def test_chakllenge(self):
        human_1 = Runner(f'name_{randint(1, 10)}')
        human_2 = Runner(f'name_{randint(1, 10)}')
        for i in range(10):
            human_1.run()
        for i in range(10):
            human_2.walk()
        self.assertNotEqual(human_1.distance, human_2.distance)
if __name__ == '__main__':
    unittest.nain()
