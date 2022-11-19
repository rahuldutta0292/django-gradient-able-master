# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('CreateDeposit/', views.create_deposit, name="create_deposit"),
    path('CreateStatutoryDeposit/', views.create_statutory_deposit, name="create_statutory_deposit"),
    path('PrintDeposit/<int:pk>/', views.print_deposit, name="print_deposit"),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
]
