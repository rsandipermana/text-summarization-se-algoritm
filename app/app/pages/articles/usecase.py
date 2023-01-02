import requests
from bs4 import BeautifulSoup
import datetime
from collections import defaultdict
from app.models import Article
from app.utils import CleanSentence

class GetArticlesUseCase:
    
    def execute(self, request):
        # Extract the 'article' and 'top_n' values from the request
        domain = request['domain']
        top_n = int(request['top_n'])
        
        # Code for retrieving articles goes here
        result = self.get_articles(domain, n=top_n)
        return {'result': result}

    def get_articles(self, domain, n=10):
        # retrieve HTML from a news site (national, sports, or other subdomain)
        html = requests.get(domain).text

        # use Beautiful Soup to extract information
        soup = BeautifulSoup(html, "html.parser")
        articles = []

        # find elements <h3> that contain article titles
        h3_elements = soup.find_all("h3")

        # get the title and link from each <h3> element
        for h3 in h3_elements[:n]:
            title = h3.text
            link = h3.find("a")["href"]
            articles.append({"title": title, "link": link})
        
        # save article details
        article_details = []
        for i, article in enumerate(articles):
            article_details.append(self.detail_article(article['link']))
        
        # Store bulk articles
        self.store_articles(article_details)
        
        # retrieve article link and title
        return article_details

    def detail_article(self, link):
        
        # link detail
        link = f"{link}?page=all"
        
        # get the web page
        response = requests.get(link)

        # parse HTML using Beautiful Soup
        content = BeautifulSoup(response.text, "html.parser")
        
        # get all <p> elements within <div class="read__content">
        paragraphs = content.find_all("p")
        
        text_paragraphs = []
        # loop through each <p> element
        for p in paragraphs:
            # print the text within the <p> element
            sentence = CleanSentence(p.text)
            text_paragraphs.append(sentence)

        # using list comprehension to remove elements containing the text "Baca juga:"
        array = [item for item in text_paragraphs if "Baca juga:" not in item and item != ""]
        
        # find the index of the element containing the text "#JernihBerkomentar"
        start_index = -1
        for i, elemen in enumerate(array):
            if "#JernihBerkomentar" in elemen:
                start_index = i
                break

        # remove the element and all the elements after it in the array list
        if start_index != -1:  # if the element is found
            for i in range(start_index, len(array)):
                del array[start_index]
        
        # get the article details
        article = {
            "title": content.find("h1").text,
            "link": link,
            "text": "".join(array)
        }

        # get the text of the article
        return article
    
    def store_articles(self, array):
        
        articles = []
        for item in array:
            # Check if the link already exists in the database
            existing_article = Article.objects.filter(link=item['link']).first()
            if not existing_article:  # If the link doesn't exist, create a new article
                articles.append(Article(title=item['title'], link=item['link'], text=item['text']))

        # Use bulk_create to insert multiple articles in a single query
        Article.objects.bulk_create(articles)