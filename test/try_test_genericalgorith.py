import os
import sys
import unittest
import random

from itertools import cycle

from unittest.mock import patch, Magicmock

sys.path.append(r'C:\Users\user\Desktop\Genetic\genetic-algortihm-python')

from GeneticAlgorithm.GeneticAlgorithm import SimpleGeneticAlgorithm
from GeneticAlgorithm.Population import Population
from GeneticAlgorithm.Individual import Individual

class TestSimpleGeneticAlgorithm(unittest.TestCase):
    def setUp(self):
        self.target_solution = [1, 0, 1, 0, 1]
        self.population_size = 10
        self.ga = SimpleGeneticAlgorithm(self.target_solution, self.population_size)

    def test_crossover_random_less_than_uniform_rate(self):
        # Mock the random number generation to return a value less than uniform_rate
        with patch("random.random", MagicMock(return_value=self.ga.uniform_rate - 0.1)):
            parent1 = Individual(self.target_solution)
            parent1.set_single_gene(0, 0)
            parent1.set_single_gene(1, 1)
            parent1.set_single_gene(2, 0)
            parent1.set_single_gene(3, 1)
            parent1.set_single_gene(4, 0)  # [0, 1, 0, 1, 0]

            parent2 = Individual(self.target_solution)
            parent2.set_single_gene(0, 1)
            parent2.set_single_gene(1, 1)
            parent2.set_single_gene(2, 0)
            parent2.set_single_gene(3, 1)
            parent2.set_single_gene(4, 0)  # [1, 1, 0, 1, 0]

            # Perform crossover
            child = self.ga.crossover(parent1, parent2)

            # Assert that the child inherits all genes from parent1
            self.assertEqual(child.genes, parent1.genes)

    def test_crossover_random_greater_than_uniform_rate(self):
        # Mock the random number generation to return a value greater than uniform_rate
        with patch("random.random", MagicMock(return_value=self.ga.uniform_rate + 0.1)):
            parent1 = Individual(self.target_solution)
            parent1.set_single_gene(0, 0)
            parent1.set_single_gene(1, 1)
            parent1.set_single_gene(2, 0)
            parent1.set_single_gene(3, 1)
            parent1.set_single_gene(4, 0)  # [0, 1, 0, 1, 0]

            parent2 = Individual(self.target_solution)
            parent2.set_single_gene(0, 1)
            parent2.set_single_gene(1, 1)
            parent2.set_single_gene(2, 0)
            parent2.set_single_gene(3, 1)
            parent2.set_single_gene(4, 0)  # [1, 1, 0, 1, 0]

            # Perform crossover
            child = self.ga.crossover(parent1, parent2)

            # Assert that the child inherits all genes from parent2
            self.assertEqual(child.genes, parent2.genes)

    def test_crossover_random_equal_to_uniform_rate(self):
        # Mock the random number generation to return a value equal to uniform_rate
        with patch("random.random", MagicMock(return_value=self.ga.uniform_rate)):
            parent1 = Individual(self.target_solution)
            parent1.set_single_gene(0, 0)
            parent1.set_single_gene(1, 1)
            parent1.set_single_gene(2, 0)
            parent1.set_single_gene(3, 1)
            parent1.set_single_gene(4, 0)  # [0, 1, 0, 1, 0]

            parent2 = Individual(self.target_solution)
            parent2.set_single_gene(0, 1)
            parent2.set_single_gene(1, 1)
            parent2.set_single_gene(2, 0)
            parent2.set_single_gene(3, 1)
            parent2.set_single_gene(4, 0)  # [1, 1, 0, 1, 0]

            # Perform crossover
            child = self.ga.crossover(parent1, parent2)

            # Assert that the child's genes are a mix of parent1 and parent2
            self.assertNotEqual(child.genes, parent1.genes)
            self.assertNotEqual(child.genes, parent2.genes)

    def test_mutate_random_less_than_mutation_rate(self):
        # Mock the random number generation to return a value less than mutation_rate
        with patch("random.random", MagicMock(return_value=self.ga.mutation_rate - 0.001)):
            individual = Individual(self.target_solution)
            original_genes = list(individual.genes)

            # Perform mutation
            self.ga.mutate(individual)

            # Assert that the genes are unchanged (random_gen < mutation_rate)
            self.assertEqual(individual.genes, original_genes)

    def test_mutate_random_greater_than_mutation_rate(self):
        # Mock the random number generation to return a value greater than mutation_rate
        with patch("random.random", MagicMock(return_value=self.ga.mutation_rate + 0.001)):
            individual = Individual(self.target_solution)
            original_genes = list(individual.genes)

            # Perform mutation
            self.ga.mutate(individual)

            # Assert that some genes have changed (random_gen >= mutation_rate)
            self.assertNotEqual(individual.genes, original_genes)

    def test_mutate_random_equal_to_mutation_rate(self):
        # Mock the random number generation to return a value equal to mutation_rate
        with patch("random.random", MagicMock(return_value=self.ga.mutation_rate)):
            individual = Individual(self.target_solution)
            original_genes = list(individual.genes)

            # Perform mutation
            self.ga.mutate(individual)

            # Assert that some genes have changed (random_gen == mutation_rate)
            self.assertNotEqual(individual.genes, original_genes)

    def test_tournament_selection(self):
        # Create a population with specific individuals and their fitness values
        population = Population(self.population_size, self.target_solution, initialize=True)
        population.get_individual(0).set_single_gene(0, 0)
        population.get_individual(1).set_single_gene(0, 0)
        population.get_individual(2).set_single_gene(0, 1)
        population.get_individual(2).set_single_gene(1, 0)
        population.get_individual(2).set_single_gene(2, 1)
        population.get_individual(2).set_single_gene(3, 0)
        population.get_individual(2).set_single_gene(4, 1)
        population.get_individual(3).set_single_gene(0, 0)
        population.get_individual(4).set_single_gene(0, 0)

        # Set the indices to be returned by the mock random_gen.randint() method
        mock_random_values = cycle([0, 2, 4])

        # Use the patch decorator to mock the random_gen.randint() method
        with patch.object(random, 'Random') as mock_random_gen:
            random_gen_instance = mock_random_gen.return_value
            random_gen_instance.randint.side_effect = lambda a, b: next(mock_random_values)

            tournament_winner = self.ga.tournament_selection(population)

            # The tournament winner should be the individual with the highest fitness (gene value = 1)
            third_individual_genes = population.get_individual(2).genes
            tournament_winner_genes = tournament_winner.genes
            self.assertEqual(tournament_winner_genes, third_individual_genes)

    def test_run_algorithm(self):
        pass

if __name__ == '__main__':
    unittest.main()
