from django.contrib import admin
from . import models
# Register your models here.
class Useradmin(admin.ModelAdmin):
    list_display=('name','email','mobile')

admin.site.register(models.User,Useradmin)

class Expenseadmin(admin.ModelAdmin):
    list_display=('user','amount','split_method')

admin.site.register(models.Expense,Expenseadmin)

class Splitadmin(admin.ModelAdmin):
    list_display=('expense','participant','amount_owed')

admin.site.register(models.Split,Splitadmin)
