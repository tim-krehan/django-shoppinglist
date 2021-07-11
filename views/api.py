from django.http.response import HttpResponse

def api(request, version):
    responseText = '{"welcome": "welcome to the API V%s!"}' % version
    return HttpResponse(responseText, content_type="application/json")