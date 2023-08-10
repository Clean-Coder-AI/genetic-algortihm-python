from Individual import Individual
import random

class EvolutionTools:

    def crossover(individual1, individual2):
        individual = Individual(len(individual1.get_genes()))
        for i in range(len(individual1.get_genes())):
            if random.random() < 0.5:
                individual.get_genes()[i] = individual1.get_genes()[i]
            else:
                individual.get_genes()[i] = individual2.get_genes()[i]
        return individual