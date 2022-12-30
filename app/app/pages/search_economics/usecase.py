class SearchEconomicUseCase:
    def execute(self, request):
        # Code for retrieving users goes here
        print(request)
        return {'data': request}