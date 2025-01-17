from original_code import Runner
import original_for_12_2
import unittest
from random import randint

class RunnerTest(unittest.TestCase):
    is_frozen = False
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

    def test_challenge(self):
        human_1 = Runner(f'name_{randint(1, 10)}')
        human_2 = Runner(f'name_{randint(1, 10)}')
        for i in range(10):
            human_1.run()
        for i in range(10):
            human_2.walk()
        self.assertNotEqual(human_1.distance, human_2.distance)




class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}


    def setUp(self):
        self.runner_1 = original_for_12_2.Runner('Усэйн', 10)
        self.runner_2 = original_for_12_2.Runner('Андрей', 9)
        self.runner_3 = original_for_12_2.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for k, v in TournamentTest.all_results.items():
            print(v)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_usain_nik(self):
        track_1 = original_for_12_2.Tournament(90, self.runner_1, self.runner_3)
        result_1 = track_1.start()
        runner_list = list(result_1.values()) #записаны имена бегунов
        TournamentTest.all_results['track_1'] = result_1
        self.assertTrue(runner_list[-1] == 'Ник', 'Ник должен быть последним')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_andrey_nik(self):
        track_2 = original_for_12_2.Tournament(90, self.runner_2, self.runner_3)
        result_2 = track_2.start()
        runner_list = list(result_2.values())
        TournamentTest.all_results['track_2'] = result_2
        self.assertTrue(runner_list[-1] == 'Ник', 'Ник должен быть последним')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_usain_andrey_nik(self):
        track_3 = original_for_12_2.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result_3 = track_3.start()
        runner_list = list(result_3.values())
        TournamentTest.all_results['track_3'] = result_3
        self.assertTrue(runner_list[-1] == 'Ник', 'Ник должен быть последним')

if __name__ == '__main__':
    unittest.main()


