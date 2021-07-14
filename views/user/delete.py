from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.core import serializers
import json

# DELETE
def delete(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return HttpResponse('{"success": true}', content_type="application/json")