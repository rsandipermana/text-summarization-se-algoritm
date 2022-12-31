import nltk
import datetime
import re
from collections import defaultdict

class SearchEconomicUseCase:
    
    def execute(self, request):
        
        # Extract the 'article' and 'top_n' values from the request
        article = request['article']
        top_n = int(request['top_n'])
        
        # Code for retrieving users goes here
        result = self.summarize(article, N=top_n)
        return {'result': result}
    
    def summarize(self, text, N=3):
        
        # cleaning data
        article = self.cleaning(text)
        
        # Split the article into sentences
        sentences = re.split(r'[.?!]', article)
        sentences = self.cleaning_whitespace(sentences)
        
        # Tokenize the sentences
        tokens = [sentence.split() for sentence in sentences]
        self.write_summary('tokens', tokens)
        
        # Calculate the frequency of each word in the article
        frequencies = defaultdict(int)
        for token in tokens:
            for word in token:
                frequencies[word] += 1
        
        # Calculate the economic value of each sentence
        values = []
        for token in tokens:
            value = 0
            for word in token:
                value += frequencies[word]
            values.append(value)
        
        # Sort the sentences by economic value
        sorted_sentences = [sentence for _, sentence in sorted(zip(values, sentences), reverse=True)]
        
        # Return the top N sentences
        return sorted_sentences[:N]
    
    def cleaning(self, text):
        
        # Split the text into sentences
        sentences = text.split('.')
        
        # Remove the leading and multiple whitespace from each sentence
        sentences = self.cleaning_whitespace(sentences)

        # Join the sentences back into a single text
        text = '. '.join(sentences)
        
        # Return text
        return text
    
    def write_summary(self, filename: str = 'test', text: any = 'test'):
        
        # write text into file
        text = str(text)
        with open(f"./logs/{filename}.json", 'w') as f:
            f.write(text)
            
    def cleaning_whitespace(self, sentences):
        
        # Remove the leading whitespace
        sentences = [sentence.lstrip() for sentence in sentences]
        
        # Remove the multiple whitespace
        sentences = [re.sub(r'\s+', ' ', sentence) for sentence in sentences]
        
        return sentences