import random
import csv
from Individual import Climate
from Population import Population

class EvolutionApplication:


    def main(args):
        print("STARTING THE APPLICATION")
        EvolutionApplication.run()


    # def run():
    #     print("EXECUTING:")
    #     population = Population(30, 20)
    #     # Randomly select the initial climate
    #     climate = random.choice([Climate.HOT, Climate.COLD])
    #     print()
    #     print("----------------------------------------")
    #     print(f"Initial climate: {climate}")
    #     print(f"Initial average fitness: {population.get_average_fitness(climate):.2f}")
    #     print("----------------------------------------")
        
    #     random_selection_percentage = float(input("Enter the random selection percentage (0-100): "))
        
    #     for i in range(10):
    #         climate=Climate.COLD

    #         # # Randomly switch climate with 50% probability
    #         # if random.random() < 0.5:
    #         #     climate = Climate.HOT if climate == Climate.COLD else Climate.COLD
                
    #         print(f"------------Population Evolution for {random_selection_percentage}% Randomness----------------------------")
    #         print(f"Generation: {i+1}")
    #         print(f"Climate: {climate}")
    #         print(f"Average fitness: {population.get_average_fitness(climate):.2f}")
    #         print(f"Fittest individual: {population.get_fittest(climate)}")
    #         print("----------------------------------------")
            
    #         population = population.evolve_v2(climate, 0.03, random_selection_percentage)

    def run():
        print("EXECUTING:")
        population = Population(30, 20)
        hot = Climate.HOT
        cold = Climate.COLD

        random_percentage = float(input("Enter the random selection percentage (0-100): "))
        
        average_fitness_hot = []
        average_fitness_cold = []
        fittest_hot = []
        fittest_cold = []

        with open('evolution.csv', mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([f"Random Selection Percentage: {random_percentage:.2f}%"])  # Row for random selection percentage
            writer.writerow(["Climate: Cold" ])  
            writer.writerow([f"Generation", "Average Hot Fitness", "Average Cold Fitness", "Fittest Hot", "Fittest Cold"])

            for i in range(30):
                # population = population.evolve_v2(cold, 0.03, random_percentage)
                average_fitness_hot.append(population.get_average_fitness(hot))
                average_fitness_cold.append(population.get_average_fitness(cold))
                fittest_hot.append(population.get_fittest(hot).get_fitness(hot))
                fittest_cold.append(population.get_fittest(cold).get_fitness(cold))
                population = population.evolve_v2(cold, 0.03, random_percentage)

                writer.writerow([i, f"{average_fitness_hot[i]:.2f}", f"{average_fitness_cold[i]:.2f}", fittest_hot[i], fittest_cold[i]])
                # # ONLY FOR TESTING: Print the individuals in the population for the first two generations
                # if i < 2:
                #     print(f"Generation: {i+1}")
                #     for individual in population.get_individuals():
                #         print(individual)
                #     print("-----------------------------")
        print("done!")

if __name__ == "__main__":
    EvolutionApplication.main([])