import random
import matplotlib.pyplot as plt

from HotColdAlgorithm import HotColdAlgorithm

if __name__ == "__main__":
    target_solution_length = 50
    population_size = 100
    num_generations = 100
    
    # Initialize the algorithm
    algorithm = HotColdAlgorithm(target_solution_length, population_size)
    algorithm.run_algorithm(num_generations, print_stats=True)
    
    # Lists to store average fitness values for each scenario over generations
    average_fitness_hot = []
    average_fitness_cold = []

    # Lists to store tournament selection fitness values
    tournament_fitness_values = []

    # Run the algorithm and collect average fitness data
    for _ in range(num_generations):
        algorithm.run_algorithm(1)  # Run the algorithm for 1 generation
        
        # Calculate average fitness for hot and cold scenarios
        total_fitness_hot = sum(ind.get_fitness(0) for ind in algorithm.my_pop.individuals)
        total_fitness_cold = sum(ind.get_fitness(1) for ind in algorithm.my_pop.individuals)
        avg_fitness_hot = total_fitness_hot / population_size
        avg_fitness_cold = total_fitness_cold / population_size
        
        average_fitness_hot.append(avg_fitness_hot)
        average_fitness_cold.append(avg_fitness_cold)

        # Collect fitness values of selected individuals during tournament selection
        selected_individuals = [algorithm.tournament_selection() for _ in range(algorithm.tournament_size)]
        tournament_fitness_values.append([ind.get_fitness(0) for ind in selected_individuals])

        algorithm.generation_count += 1
        algorithm.switch_environment()

    # Plot average fitness values for hot scenario
    plt.figure(figsize=(10, 6))
    plt.plot(range(num_generations), average_fitness_hot, label='Hot Scenario', color='red')
    plt.xlabel('Generation')
    plt.ylabel('Average Fitness')
    plt.title('Average Fitness in Hot Scenario')
    plt.legend()
    plt.show()

    # Plot average fitness values for cold scenario
    plt.figure(figsize=(10, 6))
    plt.plot(range(num_generations), average_fitness_cold, label='Cold Scenario', color='blue')
    plt.xlabel('Generation')
    plt.ylabel('Average Fitness')
    plt.title('Average Fitness in Cold Scenario')
    plt.legend()
    plt.show()

    # Plot tournament selection fitness values
    plt.figure(figsize=(10, 6))
    for i in range(algorithm.tournament_size):
        plt.plot(range(num_generations), [fitness_values[i] for fitness_values in tournament_fitness_values], label=f'Individual {i+1}')
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.title('Tournament Selection Fitness Values')
    plt.legend()
    plt.show()