from django.http.response import HttpResponse

def shoppinglist(request):
    return HttpResponse("{'message':'welcome to the shoppinglist!'}")