from django.http.response import HttpResponse

def req(request):
    return HttpResponse('{"kek":true}', content_type="application_json")