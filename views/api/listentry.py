from django.http.response import HttpResponse

def listentry(request):
    responseText = '{"welcome": "welcome to the listentry API!"}'
    return HttpResponse(responseText, content_type="application/json")