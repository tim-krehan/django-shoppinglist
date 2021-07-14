from django.http.response import HttpResponse
from ...models import ListEntry

def delete(request, pk):
    listentry = ListEntry.objects.get(pk=pk)
    listentry.delete()
    return HttpResponse('{"success": true}', content_type="application/json")
