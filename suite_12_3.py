import module_12_3
import unittest

tournamentST = unittest.TestSuite()
tournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_3.RunnerTest))
tournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(tournamentST)
