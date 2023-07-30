import os
import sys
import unittest
import random

from itertools import cycle

from unittest.mock import patch

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
         # Create two parent individuals for crossover
        parent1 = Individual(self.target_solution)  
        parent1.set_single_gene(0, 0)
        parent1.set_single_gene(1, 1)
        parent1.set_single_gene(2, 0)
        parent1.set_single_gene(3, 1)
        parent1.set_single_gene(4, 0)  #[0, 1, 0, 1, 0]

        parent2 = Individual(self.target_solution)  
        parent2.set_single_gene(0, 1)
        parent2.set_single_gene(1, 1)
        parent2.set_single_gene(2, 0)
        parent2.set_single_gene(3, 1)
        parent2.set_single_gene(4, 0) #[1, 1, 0, 1, 0]

        # Set the value to be returned by the mock random_gen.random() method
        # if random_gen.random()<SimpleGeneticAlgorithm.uniform_rate: this condition is set false
        mock_random_value = SimpleGeneticAlgorithm.uniform_rate + 0.1

        # Use the patch decorator to mock the random_gen.random() method
        with patch.object(random, 'Random') as mock_random_gen:
            random_gen_instance = mock_random_gen.return_value
            random_gen_instance.random.return_value = mock_random_value

            # Perform crossover with the mocked random_gen.random()
            child = self.ga.crossover(parent1, parent2)

        # The child should inherit the genes from parent2 since the condition is always false
        self.assertEqual(child.genes, parent2.genes)

    def test_mutate(self):
        # Create an individual for mutation
        individual = Individual(self.target_solution)  
        individual.set_single_gene(0, 0)
        individual.set_single_gene(1, 1)
        individual.set_single_gene(2, 1)
        individual.set_single_gene(3, 1)
        individual.set_single_gene(4, 0)  #[0, 1, 1, 1, 0]

        # Set the value to be returned by the mock random_gen.random() method
        mock_random_value = SimpleGeneticAlgorithm.mutation_rate - 0.1

        # Use the patch decorator to mock the random_gen.random() method
        with patch.object(random, 'Random') as mock_random_gen:
            random_gen_instance = mock_random_gen.return_value
            random_gen_instance.random.return_value = mock_random_value

            # Perform mutation with the mocked random_gen.random()
            self.ga.mutate(individual)

        # All genes should be flipped since the condition is always true
        expected_genes = [1, 0, 0, 0, 1]
        self.assertEqual(individual.genes, expected_genes)

    def test_tournament_selection(self):
        # Create a population with specific individuals and their fitness values
        population = Population(self.population_size, self.target_solution, initialize=True)
        population.get_individual(0).set_single_gene(0, 0)
        population.get_individual(1).set_single_gene(0, 0)
        population.get_individual(2).set_single_gene(0, 1)
        population.get_individual(3).set_single_gene(0, 0)
        population.get_individual(4).set_single_gene(0, 0)

        # Set the indices to be returned by the mock random_gen.randint() method
        mock_random_values = cycle([0, 2, 4])

        # Use the patch decorator to mock the random_gen.randint() method
        with patch.object(random, 'Random') as mock_random_gen:
            random_gen_instance = mock_random_gen.return_value
            random_gen_instance.randint.side_effect = lambda a, b: next(mock_random_values)

            # Perform tournament selection with the mocked random_gen.randint()
            tournament_winner = self.ga.tournament_selection(population)

        # The tournament winner should be the individual with the highest fitness (gene value = 1),
        # which is the third individual in this case
        third_individual_genes = population.get_individual(2).genes
        tournament_winner_genes = tournament_winner.genes
        self.assertTrue(tournament_winner_genes == third_individual_genes)

    def test_run_algorithm(self):
        pass

if __name__ == '__main__':
    unittest.main()
