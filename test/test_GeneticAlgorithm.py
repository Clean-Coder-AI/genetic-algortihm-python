import sys
import unittest


sys.path.append('C:/Users/Sarwe/OneDrive/Desktop/Non-Spaghetti')

from GeneticAlgorithm.GeneticAlgorithm import SimpleGeneticAlgorithm
from GeneticAlgorithm.Population import Population
from GeneticAlgorithm.Individual import Individual


class TestSimpleGeneticAlgorithm(unittest.TestCase):
    def setUp(self):
        self.target_solution = [1, 0, 1, 0, 1]
        self.population_size = 10
        self.ga = SimpleGeneticAlgorithm(self.target_solution, self.population_size)

    def test_crossover(self):
       pass

    def test_mutate(self):
        pass

    def test_tournament_selection(self):
        # Create a population with specific individuals and their fitness values
        population = Population(5, self.target_solution, initialize=True)
        population.get_individual(0).set_single_gene(0, 0)
        population.get_individual(1).set_single_gene(0, 0)
        population.get_individual(2).set_single_gene(0, 1)
        population.get_individual(3).set_single_gene(0, 0)
        population.get_individual(4).set_single_gene(0, 0)

        tournament_winner = self.ga.tournament_selection(population)

         # The tournament winner should be the individual with the highest fitness (gene value = 1)
        self.assertEqual(tournament_winner.get_single_gene(0), 1)

         # Check if the tournament_winner has the same genes as third individual
       
        third_individual_genes = population.get_individual(2).genes
        tournament_winner_genes = tournament_winner.genes

        self.assertTrue(tournament_winner_genes == third_individual_genes)
      


    def test_run_algorithm(self):
        pass

if __name__ == '__main__':
    unittest.main()

