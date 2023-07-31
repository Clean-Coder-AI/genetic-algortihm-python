from GeneticAlgorithm.GeneticAlgorithm import SimpleGeneticAlgorithm

if __name__ == "__main__":
    population_size = 50
    solution = "1110101010101111100000001110100101101010001110101010001101010101"
    ga = SimpleGeneticAlgorithm(solution, population_size)
    ga.run_algorithm()
