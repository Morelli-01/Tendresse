from django.http import HttpResponse
from django.shortcuts import render, redirect
from Tendresse.init import staff_required

import os

from bolle_vecchie.models import bolle_old


# Create your views here.

@staff_required
def get_file_url(request,number_year):
    directory = "static\\OldBolle"
    # Cerca i file nella cartella
    response = HttpResponse('not_found')
    for filename in os.listdir(directory):
        if(filename.startswith(number_year)):
            response = HttpResponse(filename)

    return response

@staff_required
def del_file(request,number_year):
    (number, year) = str(number_year).split('-')
    if request.method == 'GET':
        try:
            bolle_old.objects.get(numero=number, anno=year).delete()
            return HttpResponse(status=200)
        except:
            return HttpResponse(status=400)
    elif request.method == 'POST':
        try:
            bolle_old.objects.get(numero=number, anno=year).delete()
            return redirect('/bolle/dashboard/#' + str(number_year) + '_succesfully_removed')
        except:
            return redirect('/bolle/dashboard/')
