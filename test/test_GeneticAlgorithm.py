import sys
import random
import unittest
from unittest.mock import patch

#append the project root directory that contains the two 'test' and 'GeneticAlgorithm' directories 
sys.path.append('C:/Users/Sarwe/OneDrive/Desktop/Non-Spaghetti')

from GeneticAlgorithm.GenAlgorithm import SimpleGeneticAlgorithm
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
        # Create an individual with known genes for testing
        indiv = Individual(self.target_solution)  # Pass the target_solution to Individual constructor
        indiv.set_single_gene(0, 0)
        indiv.set_single_gene(1, 0)
        indiv.set_single_gene(2, 0)
        indiv.set_single_gene(3, 0)
        indiv.set_single_gene(4, 0)

        # Mock random_gen.random() to always return a value less than or equal to SimpleGeneticAlgorithm.mutation_rate
        with patch.object(random, 'Random') as mock_random_gen:
            random_gen_instance = mock_random_gen.return_value
            #if random<=mutation rate, mutation happens in our algorithm logic. So assigning them equal.
            random_gen_instance.random.side_effect = lambda: SimpleGeneticAlgorithm.mutation_rate

            # Perform mutation
            self.ga.mutate(indiv)

        # Assert that the genes have been mutated (flipped)
        expected_genes = [1, 1, 1, 1, 1]
        self.assertEqual(indiv.genes, expected_genes)

    def test_tournament_selection(self):
        # Create a population with specific individuals and their fitness values
        population = Population(self.population_size, self.target_solution, initialize=True)
        population.get_individual(0).set_single_gene(0, 0)
        population.get_individual(1).set_single_gene(0, 0)
        population.get_individual(2).set_single_gene(0, 1)
        population.get_individual(3).set_single_gene(0, 0)
        population.get_individual(4).set_single_gene(0, 0)

        # Calculate and set the fitness values for each individual in the population
        for individual in population.individuals:
            fitness = Individual.get_fitness(individual)
            individual.fitness = fitness

        # Mock random_gen to return specific indices for the tournament (0, 2, 4) in sequence
        def mock_randint(a, b):
            return [0, 2, 4].pop(0)

        with patch.object(random, 'Random') as mock_random_gen:
            random_gen_instance = mock_random_gen.return_value
            random_gen_instance.randint.side_effect = mock_randint

            tournament_winner = self.ga.tournament_selection(population)

        # The tournament winner should be the individual with the highest fitness (gene value = 1)
        self.assertEqual(tournament_winner.get_single_gene(0), 1)

        # Check if the tournament_winner has the same genes as individual2
        third_individual_genes = population.get_individual(2).genes
        tournament_winner_genes = tournament_winner.genes
        self.assertTrue(tournament_winner_genes == third_individual_genes)

if __name__ == '__main__':
    unittest.main()