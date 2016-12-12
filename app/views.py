from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def index(request):
    send_mail(
        'Subject here',
        'Here is the message.',
        'incisiaappmailer@gmail.com',
        ['alwaysdeone@gmail.com'],
        fail_silently=False,
    )
    return JsonResponse({'status': 'ok'})