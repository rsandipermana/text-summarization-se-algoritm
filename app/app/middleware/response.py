from django.http import JsonResponse
# import logging

class ResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # self.logger = logging.getLogger(__name__)

    def __call__(self, request):
        response = self.get_response(request)
        # self.logger.debug(response)
        if isinstance(response, JsonResponse):
            # response.data = {'data': response.data}
            response['Content-Type'] = 'application/json'
        return response