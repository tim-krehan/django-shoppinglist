from django.http.response import HttpResponse
from django.utils import timezone
from ...models import ListEntry, ShoppingList

def req(request, pk):
    listenties = ListEntry.objects.filter(shoppinglist=pk)
    listenties.delete()
    shoppinglist = ShoppingList.objects.get(pk=pk)
    shoppinglist.delete()
    
    return HttpResponse('{"success": true}', content_type="application/json")
