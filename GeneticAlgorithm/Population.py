from GeneticAlgorithm.Individual import Individual


class Population:
    def __init__(self, population_size, target_solution, initialize=True):
        self.individuals = []
        self.solution = target_solution

        if initialize:
            for _ in range(population_size):
                self.individuals.append(Individual(self.solution))

    def size(self):
        return len(self.individuals)

    def get_individuals(self):
        return self.individuals

    def get_individual(self, index):
        return self.individuals[index]

    def get_fittest(self):
        return max(self.individuals, key=lambda ind: ind.get_fitness())
