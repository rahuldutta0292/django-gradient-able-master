# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .models import Deposit
from .models import StatutoryDeposit
from .forms import DepositForm
from .forms import StatutoryDepositForm


# Create your views here.


def create_deposit(request):
    form = DepositForm
    display = ""
    saved_deposit = {}
    if request.method == 'POST':
        form = DepositForm(request.POST)
        print(form.data)
        if form.is_valid():
            saved_deposit = form.save()
            display = "deposit entry successful"

        else:
            display = "Deposit Entry Not Successful"
            print(form.errors)
            # redirect('home') //redirect to any page you wish to send the user after registration
    context = {'form': form, 'display': display, 'saved_deposit': saved_deposit}
    return render(request, 'CreateDeposit.html', context)


def create_statutory_deposit(request):
    form = StatutoryDepositForm
    display = ""
    saved_statutory_deposit = {}
    if request.method == 'POST':
        form = StatutoryDepositForm(request.POST)
        print(form.data)
        if form.is_valid():
            saved_statutory_deposit = form.save()
            display = "deposit entry successful"

        else:
            display = "Deposit Entry Not Successful"
            print(form.errors)
            # redirect('home') //redirect to any page you wish to send the user after registration
    context = {'form': form, 'display': display, 'saved_statutory_deposit': saved_statutory_deposit}
    return render(request, 'CreateStatutoryDeposit.html', context)


# def filelist(request):
#     file_list = File.objects.all()
#     section_list = Section.objects.all()
#     context = {"file_list": file_list, "section_list": section_list}
#     return render(request, 'PrintDeposit.html', context)


def print_deposit(request, pk):
    deposit = Deposit.objects.get(pk=pk)
    context = {"deposit": deposit}
    return render(request, 'PrintDeposit.html', context)


@login_required(login_url="/login/")
def index(request):
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))
