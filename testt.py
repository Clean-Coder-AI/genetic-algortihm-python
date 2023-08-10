from Individual import Climate
import random

climate = random.choice([Climate.HOT, Climate.COLD])
genes = [1, 0, 0, 1, 1]

class Test:
    # get_fitness function
    def haha(self, climate, genes):
        if climate == Climate.HOT:
            f = sum(genes)
        else:
            f = len(genes) - sum(genes)
        return f

l = [[1, 1, 0], [0, 0, 0], [1, 1, 1]]
fittest = l[0]
best_fitness = 0


for sublist in l:
    instance = Test()  # Create an instance of the Test class
    sublist_fitness = instance.haha(climate, sublist)
    if sublist_fitness > best_fitness:
        best_fitness = sublist_fitness
        fittest = sublist

print(f"Fittest sublist: {fittest}, CLimate: {climate}")
