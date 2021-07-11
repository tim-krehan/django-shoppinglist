from django.http.response import HttpResponse

def set(request):
    responseText = '{"welcome": "to the shoppinglist/set API!"}'
    return HttpResponse(responseText, content_type="application/json")