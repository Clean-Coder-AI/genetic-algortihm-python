import random
from Individual import Individual,Climate
from EvolutionTools import EvolutionTools

class Population:
    def __init__(self, population_size, number_of_genes):
        self.individuals = [Individual(number_of_genes) for _ in range(population_size)]

    def get_individuals(self):
        return self.individuals

    def get_fittest(self, climate):
        fittest = self.individuals[0]
        for individual in self.individuals:
            if individual.get_fitness(climate) > fittest.get_fitness(climate):
                fittest = individual
        return fittest
    
    def tournament_selection(self, climate, tournament_size):
        tournament = Population(tournament_size, len(self.individuals[0].get_genes()))
        for i in range(tournament_size):
            random_index = random.randint(0, len(self.individuals) - 1)
            tournament.get_individuals()[i] = self.individuals[random_index]
        return tournament.get_fittest(climate)
    

    def evolve_v2(self, climate, mutation_rate, random_selection_percentage):
        new_individuals = []
        sorted_individuals = self.sorted_individuals_by_fitness(climate)
        top_individual = sorted_individuals[0]

        if top_individual.get_fitness(climate) < 0.2 * len(top_individual.get_genes()):
            return Population(0, 0)

        top_individuals = sorted_individuals[:int(0.2 * len(sorted_individuals))]
        bottom_individuals = sorted_individuals[int(0.2 * len(sorted_individuals)):]

        # print("Top Individuals:")
        # for individual in top_individuals:
        #     print(f"Genes: {individual.get_genes()}, Fitness: {individual.get_fitness(climate)}")

        # print("\nBottom Individuals:")
        # for individual in bottom_individuals:
        #     print(f"Genes: {individual.get_genes()}, Fitness: {individual.get_fitness(climate)}")

        top_individual_babies = self.get_top_babies(mutation_rate, top_individuals)
        new_individuals.extend(top_individual_babies)

        # print("New Individuals after adding top individual babies:")
        # for individual in new_individuals:
        #     print(f"Genes: {individual.get_genes()}, Fitness: {individual.get_fitness(climate)}")

        if random_selection_percentage > 0:
            random_babies = self.mate_random_individuals(mutation_rate, random_selection_percentage, sorted_individuals)
            new_individuals.extend(random_babies)

        if len(new_individuals) < len(sorted_individuals):
            bottom_babies = self.get_bottom_babies(mutation_rate, new_individuals, sorted_individuals, bottom_individuals)
            new_individuals.extend(bottom_babies)

        # print("New Individuals after adding top,random,and bottom babies:")
        # for individual in new_individuals:
        #     print(f"Genes: {individual.get_genes()}, Fitness: {individual.get_fitness(climate)}")

        return Population(len(new_individuals), len(self.individuals[0].get_genes()))

    def get_average_fitness(self, climate):
        total_fitness = sum(individual.get_fitness(climate) for individual in self.individuals)
        return total_fitness / len(self.individuals)
 
    def get_bottom_babies(self, mutation_rate, new_individuals, sorted_individuals, bottom_individuals):
        bottom_babies = []
        # print(len(sorted_individuals) - len(new_individuals), len(sorted_individuals), len(new_individuals))
        for i in range(len(sorted_individuals) - len(new_individuals)):
            individual1 = bottom_individuals[i]
            random_index = random.randint(0, len(bottom_individuals) - 2)
            if random_index == i:
                random_index += 1
            individual2 = bottom_individuals[random_index]
            individual = EvolutionTools.crossover(individual1.mutate(mutation_rate),
                                                  individual2.mutate(mutation_rate))
            bottom_babies.append(individual)
        # print("Bottom Babies:")
        # for ind in bottom_babies:
        #     print(f"Genes: {ind.get_genes()}, Fitness: {ind.get_fitness(Climate.COLD)}")
        return bottom_babies

    def get_top_babies(self, mutation_rate, top_individuals):
        top_individual_babies = []
        # print(len(top_individuals))
        for i in range(len(top_individuals)):
            for _ in range(3):
                individual1 = top_individuals[i]
                individual2 = top_individuals[random.randint(0, len(top_individuals) - 1)]
                individual = EvolutionTools.crossover(individual1.mutate(mutation_rate),
                                                      individual2.mutate(mutation_rate))
                top_individual_babies.append(individual)
        # print("Top Babies:")
        # for ind in top_individual_babies:
        #     print(f"Genes: {ind.get_genes()}, Fitness: {ind.get_fitness(Climate.COLD)}")
        return top_individual_babies

    def mate_random_individuals(self, mutation_rate, random_selection_percentage, sorted_individuals):
        new_individuals = []
        num_random_babies = int(random_selection_percentage * 0.01 * len(sorted_individuals) * 0.4)
        for _ in range(num_random_babies):
            random_indices = random.sample(range(len(sorted_individuals)), 2)
            individual1 = sorted_individuals[random_indices[0]]
            individual2 = sorted_individuals[random_indices[1]]
            individual = EvolutionTools.crossover(individual1.mutate(mutation_rate),
                                                  individual2.mutate(mutation_rate))
            new_individuals.append(individual)
        # print("New Individuals from Random Mating:")
        # for ind in new_individuals:
        #     print(ind)
        return new_individuals
    

    def __str__(self):
        return '\n'.join(str(individual) for individual in self.individuals)

    def sorted_individuals_by_fitness(self, climate):
        # sorted_individuals=sorted(self.individuals, key=lambda ind: ind.get_fitness(climate), reverse=True)
        # for ind in sorted_individuals:
        #     print(ind)
        return sorted(self.individuals, key=lambda ind: ind.get_fitness(climate), reverse=True)
    