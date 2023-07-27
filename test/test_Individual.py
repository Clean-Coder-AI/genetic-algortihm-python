import sys
import unittest


sys.path.append('C:/Users/Sarwe/OneDrive/Desktop/Non-Spaghetti')

from GeneticAlgorithm.Individual import Individual

class TestIndividual(unittest.TestCase):

    def setUp(self):
        self.target_solution = [1, 0, 1, 0, 1]
        self.individual = Individual(self.target_solution)

    def test_default_gene_length(self):
        self.assertEqual(self.individual.default_gene_length(), len(self.target_solution))

    def test_get_single_gene(self):
        for i in range(len(self.target_solution)):
            self.assertIn(self.individual.get_single_gene(i), [0, 1])

    def test_set_single_gene(self):
        original_gene = self.individual.get_single_gene(0)
        self.individual.set_single_gene(0, 1 - original_gene)
        self.assertNotEqual(self.individual.get_single_gene(0), original_gene)

    def test_get_fitness(self):
        # Since the fitness calculation depends on the target_solution, need to test it manually
        self.individual.set_single_gene(0, 1)
        self.assertGreaterEqual(self.individual.get_fitness(), 1)
        self.assertLessEqual(self.individual.get_fitness(), 5)

    def test_clone(self):
        clone = self.individual.clone()
        self.assertIsNot(clone, self.individual)
        self.assertEqual(clone.get_fitness(), self.individual.get_fitness())
        self.assertEqual(clone.default_gene_length(), self.individual.default_gene_length())

if __name__ == '__main__':
    unittest.main()
