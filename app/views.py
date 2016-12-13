from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def index(request):
    data = dict(request.GET)
    send_mail(
        data['subject'][0],
        data['message'][0],
        data['sender'][0],
        data['recipients'],
        fail_silently=False,
    )
    return JsonResponse({'status': 'ok'})