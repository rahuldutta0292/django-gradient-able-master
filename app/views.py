# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template

from .forms import DepositForm
from .models import Deposit
from .models import StatutoryDeposit


# Create your views here.


def create_deposit(request):
    form = DepositForm
    if request.method == 'POST':
        form = DepositForm(request.POST)
        print(form.data)
        if form.is_valid():
            form.save()
        else:
            print("form not valid")
            # redirect('home') //redirect to any page you wish to send the user after registration
    context = {'form': form}
    return render(request, 'CreateDeposit.html', context)


# def filelist(request):
#     file_list = File.objects.all()
#     section_list = Section.objects.all()
#     context = {"file_list": file_list, "section_list": section_list}
#     return render(request, 'FileList.html', context)


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
