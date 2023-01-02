from django.http import JsonResponse
from app.pages.articles.usecase import GetArticlesUseCase

def fetch_kompas(request):
    # Code for summarizing the data goes here
    _request = request.GET.dict()
    result = GetArticlesUseCase().execute(_request)
    return JsonResponse(result)