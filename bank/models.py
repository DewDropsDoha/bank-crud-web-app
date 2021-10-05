from typing import Iterable
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import PositiveIntegerField

# Create your models here.

class Account(models.Model):
    balance = models.PositiveIntegerField(verbose_name="Enter Amount")
    deposit = models.TextField(default="")
    withdraw = models.TextField(default="")