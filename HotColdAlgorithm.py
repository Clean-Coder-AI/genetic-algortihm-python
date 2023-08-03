import random

from Individual import Individual
from Population import Population


class HotColdAlgorithm:
    generation_count = 0
    tournament_size = 5
    uniform_rate = 0.5
    mutation_rate = 0.015
    elitism = True
    elitism_offset = 0

    def __init__(self, target_solution_length, population_size):
        self.solution_length = target_solution_length
        self.population_size = population_size
        self.current_environment = random.randint(0, 1)  # Initialize the environment randomly as hot (0) or cold (1)

    def switch_environment(self):
        generated_number = random.randint(0, 1)
        if generated_number == 1:
            self.current_environment = 1 - self.current_environment #Switch between hot(0) or cold(1)

    def run_algorithm(self, num_generations=100):
        self.my_pop = self.initialize_population()

        for _ in range(num_generations):
            print(f"Generation: {self.generation_count} "
                  f"Fitness: {self.my_pop.get_fittest(self.current_environment).get_fitness(self.current_environment)}/{self.solution_length} "
                  f"Environment: {' Hot' if self.current_environment == 0 else 'Cold'} "
                  f"Genes: {self.my_pop.get_fittest(self.current_environment)}")

            self.evolve_population()
            self.generation_count += 1
            self.switch_environment()  # Randomly switch environment after each generation

        print("-----------------------------------------------------------------------------")
        print(f"Best Genes: {self.my_pop.get_fittest(self.current_environment)}")
        print(f"Environment: {'Hot' if self.current_environment == 0 else 'Cold'}")
        print(f"Fitness: {self.my_pop.get_fittest(self.current_environment).get_fitness(self.current_environment)}/{self.solution_length}")


    def initialize_population(self):
        return Population(self.population_size, self.solution_length, initialize=True)

    def evolve_population(self):
        new_population = Population(self.my_pop.size(), self.solution_length, initialize=False)

        self.elitism_offset = 1 if self.elitism else 0

        if self.elitism:
            new_population.individuals.append(self.my_pop.get_fittest(self.current_environment).clone())

        for _ in range(self.elitism_offset, self.my_pop.size()):
            indiv1 = self.tournament_selection()
            indiv2 = self.tournament_selection()
            new_indiv = self.crossover(indiv1, indiv2)
            new_population.individuals.append(new_indiv)

        for i in range(self.elitism_offset, len(new_population.individuals)):
            self.mutate(new_population.individuals[i])

        self.my_pop = new_population

    def tournament_selection(self):
        tournament = Population(self.tournament_size, self.solution_length, initialize=False)
        random_gen = random.Random()

        for _ in range(self.tournament_size):
            random_id = random_gen.randint(0, self.my_pop.size()-1)
            tournament.individuals.append(self.my_pop.get_individual(random_id))

        return tournament.get_fittest(self.current_environment)

    def crossover(self, indiv1, indiv2):
        new_sol = Individual(self.solution_length)
        random_gen = random.Random()

        for i in range(new_sol.default_gene_length()):
            if random_gen.random() < self.uniform_rate:
                new_sol.set_single_gene(i, indiv1.get_single_gene(i))
            else:
                new_sol.set_single_gene(i, indiv2.get_single_gene(i))

        return new_sol

    def mutate(self, indiv):
        random_gen = random.Random()

        for i in range(indiv.default_gene_length()):
            if random_gen.random() <= self.mutation_rate:
                gene = 1 - indiv.get_single_gene(i)  # flip the bit
                indiv.set_single_gene(i, gene)