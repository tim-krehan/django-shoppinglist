from django.http.response import HttpResponse

def listentry(request):
    return HttpResponse("{'message':'welcome to the listentry!'}")