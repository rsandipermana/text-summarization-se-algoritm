from django.http import JsonResponse
from app.pages.search_economics.usecase import SearchEconomicUseCase

def summarize(request):
    # Code for summarizing the data goes here
    _request = request.GET.dict()
    result = SearchEconomicUseCase().execute(_request)
    return JsonResponse(result)
    
def detail(request, pk):
    # Code for getting the detail of the data goes here
    return JsonResponse({'detail': 'Detail of data with PK %d' % pk})
