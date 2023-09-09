import datetime
import os
import random
import subprocess

import MySQLdb
import django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core import exceptions
import re

from bolle_vecchie.models import *
from Bolle.models import *


# Create your views here.

@login_required
def create_bolla(request):
    if request.user.is_staff:
        if request.method == 'GET':
            ctx = {
                'dst': Bolla_dst.objects.all().filter(alt_dst=False)
            }
            return render(request=request, template_name='bolla_form.html', context=ctx)
        elif request.method == 'POST':
            for p in request.POST:
                re.fullmatch('^note', p)
                if request.POST[p] == '' and re.fullmatch('^note.*', p) is None and p != 'alt-dst-line2':
                    raise exceptions.BadRequest()

            bolla = Bolla()
            bolla.data = datetime.datetime.fromisoformat(request.POST['data_bolla'])
            descr = []
            for p in request.POST:
                if re.fullmatch('^descr.*', p) is not None:
                    descr.append(request.POST[p])
            bolla.descrizioni = {
                'descrizioni': descr
            }

            qta = []
            for p in request.POST:
                if re.fullmatch('^qta.*', p) is not None:
                    qta.append(request.POST[p])
            bolla.qta = {
                'qta': qta
            }

            um = []
            for p in request.POST:
                if re.fullmatch('^um.*', p) is not None:
                    um.append(request.POST[p])
            bolla.um = {
                'um': um
            }

            note = []
            for p in request.POST:
                if re.fullmatch('^note.*', p) is not None:
                    note.append(request.POST[p])
            bolla.note = {
                'note': note
            }

            bolla.lavorazione = request.POST['lavorazione']
            bolla.respSpedizione = request.POST['resp']
            bolla.dataTrasp = datetime.datetime.fromisoformat(request.POST['data_trasporto'])
            bolla.aspetto = request.POST['aspetto']
            bolla.dst = Bolla_dst.objects.get(name=request.POST['dst'])
            if str(request.POST['number']) == '0':
                if not Bolla.objects.all().exists():
                    bolla.number = 0
                else:
                    last_bolla = Bolla.objects.all().order_by('number').last()
                    bolla.number = int(last_bolla.number) + 1

                bolla.year = datetime.datetime.fromisoformat(request.POST['data_trasporto']).year
            else:
                bolla.number = int(request.POST['number'])
                bolla.year = int(request.POST['year'])

            if request.POST.get('alt-dst-name') is not None:
                bolla.sameAddress = False
                alt_dst = Bolla_dst.objects.get_or_create(name=request.POST['alt-dst-name'])[0]
                print('alt_dst: ' + str(alt_dst))
                # alt_dst.name = request.POST['alt-dst-name']
                alt_dst.line1 = request.POST['alt-dst-line1']
                # alt_dst.line2 = request.POST['alt-dst-line2']
                alt_dst.city = request.POST['alt-dst-city']
                alt_dst.province = request.POST['alt-dst-province']
                alt_dst.zip = request.POST['alt-dst-zip']
                alt_dst.country = request.POST['alt-dst-country']
                alt_dst.alt_dst = True
                alt_dst.save()
                bolla.dst2 = Bolla_dst.objects.all().get(name=request.POST['alt-dst-name'])

            print(bolla)
            program_path = 'BollaDrawer' + os.path.sep + 'target' + os.path.sep + 'BollaDrawer-1.0-SNAPSHOT.jar'
            cmd_command = 'java -jar  ' + program_path + ' ' + "\"" + \
                          bolla.to_json().replace("'", "`").replace("\"", "'") + "\""
            print(cmd_command)
            try:
                # Esegui il comando CMD
                result = subprocess.run(cmd_command, capture_output=True, text=True, check=True, shell=True)

                # Stampa l'output
                print("Output CMD:")
                print(result.stdout)

            except subprocess.CalledProcessError as e:
                print("Errore durante l'esecuzione del comando CMD:")
                print(e)
                print(e.stderr)
            print(bolla)
            try:
                bolla.save()
            except django.db.utils.IntegrityError as e:
                return redirect('/bolle/#already_exist')
            return redirect('/bolle/#successfully_created')

    else:
        raise exceptions.PermissionDenied()


@login_required
def add_dst(request):
    if request.user.is_staff:
        if request.method == 'GET':
            ctx = {
                'dst': Bolla_dst.objects.all().filter(alt_dst=False)
            }
            return render(request=request, template_name='dst_form.html', context=ctx)

        if request.method == 'POST':
            for p in request.POST:
                if request.POST[p] == '' and p != 'line2':
                    raise exceptions.BadRequest()
                if Bolla_dst.objects.filter(name=request.POST['name']).exists():
                    return redirect('/bolle/dst/#dst_already_exists')
            new_dst = Bolla_dst()
            new_dst.name = request.POST['name']
            new_dst.line1 = request.POST['line1']
            new_dst.line2 = request.POST['line2']
            new_dst.city = request.POST['city']
            new_dst.zip = request.POST['zip']
            new_dst.province = request.POST['province']
            new_dst.country = request.POST['country']
            new_dst.save()
            # print(new_dst)
            return redirect('/bolle/dst/#successfully_added')

    else:
        raise exceptions.PermissionDenied()


@login_required
def edit_dst(request, name):
    if request.user.is_staff:
        if request.method == 'GET':
            ctx = {
                'selected': Bolla_dst.objects.get(name=name),
                'dst': Bolla_dst.objects.all().filter(alt_dst=False)
            }
            return render(request=request, template_name='dst_edit_form.html', context=ctx)

        if request.method == 'POST':
            for p in request.POST:
                if request.POST[p] == '' and p != 'line2':
                    raise exceptions.BadRequest()
                # if Bolla_dst.objects.filter(name=request.POST['name']).exists():
                #     return redirect('/bolle/dst/#dst_already_exists')
            edit_dst = Bolla_dst.objects.get(name=name)
            # edit_dst.delete()
            edit_dst.name = request.POST['name']
            edit_dst.line1 = request.POST['line1']
            edit_dst.line2 = request.POST['line2']
            edit_dst.city = request.POST['city']
            edit_dst.zip = request.POST['zip']
            edit_dst.province = request.POST['province']
            edit_dst.country = request.POST['country']

            edit_dst.save()
            # print(new_dst)
            return redirect('/bolle/dst/#successfully_edited')

    else:
        raise exceptions.PermissionDenied()


@login_required
def delete_dst(request, name):
    if request.user.is_staff:
        if request.method == 'POST':
            Bolla_dst.objects.get(name=name).delete()
            return redirect('/bolle/dst/#successfully_deleted')

    else:
        raise exceptions.PermissionDenied()


@login_required
def dash(request):
    if request.user.is_staff:
        if request.method == 'GET':
            ctx = {
                'bolle': Bolla.objects.all().order_by('number'),
                'old_bolle': bolle_old.objects.all().order_by('anno', 'numero'),
                'dsts': Bolla_dst.objects.all()
            }
            return render(request, template_name='dashboard.html', context=ctx)

    else:
        raise exceptions.PermissionDenied()


@login_required
def delete_bolla(request, number_year):
    if request.user.is_staff:
        if request.method == 'POST':
            (number, year) = str(number_year).split('-')
            bolla_to_del = Bolla.objects.get(number=number, year=year)
            print(bolla_to_del)
            bolla_file_path = 'static/Bolle/' + str(number) + '-' + str(year) + '.pdf'
            try:
                os.remove(bolla_file_path)
            except:
                print('Bolla file not found so assumed it was already deleted')
            bolla_to_del.delete()
            return redirect('/bolle/dashboard/#' + str(number_year) + '_succesfully_removed')

    else:
        raise exceptions.PermissionDenied()


@login_required
def edit_bolla(request, number_year):
    if request.user.is_staff:
        if request.method == 'GET':
            (number, year) = str(number_year).split('-')

            ctx = {
                'dst': Bolla_dst.objects.all().filter(alt_dst=False),
                'bolla': Bolla.objects.all().get(number=number, year=year)
            }
            return render(request=request, template_name='edit_bolla_form.html', context=ctx)
        elif request.method == 'POST':
            # elimina la bolla
            (number, year) = str(number_year).split('-')
            bolla_to_del = Bolla.objects.get(number=number, year=year)
            print(bolla_to_del)
            bolla_file_path = 'static' + os.path.sep + 'Bolle' + os.path.sep + str(number) + '-' + str(year) + '.pdf'
            try:
                os.remove(bolla_file_path)
            except:
                print('Bolla file not found so assumed it was already deleted')
            bolla_to_del.delete()

            for p in request.POST:
                re.fullmatch('^note', p)
                if request.POST[p] == '' and re.fullmatch('^note.*', p) is None and p != 'alt-dst-line2':
                    raise exceptions.BadRequest()

            # ricrea la bolla

            bolla = Bolla()
            bolla.data = datetime.datetime.fromisoformat(request.POST['data_bolla'])
            descr = []
            for p in request.POST:
                if re.fullmatch('^descr.*', p) is not None:
                    descr.append(request.POST[p])
            bolla.descrizioni = {
                'descrizioni': descr
            }

            qta = []
            for p in request.POST:
                if re.fullmatch('^qta.*', p) is not None:
                    qta.append(request.POST[p])
            bolla.qta = {
                'qta': qta
            }

            um = []
            for p in request.POST:
                if re.fullmatch('^um.*', p) is not None:
                    um.append(request.POST[p])
            bolla.um = {
                'um': um
            }

            note = []
            for p in request.POST:
                if re.fullmatch('^note.*', p) is not None:
                    note.append(request.POST[p])
            bolla.note = {
                'note': note
            }

            bolla.lavorazione = request.POST['lavorazione']
            bolla.respSpedizione = request.POST['resp']
            bolla.dataTrasp = datetime.datetime.fromisoformat(request.POST['data_trasporto'])
            bolla.aspetto = request.POST['aspetto']
            bolla.dst = Bolla_dst.objects.get(name=request.POST['dst'])
            if str(request.POST['number']) == '0':
                if not Bolla.objects.all().exists():
                    bolla.number = 0
                else:
                    last_bolla = Bolla.objects.all().order_by('number').last()
                    bolla.number = int(last_bolla.number) + 1

                bolla.year = datetime.datetime.fromisoformat(request.POST['data_trasporto']).year
            else:
                bolla.number = int(request.POST['number'])
                bolla.year = int(request.POST['year'])

            if request.POST.get('alt-dst-name') is not None:
                bolla.sameAddress = False
                alt_dst = Bolla_dst.objects.get_or_create(name=request.POST['alt-dst-name'])[0]
                print('alt_dst: ' + str(alt_dst))
                # alt_dst.name = request.POST['alt-dst-name']
                alt_dst.line1 = request.POST['alt-dst-line1']
                # alt_dst.line2 = request.POST['alt-dst-line2']
                alt_dst.city = request.POST['alt-dst-city']
                alt_dst.province = request.POST['alt-dst-province']
                alt_dst.zip = request.POST['alt-dst-zip']
                alt_dst.country = request.POST['alt-dst-country']
                alt_dst.alt_dst = True
                alt_dst.save()
                bolla.dst2 = Bolla_dst.objects.all().get(name=request.POST['alt-dst-name'])

            print(bolla)
            program_path = 'BollaDrawer' + os.path.sep + 'target' + os.path.sep + 'BollaDrawer-1.0-SNAPSHOT.jar'
            cmd_command = 'java -jar  ' + program_path + ' ' + "\"" + \
                          bolla.to_json().replace("'", "`").replace("\"", "'") + "\""
            print(cmd_command)
            try:
                # Esegui il comando CMD
                result = subprocess.run(cmd_command, capture_output=True, text=True, check=True, shell=True)

                # Stampa l'output
                print("Output CMD:")
                print(result.stdout)

            except subprocess.CalledProcessError as e:
                print("Errore durante l'esecuzione del comando CMD:")
                print(e)
                print(e.stderr)
            print(bolla)
            try:
                bolla.save()
            except django.db.utils.IntegrityError as e:
                return redirect('/bolle/#already_exist')

            return redirect('/bolle/dashboard/#' + str(number_year) + '_succesfully_edited')

    else:
        raise exceptions.PermissionDenied()
