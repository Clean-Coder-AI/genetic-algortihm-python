from genetic_algorithm import SimpleGeneticAlgorithm

if __name__ == "__main__":
    population_size = 50
    solution = "1011000100000100010000100000100111001000000100000100000000001111"
    ga = SimpleGeneticAlgorithm(solution, population_size)
    ga.run_algorithm()

    