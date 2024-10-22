from django.shortcuts import render, redirect #type:ignore 
from .models import User, Expense, Split
from .forms import UserForm, ExpenseForm

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_expenses')
    else:
        form = UserForm()
    return render(request, 'expenses/create_user.html', {'form': form})

from django.shortcuts import render, redirect #type:ignore
from .forms import ExpenseForm
from django.contrib.auth import get_user_model #type: ignore


def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user  # Ensure this points to the correct user instance
            expense.save()
            return redirect('balance_sheet')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})



def user_expenses(request):
    users = User.objects.all()
    expenses = Expense.objects.all()
    return render(request, 'expenses/user_expenses.html', {'users': users, 'expenses': expenses})

def balance_sheet(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses/balance_sheet.html', {'expenses': expenses})
