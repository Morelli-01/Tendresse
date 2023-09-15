from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_imported
from django.contrib.auth import logout as logout_imported
from Tendresse.init import logging as log
import logging
from cart.models import Cart

@log
def home(request):
    return render(request, template_name='home.html')

def login(request):
    if request.user.is_authenticated:
        return redirect(to='/home#already_logged')
    if request.method == 'GET':
        return render(request, template_name='login.html')

    if request.method == 'POST':
        user = User.objects.all().filter(username=request.POST.get('email'), password=request.POST.get('password')).first()
        if user is not None:
            login_imported(request=request, user=user)
            logging.info('Logged user: ' + str(request.user))
            if Cart.objects.all().filter(ip=request.META.get('REMOTE_ADDR')).exists():
                cart = Cart.objects.all().filter(ip=request.META.get('REMOTE_ADDR')).first()
                if Cart.objects.all().filter(user=user).exists():
                    Cart.objects.all().filter(user=user).first().delete()
                cart.user = user
                cart.ip = ''
                cart.save()

            return redirect('/home#loggedin')
        else:
            message = 'Username o password sono sbagliati, Riprova'
            ctx = {
                'msg': message
            }
        return render(request, template_name='login.html', context=ctx)

def register(request):
    if request.method == 'GET':
        return render(request, template_name='register.html')
    elif request.method == 'POST':
        if request.POST.get('name') == '' or \
                request.POST.get('surname') == '' or \
                request.POST.get('email') == '' or \
                request.POST.get('password') == '':
            return redirect(to='/register#missing_inputs')
        user = User()
        user.first_name = request.POST.get('name')
        user.last_name = request.POST.get('surname')
        user.email = request.POST.get('email')
        user.username = request.POST.get('email')
        user.password = request.POST.get('password')
        response = HttpResponse()
        if User.objects.filter(username=user.username).exists():
            response.status_code = 400
        else:
            user.save()
            login_imported(request=request, user=user)
            logging.info('Logged user: ' + str(request.user))
            if Cart.objects.all().filter(ip=request.META.get('REMOTE_ADDR')).exists():
                cart = Cart.objects.all().filter(ip=request.META.get('REMOTE_ADDR')).first()
                if Cart.objects.all().filter(user=user).exists():
                    Cart.objects.all().filter(user=user).first().delete()
                cart.user = user
                cart.ip = ''
                cart.save()
            return redirect(to='/account')

        return response

@login_required
def logout(request):
    logout_imported(request)
    return redirect(to='/login#loggedout')

@log
def orari(request):
    return render(request, template_name='orari.html')