from django.http.response import HttpResponse
from django.utils import timezone
from ...models import ListEntry

def req(request, pk):
    listentry = ListEntry.objects.get(pk=pk)
    listentry.delete()
    listentry.shoppinglist.last_change = timezone.now()
    listentry.shoppinglist.save()
    return HttpResponse('{"success": true}', content_type="application/json")
