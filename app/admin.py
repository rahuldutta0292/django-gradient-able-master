# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Deposit
from .models import StatutoryDeposit


admin.site.register(Deposit)
admin.site.register(StatutoryDeposit)
# Register your models here.
