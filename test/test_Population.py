import sys
import unittest


sys.path.append('C:/Users/Sarwe/OneDrive/Desktop/Non-Spaghetti')


from GeneticAlgorithm.Population import Population, Individual

class TestPopulation(unittest.TestCase):
    def setUp(self):
        self.target_solution = [1, 0, 1, 0, 1]
        self.population_size=5
        self.population=Population(self.population_size,self.target_solution, initialize=True)

    def test_size(self):
        self.assertEqual(self.population.size(), self.population_size)

    def test_get_individuals(self):
        individuals=self.population.get_individuals()
        self.assertEqual(len(individuals), self.population_size)
        for individual in individuals:
            self.assertIsInstance(individual, Individual)

    def test_get_individual(self):
        index=2
        individual=self.population.get_individual(index)
        self.assertIsInstance(individual, Individual)
        self.assertEqual(individual, self.population.get_individuals()[index])

    def test_get_fittest(self):
        fittest=self.population.get_fittest()
        self.assertIsInstance(fittest, Individual)
        self.assertEqual(fittest.get_fitness(), max(ind.get_fitness() for ind in self.population.get_individuals()))




if __name__ == '__main__':
    unittest.main()

