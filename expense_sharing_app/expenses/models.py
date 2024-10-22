from django.db import models # type: ignore
from django.contrib.auth.models import AbstractUser #type:ignore
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    split_method = models.CharField(max_length=50, choices=[('equal', 'Equal'), ('exact', 'Exact'), ('percentage', 'Percentage')])

    def __str__(self):
        return f"{self.description} - {self.amount}"
    
class Split(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    amount_owed = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.participant} owes {self.amount_owed} for {self.expense.description}"
