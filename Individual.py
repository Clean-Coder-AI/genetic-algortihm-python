import random

class Individual:
    def __init__(self, numberOfGenes):
        self.genes = self.generate_random_gene(numberOfGenes)

    def generate_random_gene(self, numberOfGenes):
        # genes = [random.randint(0, 1) for _ in range(numberOfGenes)]
        # return genes
        numberOfOnes = int(random.random() * numberOfGenes)
        indices = self.generate_random_indices(numberOfGenes, numberOfOnes)
        genes = [0] * numberOfGenes
        for i in indices:
            genes[i] = 1
        return genes

    def generate_random_indices(self, numberOfGenes, numberOfOnes):
        indices = list(range(numberOfGenes))
        for _ in range(numberOfGenes - numberOfOnes):
            random_index = random.randint(0, len(indices) - 1)
            indices.pop(random_index)
        return indices

    def get_genes(self):
        return self.genes

    def get_fitness(self, climate):
        if climate == Climate.HOT:
            return sum(self.genes)
        else:
            return len(self.genes) - sum(self.genes)

    def clone_individual(self):
        clone = Individual(len(self.genes))
        clone.genes = list(self.genes)
        return clone       

    def mutate(self, mutation_rate):
        individual = self.clone_individual()
        for i in range(len(individual.genes)):
            if random.random() < mutation_rate:
                individual.genes[i] = 1 - individual.genes[i]  #flip the bit
        return individual

    def __str__(self):
        return ''.join(map(str, self.genes))

class Climate:
    HOT = 'HOT'
    COLD = 'COLD'
