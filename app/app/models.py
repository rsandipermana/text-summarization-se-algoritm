from django.db import models


class Article(models.Model):
    # Column to store the article title
    title = models.CharField(max_length=255, default="-")
    # Column to store the article link
    link = models.URLField(default="-")
    # Column to store the article text
    text = models.TextField()
    
    def __str__(self):
        return self.text
    
class Summary(models.Model):
    # Column to store the summary text
    text = models.TextField()
    # Column to store the algorithm used to generate the summary
    algorithm = models.CharField(max_length=50, choices=[
        ('SumBasic', 'SumBasic'),
        ('LexRank', 'LexRank'),
        ('LSA', 'LSA'),
        ('TextRank', 'TextRank'),
        ('KLSum', 'KLSum'),
        ('GA', 'Genetic Algorithm'),
        ('SE', 'Search Economics'),
    ])
    # Column to store the compression rate of the summary
    compression_rate = models.FloatField()
    # Foreign key to the Article model
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text
    
class Evaluation(models.Model):
    # Foreign key to the Summary model
    summary = models.ForeignKey(Summary, on_delete=models.CASCADE)
    # Column to store the score for the evaluation
    score = models.FloatField()
    # Column to store the method used to evaluate the summary
    index = models.CharField(max_length=50, choices=[
        ('ROUGE', 'ROUGE'),
        ('Cosine Similarity', 'Cosine Similarity'),
        ('F-measure', 'F-measure'),
        ('Bleu', 'Bleu'),
    ])
    
    def __str__(self):
        return self.text

