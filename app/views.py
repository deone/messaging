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

    attachment = os.path.join(settings.MEDIA_ROOT, _file.split('/')[-1])

    response = requests.get(_file)
    with open(attachment, 'w') as f:
        f.write(response.content)

    email = EmailMessage(
        data['subject'][0],
        data['message'][0],
        data['sender'][0],
        data['recipients'],
    )

    email.attach_file(attachment)
    email.send()

    os.remove(attachment)

    return JsonResponse({'status': 'ok'})