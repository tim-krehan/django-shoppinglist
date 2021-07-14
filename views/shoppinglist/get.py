import sys
from django.core import serializers
from ...models import ShoppingList
from django.http.response import HttpResponse

def req(request, pk):
    shoppinglist = ShoppingList.objects.get(pk=pk)
    json = serializers.serialize("json", [shoppinglist])
    return HttpResponse(json, content_type="application/json")