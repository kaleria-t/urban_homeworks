import unittest
import original_for_12_2

class TournamentTest(unittest.TestCase):

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
            
    def test_tournament_usain_nik(self):
        track_1 = original_for_12_2.Tournament(90, self.runner_1, self.runner_3)
        result_1 = track_1.start()
        runner_list = list(result_1.values()) #записаны имена бегунов
        TournamentTest.all_results['track_1'] = result_1
        self.assertTrue(runner_list[-1] == 'Ник', 'Ник должен быть последним')

    def test_tournament_andrey_nik(self):
        track_2 = original_for_12_2.Tournament(90, self.runner_2, self.runner_3)
        result_2 = track_2.start()
        runner_list = list(result_2.values())
        TournamentTest.all_results['track_2'] = result_2
        self.assertTrue(runner_list[-1] == 'Ник', 'Ник должен быть последним')

    def test_tournament_usain_andrey_nik(self):
        track_3 = original_for_12_2.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result_3 = track_3.start()
        runner_list = list(result_3.values())
        TournamentTest.all_results['track_3'] = result_3
        self.assertTrue(runner_list[-1] == 'Ник', 'Ник должен быть последним')

if __name__ == '__main__':
    unittest.main()



