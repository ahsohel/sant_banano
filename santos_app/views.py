from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, HttpResponse

from django.http import JsonResponse
from django.core import serializers

from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.views.decorators.csrf import csrf_exempt


# Create your views here.


# def index(request):
#     return render(request, 'index.html')


def index(request):
    get_click_or_not = request.session.get('click_or_not')
    clic = ''
    if get_click_or_not:
        clic = 'clicked'
    else:
        pass
    contex = {'clic': clic}

    return render(request, 'index.html', contex)


def do_or_do_not(request):
    return render(request, 'do_or_do_not.html')


@csrf_exempt
def going_for_email(request):
    Title = request.POST.get('title')
    First_Name = request.POST.get('fname')
    Last_Name = request.POST.get('lname')
    Mobile_Number = request.POST.get('phone')
    eMail = request.POST.get('email')
    n_Message_field = request.POST.get('Message_field')

    print(Title)
    print(First_Name)
    print(Last_Name)
    print(Mobile_Number)
    print(eMail)
    print('n_Message_field')
    print(n_Message_field)
    # emal_add = 'abdussobahanchowdhury@gmail.com'
    emal_add = 'Info@santoshealingvibes.com'
    # emal_add = 'mdabuhassan279@gmail.com'
    # emal_add = 'md0099ahsohel@gmail.com'

    email_for_buy = render_to_string(
        'santos_email.html',
        {
            'Title': Title,
            'First_Name_1': First_Name,
            'Last_Name_1': Last_Name,
            'Mobile_Number_1': Mobile_Number,
            'eMail': eMail,
            'n_Message_field': n_Message_field,
        }
    )

    send_mail(
        'Contact Information - Thank You',  # subject
        email_for_buy,  # massage
        '',  # from email
        [emal_add],  # to email
        fail_silently=True,
    )

    print('done')

    # return redirect('do_or_do_not')
    return JsonResponse("Your email  has been sent successfully", safe=False)


@csrf_exempt
def set_cookie(request):
    request.session['click_or_not'] = 'ok'
    print('name')

    return HttpResponse('name2')


@csrf_exempt
def connect_massage_send(request):
    email_get = request.POST.get('email_get')
    massage_get = request.POST.get('massage_get')
    print(email_get)
    print(massage_get)

    if email_get and massage_get:
        if '@' in email_get:

            emal_add = 'Info@santoshealingvibes.com'
            # emal_add = 'md0099ahsohel@gmail.com'

            email_for_connect = render_to_string(
                'connect_email.html',
                {
                    'Connect_email': email_get,
                    'Massage_get': massage_get,
                }
            )

            send_mail(
                'Custom Project - Thank You For Sending Us',  # subject
                email_for_connect,  # massage
                '',  # from email
                [emal_add],  # to email
                fail_silently=True,
            )

            return HttpResponse('email is send')
        else:
            return HttpResponse('email not correct')

    return HttpResponse('email_get')


