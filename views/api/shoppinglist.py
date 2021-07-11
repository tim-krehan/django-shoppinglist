from django.http.response import HttpResponse

def shoppinglist(request):
    responseText = '{"welcome": "welcome to the shoppinglist API!"}'
    return HttpResponse(responseText, content_type="application/json")