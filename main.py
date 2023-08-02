from HotColdAlgorithm import HotColdAlgorithm

if __name__ == "__main__":
    target_solution_length = 64
    population_size = 50

    genetic_algorithm = HotColdAlgorithm(target_solution_length, population_size)
    genetic_algorithm.run_algorithm()
