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
    file = data['file'][0]
    file_name = file.split('/')[-1]

    response = requests.get(file)
    with open(file_name, 'a') as f:
        f.write(response.content)

    email = EmailMessage(
        data['subject'][0],
        data['message'][0],
        data['sender'][0],
        data['recipients'],
    )
    file = os.path.join(settings.BASE_DIR, file_name)
    email.attach_file(file)
    email.send()

    os.remove(file)

    return JsonResponse({'status': 'ok'})