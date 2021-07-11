import sys
from django.core import serializers
from ...models import ShoppingList
from django.http.response import HttpResponse

def get(request, pk):
    sl = ShoppingList.objects.filter(pk=pk)
    json = serializers.serialize("json", sl)
    return HttpResponse(json, content_type="application/json")