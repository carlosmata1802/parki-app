from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth import authenticate
from users.forms import RegisterForm

from django.conf import settings
# Mail includes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from smtplib import SMTPRecipientsRefused
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

def login(request):
    if request.user.is_authenticated():
        return redirect('park:park')

    mensaje = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login_django(request, user)
            return redirect('park:park')
        else:
            mensaje = 'Revisa tus credenciales'

    template = 'login.html'
    context = {
        'messange': mensaje,
    }
    return render(request, template, context)

def type_inicio(request):
    template='login.html'
    context = {}
    return render(request, template, context)

@login_required()
def logout(request):
    logout_django(request)
    return redirect('users:login')

def register(request):
    template = "user_register.html"
    f = RegisterForm()
    messages = None
    context = {
        'title': 'Registro de usuarios',
        'form': f,
        'message': messages
    }
    if request.method == 'POST':
        f = RegisterForm(request.POST, request.FILES)
        if f.is_valid():
            print("Es valido")

            name = request.POST['username']
            email = request.POST['email']
            photo = request.POST["avatar"]

            """new_context = {
                'name': name,
                'email': email,
                'photo': photo
            }

            sendmail(request, email, new_context)"""
            f.save()

        else:
            print("no se guardó")
        messages = 'Usuario creado correctamente'
    return render(request, template, context)


def sendmail(request, email_user, new_context):
    fromaddr = "charlixd.cm@gmail.com"
    toaddr = email_user
    template = get_template('mail.html')
    html_content = template.render(new_context)
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Registro exitoso"
    body = html_content
    msg.attach(MIMEText(body, 'html'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "#ParkiApp")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
