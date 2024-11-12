import pandas as pd
import random
import numpy as np
from collections import Counter

course_metadata = pd.read_csv(r"csv_dataframe - Sheet1.csv") 

unique_ids_in_resultschatbot = ['Mr. Sajid Ali', 'Dr Salman Ahmed', 'CS112']

results_chatbot = pd.read_csv('results_chatbot.csv')

# Initialize timetable with 5 days and 10 lecture halls
columns = [f'lh{i}' for i in range(15)]
data = [[None for _ in range(15)] for _ in range(5)]
timetable = pd.DataFrame(data, columns=columns)
temp_lh_list = []
# GA parameters
POPULATION_SIZE = 100
GENES = list(range(len(course_metadata)))  # Courses are represented by indices in course_metadata
MAX_GENERATIONS = 200
ANNEALING_THRESHOLD = 50  # Apply simulated annealing if no improvement in 50 generations
day_ctr = 0
# Individual class
class Individual:
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.calculate_fitness()

    @classmethod
    def create_gnome(cls):
        return [random.choice(GENES) for _ in range(8)]

    @classmethod
    def mutate_gene(cls):
        return random.choice(GENES)

    def mate(self, partner):
        child_chromosome = []
        for gene1, gene2 in zip(self.chromosome, partner.chromosome):
            prob = random.random()
            if prob < 0.45:
                child_chromosome.append(gene1)
            elif prob < 0.90:
                child_chromosome.append(gene2)
            else:
                child_chromosome.append(self.mutate_gene())
        return Individual(child_chromosome)

    def calculate_fitness(self):
        fitness = 0
        counts = Counter(self.chromosome)
        flattened_templh_list = [item for sublist in temp_lh_list if sublist is not None for item in sublist]
        counts_flattened = Counter(flattened_templh_list)
        # Constraints for credit hours
        for i, course_index in enumerate(self.chromosome):
            if course_metadata.iloc[course_index]['Credit Hours'] <= 0:
                fitness += 1
            if counts[course_index] > course_metadata.iloc[course_index]['Credit Hours']:
                fitness += counts[course_index] - course_metadata.iloc[course_index]['Credit Hours']
            # avoiding overlaps
            for lh_slots in temp_lh_list:
                if lh_slots[i] == course_index:
                    fitness+=1
                # avoiding teacher overlaps
                if course_metadata.iloc[lh_slots[i]]["Teacher ID"] == course_metadata.iloc[course_index]["Teacher ID"] :
                    fitness+=1
                # avoiding same section clash
                if course_metadata.iloc[lh_slots[i]]["Semester"] == course_metadata.iloc[course_index]["Semester"] :
                    if course_metadata.iloc[lh_slots[i]]["Section"] == course_metadata.iloc[course_index]["Section"] :
                        fitness+=1
            if counts_flattened[course_index] >= 2:
                fitness += counts_flattened[course_index]
        # Wednesday slot 11 30 to 12 30 should be reserved for seminar
            if day_ctr == 2:
                if 102 in self.chromosome:
                    if i == 4 and course_index == 102:
                        fitness -= 3
                    else:
                        fitness -= 1
                else:
                    fitness += 3
            if day_ctr != 2 and 102 in self.chromosome:
                fitness += 3
            # Solving teacher prefrences problem
            if course_metadata.iloc[course_index]["Course ID"] in unique_ids_in_resultschatbot: 
                row_index = results_chatbot[results_chatbot['unique_id'] == course_metadata.iloc[course_index]["Course ID"]].index[0]
                row_index = int(row_index)
                if chr(i) in results_chatbot.iloc[row_index]['time_slots']:
                    fitness -= 1
                else:
                    fitness += 1
            elif course_metadata.iloc[course_index]["Teacher ID"] in unique_ids_in_resultschatbot:
                row_index = results_chatbot[results_chatbot['unique_id'] == course_metadata.iloc[course_index]["Teacher ID"]].index[0]
                row_index = int(row_index)
                if chr(i) in results_chatbot.iloc[row_index]['time_slots']:
                    fitness -= 1
                else:
                    fitness +=1
                
            
        return fitness

def tournament_selection(population):
    tournament = random.sample(population, k=5)
    return min(tournament, key=lambda ind: ind.fitness)

def reduce_credit_hours(course_list):
    for course in course_list:
        course_metadata.loc[course, 'Credit Hours'] -= 1

def simulated_annealing(individual, temperature=1.0, cooling_rate=0.95):
    current = individual
    best = Individual(current.chromosome.copy())  # Initialize best with a copy of the current individual
    while temperature > 0.01:
        # Generate a slightly mutated individual
        new_individual = Individual(
            [gene if random.random() > 0.2 else random.choice(GENES) for gene in current.chromosome]
        )

        # Update best if we find a better solution
        if new_individual.fitness < best.fitness:
            best = new_individual
            current = new_individual  # Set current to new better solution immediately
        # Otherwise, accept new_individual with some probability to allow exploration
        elif random.random() < np.exp((current.fitness - new_individual.fitness) / temperature):
            current = new_individual

        # Reduce the temperature
        temperature *= cooling_rate

    return best  # Return the best solution found


def initialize_population():
    # Greedy initialization for a better start
    population = []
    for _ in range(POPULATION_SIZE // 2):
        chromosome = [random.choice(GENES) for _ in range(8)]
        population.append(Individual(chromosome))
    # Adding some completely random individuals
    for _ in range(POPULATION_SIZE // 2):
        chromosome = Individual.create_gnome()
        population.append(Individual(chromosome))
    return population

def main():
    ctr = 0
    global timetable
    global temp_lh_list
    global day_ctr
    for day in timetable.index:
        print("Processing day:", day)
        temp_lh_list = []
        for lh in timetable.columns:
            generation = 1
            found = False
            population = initialize_population()
            no_improvement_count = 0
            best_fitness = float('inf')
            
            while not found and generation < MAX_GENERATIONS:
                population.sort(key=lambda x: x.fitness)

                # Check for best individual
                if population[0].fitness <= 0:
                    found = True
                    timetable.loc[day, lh] = population[0].chromosome
                    reduce_credit_hours(population[0].chromosome)
                    temp_lh_list.append(population[0].chromosome)
                    ctr+=1
                    print(day,ctr)
                    break

                # If no improvement in fitness, apply simulated annealing
                if population[0].fitness < best_fitness:
                    best_fitness = population[0].fitness
                    no_improvement_count = 0
                else:
                    no_improvement_count += 1
                    if no_improvement_count >= ANNEALING_THRESHOLD:
                        population[0] = simulated_annealing(population[0])
                        no_improvement_count = 0

                # New generation using elitism and mating
                new_generation = []
                new_generation.extend(population[:int(0.15 * POPULATION_SIZE)])  # Elitism
                for _ in range(int(0.7 * POPULATION_SIZE)):
                    parent1 = tournament_selection(population)
                    parent2 = tournament_selection(population)
                    child = parent1.mate(parent2)
                    new_generation.append(child)
                for _ in range(int(0.15 * POPULATION_SIZE)):
                    new_generation.append(Individual(Individual.create_gnome()))  # Random mutation
                
                population = new_generation
                print(day,lh, generation)
                generation += 1
        print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj",day)
        day_ctr += 1

if __name__ == "__main__":
    main()
    print(timetable)
    timetable.to_csv("timetable.csv")