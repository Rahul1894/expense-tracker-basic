from django.urls import path
from . import views

urlpatterns = [
    path('create_user/', views.create_user, name='create_user'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('user_expenses/', views.user_expenses, name='user_expenses'),
    path('balance_sheet/', views.balance_sheet, name='balance_sheet'),
]
