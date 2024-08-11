import unittest
import Runner

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        self.Garry = Runner.Runner('Garry')
        for run in range(10):
            self.Garry.walk()

        self.assertEqual((self.Garry.distance), 50)


    def test_run(self):
        self.Harry = Runner.Runner('Harry')
        for run in range(10):
            self.Harry.run()

        self.assertEqual((self.Harry.distance), 100)

    def test_challenge(self):
        self.Parry = Runner.Runner('Parry')
        for run in range(10):

            self.Parry.run()
        self.Rorry = Runner.Runner('Rorry')
        for run in range(10):
            self.Rorry.walk()


        self.assertNotEqual(self.Rorry.distance, self.Parry.distance)
