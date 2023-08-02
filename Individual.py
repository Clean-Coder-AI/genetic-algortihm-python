import random

class Individual:
    def __init__(self, target_solution_length):
        self.genes = [random.randint(0, 1) for _ in range(target_solution_length)]
        self.fitness_hot = 0
        self.fitness_cold = 0

    def get_single_gene(self, index):
        return self.genes[index]

    def set_single_gene(self, index, value):
        self.genes[index] = value
        self.fitness_hot = 0
        self.fitness_cold = 0

    def default_gene_length(self):
        return len(self.genes)

    def get_fitness(self, current_environment):
        if current_environment == 0:  # Hot environment (most 1's are fittest)
            if self.fitness_hot == 0:
                self.fitness_hot = sum(1 for i in range(len(self.genes)) if self.genes[i] == 1)
            return self.fitness_hot
        else:  # Cold environment (most 0's are fittest)
            if self.fitness_cold == 0:
                self.fitness_cold = sum(1 for i in range(len(self.genes)) if self.genes[i] == 0)
            return self.fitness_cold
        
    def __str__(self):
        return "".join(str(gene) for gene in self.genes)

    def clone(self):
        clone = Individual(len(self.genes))
        clone.genes = list(self.genes)
        clone.fitness_hot = self.fitness_hot
        clone.fitness_cold = self.fitness_cold
        return clone
