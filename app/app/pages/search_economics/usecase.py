import math
from collections import defaultdict
from app.models import Article, Summary
from app.utils import CleanSentence, CleanSentences, Article2Sentences, CR2N, Logs

class SearchEconomicUseCase:
    
    def execute(self, request):
        
        # Extract the 'article' and 'top_n' values from the request
        cr = float(request['cr'])
        article_url = request['article_url']
        article = Article.objects.get(link=article_url)
        
        # Code for retrieving users goes here
        summary = self.summarize(article, cr)
        
        return {
            'reference': article.text,
            'summary': summary
        }
    
    def summarize(self, article_instance, CR=0.1):
        
        # cleaning data
        article = CleanSentence(article_instance.text)
        
        # Split the article into sentences
        sentences = Article2Sentences(article)
        
        # Tokenize the sentences
        tokens = [sentence.split() for sentence in sentences]
        
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
        N = CR2N(len(sentences), CR)
        
        top_sentences = sorted_sentences[:N]
        clean_sentences = CleanSentences(top_sentences)
        
        summary = "".join(clean_sentences)
        
        self.store(summary, article_instance, CR)
        # Return the top sentences clean
        return summary
    
    def store(self, summary, article, cr):
        # Check summary if the article with algorithm already exists in the database
        algorithm = 'SE'
        existing_summary = Summary.objects.filter(
            article=article, 
            algorithm=algorithm, 
            compression_rate=cr
        ).first()
        if not existing_summary:
            Summary.objects.create(
                text="".join(summary), 
                algorithm=algorithm, 
                compression_rate=cr,
                article=article
            )