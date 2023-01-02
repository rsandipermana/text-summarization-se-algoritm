from django.http import JsonResponse
from app.pages.articles.usecase import GetArticlesUseCase

def fetch_kompas(request):
    # Code for summarizing the data goes here
    result = GetArticlesUseCase().execute(request)
    return JsonResponse(result)