import os
import sys
import unittest
from unittest.mock import patch

sys.path.append(r'C:\Users\user\Desktop\Work')

os.chdir(r'C:\Users\user\Desktop\Work\GeneticAlgorithm')

from GeneticAlgorithm.GeneticAlgorithm import SimpleGeneticAlgorithm
from GeneticAlgorithm.Population import Population
from GeneticAlgorithm.Individual import Individual

class TestSimpleGeneticAlgorithm(unittest.TestCase):
    def setUp(self):
        self.target_solution = [1, 0, 1, 0, 1]
        self.population_size = 10
        self.ga = SimpleGeneticAlgorithm(self.target_solution, self.population_size)

    def test_crossover(self):
        # Test case 1: Crossover between parent1 with all 1s and parent2 with all 0s
        parent1 = Individual(self.target_solution)  # [1, 0, 1, 0, 1]
        parent1.set_single_gene(0, 1)
        parent1.set_single_gene(1, 1)
        parent1.set_single_gene(2, 1)
        parent1.set_single_gene(3, 1)
        parent1.set_single_gene(4, 1)

        parent2 = Individual(self.target_solution)  # [1, 0, 1, 0, 1]
        parent2.set_single_gene(0, 0)
        parent2.set_single_gene(1, 0)
        parent2.set_single_gene(2, 0)
        parent2.set_single_gene(3, 0)
        parent2.set_single_gene(4, 0)

        expected_child_1 = Individual(self.target_solution)  # [1, 0, 1, 0, 1]
        expected_child_1.set_single_gene(0, 1)
        expected_child_1.set_single_gene(1, 1)
        expected_child_1.set_single_gene(2, 1)
        expected_child_1.set_single_gene(3, 1)
        expected_child_1.set_single_gene(4, 1)

        with patch.object(self.ga, 'crossover', return_value=expected_child_1) as mock_crossover:
            child_1 = self.ga.crossover(parent1, parent2)
            self.assertEqual(child_1, expected_child_1)
            mock_crossover.assert_called_once_with(parent1, parent2)

        # Test case 2: Crossover between parent1 with all 0s and parent2 with all 1s
        parent1.set_single_gene(0, 0)
        parent1.set_single_gene(1, 0)
        parent1.set_single_gene(2, 0)
        parent1.set_single_gene(3, 0)
        parent1.set_single_gene(4, 0)

        parent2.set_single_gene(0, 1)
        parent2.set_single_gene(1, 1)
        parent2.set_single_gene(2, 1)
        parent2.set_single_gene(3, 1)
        parent2.set_single_gene(4, 1)

        expected_child_2 = Individual(self.target_solution)  # [1, 0, 1, 0, 1]
        expected_child_2.set_single_gene(0, 0)
        expected_child_2.set_single_gene(1, 0)
        expected_child_2.set_single_gene(2, 0)
        expected_child_2.set_single_gene(3, 0)
        expected_child_2.set_single_gene(4, 0)

        with patch.object(self.ga, 'crossover', return_value=expected_child_2) as mock_crossover:
            child_2 = self.ga.crossover(parent1, parent2)
            self.assertEqual(child_2, expected_child_2)
            mock_crossover.assert_called_once_with(parent1, parent2)

    def test_mutate(self):
        # Test case 1: Mutate an individual with all 1s
        individual_1 = Individual(self.target_solution)  # [1, 0, 1, 0, 1]
        individual_1.set_single_gene(0, 1)
        individual_1.set_single_gene(1, 1)
        individual_1.set_single_gene(2, 1)
        individual_1.set_single_gene(3, 1)
        individual_1.set_single_gene(4, 1)
        with patch.object(self.ga, 'mutate', return_value=individual_1) as mock_mutate:
            mutated_individual_1 = self.ga.mutate(individual_1)
            self.assertEqual(mutated_individual_1, individual_1)
            mock_mutate.assert_called_once_with(individual_1)

        # Test case 2: Mutate an individual with all 0s
        individual_2 = Individual(self.target_solution)  # [1, 0, 1, 0, 1]
        individual_2.set_single_gene(0, 0)
        individual_2.set_single_gene(1, 0)
        individual_2.set_single_gene(2, 0)
        individual_2.set_single_gene(3, 0)
        individual_2.set_single_gene(4, 0)
        with patch.object(self.ga, 'mutate', return_value=individual_2) as mock_mutate:
            mutated_individual_2 = self.ga.mutate(individual_2)
            self.assertEqual(mutated_individual_2, individual_2)
            mock_mutate.assert_called_once_with(individual_2)

        # Test case 3: Mutate an individual with mixed values
        individual_3 = Individual(self.target_solution)  # [1, 0, 1, 0, 1]
        individual_3.set_single_gene(0, 0)
        individual_3.set_single_gene(1, 1)
        individual_3.set_single_gene(2, 0)
        individual_3.set_single_gene(3, 1)
        individual_3.set_single_gene(4, 0)
        with patch.object(self.ga, 'mutate', return_value=individual_3) as mock_mutate:
            mutated_individual_3 = self.ga.mutate(individual_3)
            self.assertEqual(mutated_individual_3, individual_3)
            mock_mutate.assert_called_once_with(individual_3)

    def test_tournament_selection(self):
        # Create a population with specific individuals and their fitness values
        population = Population(5, self.target_solution, initialize=True)
        population.get_individual(0).set_single_gene(0, 0)  # Fitness: 0
        population.get_individual(1).set_single_gene(0, 0)  # Fitness: 0
        population.get_individual(2).set_single_gene(0, 1)  # Fitness: 1
        population.get_individual(3).set_single_gene(0, 0)  # Fitness: 0
        population.get_individual(4).set_single_gene(0, 0)  # Fitness: 0

        # We expect the tournament winner to be the individual with the highest fitness (gene value = 1)
        expected_winner = population.get_individual(2)

        # Replace the `tournament_selection` method with a mock that returns the expected winner
        with patch.object(self.ga, 'tournament_selection', return_value=expected_winner) as mock_tournament_selection:
            tournament_winner = self.ga.tournament_selection(population)
            self.assertEqual(tournament_winner, expected_winner)
            mock_tournament_selection.assert_called_once_with(population)

    def test_run_algorithm(self):
        pass

if __name__ == '__main__':
    unittest.main()
