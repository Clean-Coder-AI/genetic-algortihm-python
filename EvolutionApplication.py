import random
import csv
from Individual import Climate
from Population import Population
import matplotlib.pyplot as plt

class EvolutionApplication:

    def main(args):
        print("STARTING THE APPLICATION")
        EvolutionApplication.run()

    def run():
        print("EXECUTING:")
        population = Population(30, 20)
        hot = Climate.HOT
        cold = Climate.COLD

        random_percentage = float(input("Enter the random selection percentage (0-100): "))
        random_percentages = [random_percentage]

        average_fitness_hot = {percentage: [] for percentage in random_percentages}
        average_fitness_cold = {percentage: [] for percentage in random_percentages}

        with open('evolution.csv', mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([f"Random Selection Percentage: {random_percentage:.2f}%"])
            writer.writerow(["Climate: Hot"])
            writer.writerow(["Generation", "Average Hot Fitness", "Average Cold Fitness", "Fittest Hot", "Fittest Cold"])

            for i in range(30):
                # Replace this part with your existing genetic algorithm simulation
                # This is where you would update the population and calculate average fitness
                # and fittest_hot and fittest_cold

                # Sample data (replace this with your own data)
                average_fitness_hot[random_percentage].append(random.uniform(0, 10))
                average_fitness_cold[random_percentage].append(random.uniform(0, 10))
                fittest_hot = random.uniform(0, 10)  # Replace with your logic
                fittest_cold = random.uniform(0, 10)  # Replace with your logic

                writer.writerow([i, f"{average_fitness_hot[random_percentage][i]:.2f}", f"{average_fitness_cold[random_percentage][i]:.2f}", fittest_hot, fittest_cold])

        plt.figure(figsize=(10, 6))

        plt.title('Average Fitness Evolution')
        plt.xlabel('Generation')
        plt.ylabel('Average Fitness')

        plt.plot(average_fitness_hot[random_percentage], label=f'{random_percentage}% Random Selection (Hot)')
        plt.plot(average_fitness_cold[random_percentage], label=f'{random_percentage}% Random Selection (Cold)')

        plt.legend()
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    EvolutionApplication.main([])
