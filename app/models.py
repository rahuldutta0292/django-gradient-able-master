# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User


class Employee(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Deposit(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    entry_date = models.DateField()
    order_date = models.CharField(max_length=100)
    misc_case_no = models.CharField(max_length=500, blank=True, null=True)
    main_case_no = models.CharField(max_length=500)
    appellant = models.CharField(max_length=500)
    party_name = models.CharField(max_length=500)
    amount = models.CharField(max_length=500)
    in_words = models.CharField(max_length=1000)
    cheque_no = models.CharField(max_length=100)
    cheque_date = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=50)

    def __str__(self):
        return self.main_case_no


class StatutoryDeposit(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    entry_date = models.DateField()
    order_date = models.CharField(max_length=100)
    mac_case_details = models.CharField(max_length=800)
    party_name = models.CharField(max_length=500)
    amount = models.CharField(max_length=500)
    in_words = models.CharField(max_length=500)
    cheque_no = models.CharField(max_length=100)
    cheque_date = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=50)

    def __str__(self):
        return self.mac_case_no


# Create your models here.
