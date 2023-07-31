import random


class Individual:
    def __init__(self, target_solution):
        self.solution = target_solution
        self.genes = [random.randint(0, 1) for _ in range(len(self.solution))]
        self.fitness = 0

    def get_single_gene(self, index):
        return self.genes[index]

    def set_single_gene(self, index, value):
        self.genes[index] = value
        self.fitness = 0

    def default_gene_length(self):
        return len(self.genes)

    def get_fitness(self):
        if self.fitness == 0:
            self.fitness = sum(
                1
                for i in range(len(self.genes))
                if self.genes[i] == int((self.solution[i]))
            )

        return self.fitness

    def __str__(self):
        return "".join(str(gene) for gene in self.genes)

    def clone(self):
        clone = Individual(self.solution)
        clone.genes = list(self.genes)
        clone.fitness = self.fitness
        return clone
