import random
from collections import defaultdict
import string

class GeneticAlgorithmUseCase:
    def execute(self, request):
        # Extract the 'article' and 'top_n' values from the request
        article = request['article']
        top_n = int(request['top_n'])
        
        # Code for retrieving users goes here
        result = self.summarize(article, N=top_n)
        return {'result': result}
        
    def summarize(self, article, N):
        # Split the article into sentences
        sentences = article.split('. ')
        
        # Initialize the population of summary sentences
        population = [''.join(random.sample(sentences, N)) for _ in range(100)]
        
        # Define the fitness function
        def fitness(summary):
            # Calculate the number of common words between the summary and the original article
            common_words = len(set(summary.split()) & set(article.split()))
            # Return the fitness score as the inverse of the number of common words
            return 1 / common_words
        
        # Run the genetic algorithm
        for _ in range(100):
            # Select the fittest individuals
            fittest = sorted(population, key=fitness, reverse=True)[:50]
            # Perform crossover and mutation on the fittest individuals
            population = [self.crossover(fittest) for _ in range(50)] + [self.mutate(fittest) for _ in range(50)]
        
        # Return the fittest individual as the summary
        # In this case, the summary is a list of sentences, so we need to convert it to a string
        summary_str = '. '.join(fittest[0])
        return summary_str
    
    def crossover(self, individuals):
        # Choose two random individuals for crossover
        individual1, individual2 = random.sample(individuals, 2)
        # Split the individuals at a random point
        point = random.randint(0, len(individual1))
        # Create a new individual by combining the two individuals at the crossover point
        individual = individual1[:point] + individual2[point:]
        return individual
    
    def mutate(self, individual):
        # Choose a random point in the individual
        point = random.randint(0, len(individual))
        # Replace the character at the chosen point with a random character
        individual[point] = random.choice(string.ascii_letters)
        return individual