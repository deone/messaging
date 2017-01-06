from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.views.decorators.csrf import ensure_csrf_cookie

import requests
import os

@ensure_csrf_cookie
def index(request):
    data = dict(request.GET)
    _file = data['file'][0]
    file_name = _file.split('/')[-1]

    response = requests.get(_file)
    with open(file_name, 'w') as f:
        f.write(response.content)

    email = EmailMessage(
        data['subject'][0],
        data['message'][0],
        data['sender'][0],
        data['recipients'],
    )

    _file = os.path.join(settings.BASE_DIR, file_name)
    email.attach_file(_file)
    email.send()

    os.remove(_file)

    return JsonResponse({'status': 'ok'})