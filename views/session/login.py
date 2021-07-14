import json
from os import error

from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.db import models


def req(request):
    res = {
        'success': False,
        'error': ''
    }
    body = request.body
    jsonBody = json.loads(body)

    if 'username' in jsonBody:
        user = jsonBody["username"]
    else:
        user = jsonBody["email"]

    password = jsonBody["password"]

    user = User.objects.filter(models.Q(username=user) | models.Q(email=user))
    if not user.count() == 1:
        res["error"] = 'not unique user!'
    else:
        if not user[0].check_password(raw_password=password):
            res["error"] = 'wrong pass or user!'
        else:
            res["success"] = True

    jsonRes = json.dumps(res)
    return HttpResponse(jsonRes, content_type="application_json")
